"""Contract tests against the live Deadlock API. Run with ``pytest -m contract``.

They check what the generated types cannot: real response shapes, the untyped
match metadata layout and the numbers the SDK derives.
"""

from __future__ import annotations

import time
from collections.abc import Iterator

import pytest

from deadlock_sdk import RANK_NAMES, Deadlock

pytestmark = pytest.mark.contract


@pytest.fixture(scope="module")
def live() -> Iterator[Deadlock]:
    with Deadlock(user_agent="deadlock-sdk-python contract tests") as dl:
        yield dl


def last_week() -> int:
    return int(time.time()) - 7 * 86400


def test_assets(live: Deadlock) -> None:
    heroes = live.heroes.list()
    assert len(heroes) > 20
    assert {"id", "name", "class_name"} <= set(heroes[0])
    shop = live.items.shop()
    assert len(shop) > 80
    assert {i["item_slot_type"] for i in shop} == {"weapon", "vitality", "spirit"}
    # The built-in fallback names must match the live ones.
    for r in live.ranks.list():
        assert RANK_NAMES[r["tier"]] == r["name"]


def test_hero_stats_add_up(live: Deadlock) -> None:
    stats = live.heroes.stats(min_unix_timestamp=last_week())
    assert 11.5 < sum(s.pick_rate for s in stats) < 12.5
    assert any(t.tier == "S" for t in live.heroes.tier_list(min_unix_timestamp=last_week()))


def test_matchups(live: Deadlock) -> None:
    hero = live.heroes.list()[0]
    assert len(live.heroes.counters(hero["id"], min_unix_timestamp=last_week())) > 10
    assert len(live.heroes.synergies(hero["id"], min_unix_timestamp=last_week())) > 10


def test_players_and_scoreboard(live: Deadlock) -> None:
    board = live.leaderboard.get("eu", limit=20)
    assert len(board) == 20
    assert board[0].rank == 1
    # A real public player from the leaderboard instead of a hardcoded id.
    account_id = next(a for r in board for a in r.account_ids)
    history = live.players.match_history(account_id, limit=20)
    assert history
    newest = history[0]
    s = live.matches.scoreboard(newest["match_id"])
    assert len(s.players) == 12
    me = next(p for p in s.players if p.account_id == account_id)
    assert me.hero_id == newest["hero_id"]
    assert me.kills == newest["player_kills"]
    assert me.final_items


def test_patches_and_sql(live: Deadlock) -> None:
    latest = live.patches.latest()
    assert latest
    assert latest.url.startswith("https://")
    assert "match_player" in live.sql.tables()
    columns = {c["name"] for c in live.sql.schema("match_player")}
    assert {"match_id", "hero_id", "account_id"} <= columns
