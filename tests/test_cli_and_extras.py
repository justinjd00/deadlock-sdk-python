from __future__ import annotations

import json
import re
import time
from pathlib import Path

import pytest
import respx
from typing_extensions import assert_type

from deadlock_sdk import (
    DEFAULT_USER_AGENT,
    Deadlock,
    HeroStat,
    PlayerSummary,
    Scoreboard,
    TierEntry,
    __version__,
)
from deadlock_sdk.cli import run
from deadlock_sdk.pandas import to_dataframe
from deadlock_sdk.types import Hero, PlayerMatchHistoryEntry

from .conftest import MATCH_ID, SUBJECT


@pytest.fixture
def cli(api: respx.Router, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):  # type: ignore[no-untyped-def]
    monkeypatch.setenv("NO_COLOR", "1")
    monkeypatch.delenv("DEADLOCK_API_KEY", raising=False)

    def invoke(*argv: str) -> tuple[int, str, str]:
        code = run(list(argv))
        captured = capsys.readouterr()
        return code, captured.out, captured.err

    return invoke


def test_cli_player_card(cli) -> None:  # type: ignore[no-untyped-def]
    code, out, _ = cli("player", str(SUBJECT))
    assert code == 0
    assert "Test Player" in out
    assert re.search(r"Rank\s+[A-Z][a-z]+ \d", out)
    assert re.search(r"\d+W \d+L", out)
    assert "Top heroes" in out


def test_cli_name_search_fallback(cli) -> None:  # type: ignore[no-untyped-def]
    code, _, err = cli("rank", "Test Player")
    assert code == 0
    assert f"Using Test Player ({SUBJECT})" in err


def test_cli_tables_and_json(cli) -> None:  # type: ignore[no-untyped-def]
    code, out, _ = cli("matches", str(SUBJECT), "--limit", "3")
    assert code == 0
    lines = out.strip().splitlines()
    assert re.match(r"when\s+match\s+hero\s+result\s+kda", lines[0])
    assert len(lines) == 4
    code, out, _ = cli("--json", "matches", str(SUBJECT), "--limit", "2")
    assert json.loads(out)
    assert len(json.loads(out)) == 2


def test_cli_scoreboard(cli) -> None:  # type: ignore[no-untyped-def]
    code, out, _ = cli("match", str(MATCH_ID))
    assert code == 0
    assert "Hidden King" in out
    assert "Archmother" in out
    assert len(re.findall(r"\bWIN\b", out)) == 1


def test_cli_meta_defaults_to_30_days(cli, api: respx.Router) -> None:  # type: ignore[no-untyped-def]
    code, out, _ = cli("tiers", "--min-rank", "oracle 3", "--limit", "5")
    assert code == 0
    assert out.splitlines()[1].startswith("S")
    params = next(c.request.url.params for c in api.calls if c.request.url.path.endswith("hero-stats"))
    assert params["min_average_badge"] == "83"
    assert abs(time.time() - int(params["min_unix_timestamp"]) - 30 * 86400) < 120


@pytest.mark.parametrize(
    "argv",
    [
        ["hero", "1"],
        ["items", "--limit", "3"],
        ["leaderboard", "eu", "--limit", "3"],
        ["live", "--limit", "2"],
        ["patches", "--limit", "1"],
        ["search", "test"],
        ["steamid", "[U:1:22202]"],
        ["sql", "SELECT 1"],
        ["sql", "tables"],
    ],
)
def test_cli_commands(cli, argv: list[str]) -> None:  # type: ignore[no-untyped-def]
    code, out, _ = cli(*argv)
    assert code == 0, argv
    assert out.strip()


def test_cli_errors(cli) -> None:  # type: ignore[no-untyped-def]
    assert cli("leaderboard", "mars")[0] == 2
    assert cli("tiers", "--min-rank", "diamond")[0] == 2
    assert cli("steamid", "not-an-id")[0] == 2
    with pytest.raises(SystemExit):
        cli("nope")


def test_dataframe_export(dl: Deadlock) -> None:
    df = to_dataframe(dl.heroes.tier_list(min_matches=1))
    assert {"tier", "name", "win_rate", "pick_rate", "confidence"} <= set(df.columns)
    assert "raw" not in df.columns
    summary = to_dataframe([dl.players.summary(SUBJECT)])
    assert "rank_label" in summary.columns
    raw = to_dataframe(dl.heroes.list())
    assert "class_name" in raw.columns


def test_version_matches_pyproject() -> None:
    pyproject = (Path(__file__).resolve().parent.parent / "pyproject.toml").read_text()
    assert 'name = "deadlock-sdk"' in pyproject
    assert f"deadlock-sdk-python/{__version__}" in DEFAULT_USER_AGENT


def typing_contract(dl: Deadlock) -> None:
    """Never called. mypy checks these lines, `warn_unused_ignores` makes the ignores assertions."""
    assert_type(dl.api.get("/v1/assets/heroes", query={"only_active": True}), list[Hero])
    assert_type(
        dl.api.get("/v1/players/{account_id}/match-history", path_params={"account_id": 1}),
        list[PlayerMatchHistoryEntry],
    )
    assert_type(dl.players.summary(1), PlayerSummary)
    assert_type(dl.heroes.stats(), list[HeroStat])
    assert_type(dl.heroes.tier_list(), list[TierEntry])
    assert_type(dl.matches.scoreboard(1), Scoreboard)
    dl.api.get("/v1/does-not-exist")  # type: ignore[call-overload]
    dl.api.get("/v1/players/{account_id}/rank")  # type: ignore[call-overload]
    dl.api.get("/v1/assets/heroes", query={"language": "klingon"})  # type: ignore[call-overload]
    dl.players.summary({"id": 1})  # type: ignore[arg-type]
