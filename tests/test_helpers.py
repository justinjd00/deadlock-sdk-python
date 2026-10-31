from __future__ import annotations

from typing import Any

import pytest

from deadlock_sdk import (
    DeadlockError,
    decode_badge,
    did_win,
    encode_badge,
    game_mode_name,
    is_player_input,
    kda,
    match_mode_name,
    normalize_region,
    parse_badge,
    steam_profile_url,
    summarize_history,
    to_account_id,
    to_steam_id2,
    to_steam_id3,
    to_steam_id64,
    wilson_lower_bound,
    win_rate,
)
from deadlock_sdk.helpers import chunk, normalize_text

from .conftest import fixture

# Valve's documented example account.
ID = 22202


@pytest.mark.parametrize(
    "value",
    [ID, "22202", 76561197960287930, "76561197960287930", "[U:1:22202]", "U:1:22202", "STEAM_1:0:11101", "STEAM_0:0:11101",
     "https://steamcommunity.com/profiles/76561197960287930/", "  76561197960287930 "],
)  # fmt: skip
def test_reads_every_steam_id_format(value: int | str) -> None:
    assert to_account_id(value) == ID


def test_converts_to_every_format() -> None:
    assert to_steam_id64(ID) == "76561197960287930"
    assert to_steam_id3(ID) == "[U:1:22202]"
    assert to_steam_id2(ID) == "STEAM_1:0:11101"
    assert to_steam_id2(22203) == "STEAM_1:1:11101"
    assert steam_profile_url(ID) == "https://steamcommunity.com/profiles/76561197960287930"


def test_explains_vanity_urls_and_rejects_garbage() -> None:
    with pytest.raises(DeadlockError, match="vanity"):
        to_account_id("https://steamcommunity.com/id/gaben")
    bad: Any
    for bad in ["", "abc", "-5", "1.5", "STEAM_1:2:3", -1, True]:
        with pytest.raises(DeadlockError) as info:
            to_account_id(bad)
        assert info.value.code == "INVALID_INPUT"
    assert is_player_input("[U:1:5]")
    assert not is_player_input("nope")


def test_decodes_badges() -> None:
    b = decode_badge(115)
    assert (b.tier, b.subrank, b.name, b.label) == (11, 5, "Eternus", "Eternus 5")
    assert decode_badge(0).label == "Obscurus"
    assert decode_badge(-3).badge == 0


def test_uses_live_rank_assets() -> None:
    b = decode_badge(115, fixture("ranks"))
    assert b.name == "Eternus"
    assert b.image
    assert b.image.startswith("https://")
    assert b.color
    assert b.color.startswith("#")


def test_parses_what_people_type() -> None:
    assert parse_badge("oracle") == 81
    assert parse_badge("Oracle 3") == 83
    assert parse_badge("eternus6") == 116
    assert parse_badge("obscurus") == 0
    assert parse_badge("81") == 81
    assert encode_badge(8, 1) == 81
    for bad in ["diamond", "oracle 7"]:
        with pytest.raises(DeadlockError):
            parse_badge(bad)


def test_stats_math() -> None:
    assert win_rate(3, 4) == 0.75
    assert win_rate(0, 0) == 0
    assert kda(10, 0, 5) == 15
    assert kda(10, 5, 5) == 3
    # 6/10 has the higher raw win rate but far less evidence than 550/1000.
    assert wilson_lower_bound(550, 1000) > wilson_lower_bound(6, 10)
    assert wilson_lower_bound(0, 0) == 0
    assert wilson_lower_bound(500, 1000) == pytest.approx(0.469, abs=1e-3)
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_modes_and_regions() -> None:
    assert game_mode_name(1) == "Normal"
    assert match_mode_name(4) == "Ranked"
    assert match_mode_name(99) == "Mode 99"
    assert normalize_region("eu") == "Europe"
    assert normalize_region("North America") == "NAmerica"
    assert normalize_region("SAMERICA") == "SAmerica"
    with pytest.raises(DeadlockError, match="Unknown region"):
        normalize_region("mars")
    assert normalize_text("Lady Geist") == normalize_text("ladygeist")


def test_history_summary_agrees_with_a_manual_count() -> None:
    history: list[Any] = fixture("match-history")
    s = summarize_history(history)
    wins = sum(1 for m in history if m["match_result"] == m["player_team"])
    assert s.matches == len(history)
    assert s.wins == wins
    assert s.losses == len(history) - wins
    assert s.win_rate == pytest.approx(wins / len(history), abs=1e-3)
    assert sum(h.matches for h in s.heroes) == len(history)
    assert s.heroes[0].matches >= s.heroes[-1].matches
    assert s.first_match_at
    assert s.last_match_at
    assert s.last_match_at >= s.first_match_at


def test_streak_counts_from_the_newest_match() -> None:
    base: dict[str, Any] = fixture("match-history")[0]

    def m(t: int, win: bool) -> Any:
        return {**base, "start_time": t, "player_team": 0, "match_result": 0 if win else 1}

    s = summarize_history([m(1, False), m(3, True), m(2, False), m(4, True)])
    assert (s.streak.kind, s.streak.count) == ("win", 2)
    assert did_win(m(1, True))
    assert summarize_history([]).streak.kind == "none"
