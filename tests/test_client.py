from __future__ import annotations

from typing import Any

import httpx
import pytest
import respx

from deadlock_sdk import ATTRIBUTION, CallOptions, Deadlock, DeadlockError, MemoryCache, worst_matchups

from .conftest import BASE, MATCH_ID, SUBJECT, fixture, paths


class TestTypedApi:
    def test_fills_path_params_and_joins_lists(self, dl: Deadlock, api: respx.Router) -> None:
        dl.api.get("/v1/players/{account_id}/rank", path_params={"account_id": SUBJECT})
        dl.api.get("/v1/players/rank", query={"account_ids": [1, 2]})
        urls = [str(c.request.url) for c in api.calls]
        assert urls[0] == f"{BASE}/v1/players/{SUBJECT}/rank"
        assert "account_ids=1%2C2" in urls[1]

    def test_missing_path_params_fail_before_the_network(self, dl: Deadlock, api: respx.Router) -> None:
        with pytest.raises(DeadlockError) as info:
            dl.api.get("/v1/players/{account_id}/rank", path_params={})  # type: ignore[call-overload]
        assert info.value.code == "INVALID_INPUT"
        assert not api.calls


class TestCache:
    def test_serves_repeats_from_cache_and_bypasses_with_fresh(self, dl: Deadlock, api: respx.Router) -> None:
        dl.heroes.list()
        dl.heroes.list()
        assert len(api.calls) == 1
        dl.heroes.list(options=CallOptions(fresh=True))
        assert len(api.calls) == 2

    def test_keys_by_full_url(self, dl: Deadlock) -> None:
        assert len(dl.heroes.list(only_active=False)) > len(dl.heroes.list())

    def test_can_be_disabled_or_replaced(self, api: respx.Router) -> None:
        with Deadlock(cache=False, retry=None) as dl:
            dl.heroes.list()
            dl.heroes.list()
        assert len(api.calls) == 2
        store = MemoryCache(max_entries=1)
        with Deadlock(cache=store, retry=None) as dl:
            dl.heroes.list()
            dl.items.list()
        assert len(store) == 1

    def test_per_resource_ttl(self, api: respx.Router) -> None:
        with Deadlock(retry=None, ttl={"assets": 0}) as dl:
            dl.heroes.list()
            dl.heroes.list()
        assert len(api.calls) == 2

    def test_clear(self, dl: Deadlock, api: respx.Router) -> None:
        dl.heroes.list()
        dl.clear_cache()
        dl.heroes.list()
        assert len(api.calls) == 2


class TestPlayers:
    def test_summary_combines_rank_history_profile_and_heroes(self, dl: Deadlock) -> None:
        s = dl.players.summary(f"[U:1:{SUBJECT}]", matches=20)
        assert s.account_id == SUBJECT
        assert s.steam_id64 == str(76561197960265728 + SUBJECT)
        assert s.profile
        assert s.profile["personaname"] == "Test Player"
        assert s.rank
        assert s.rank.label.split()[0].isalpha()
        assert s.recent.matches == 20
        assert s.top_heroes
        assert all(not h.name.startswith("Hero ") for h in s.top_heroes)

    def test_summary_tolerates_private_players(self, api: respx.Router) -> None:
        api.routes[r"/v1/players/\d+/rank"].respond(403, json={"error": "protected"})
        api.routes[r"/v1/players/steam"].respond(403)
        with Deadlock(retry=None) as dl:
            s = dl.players.summary(SUBJECT)
        assert s.rank is None
        assert s.profile is None
        assert s.recent.matches > 0

    def test_filters_history_locally(self, dl: Deadlock) -> None:
        history = fixture("match-history")
        hero_id, since = history[0]["hero_id"], history[5]["start_time"]
        rows = dl.players.match_history(SUBJECT, hero_id=hero_id, since=since, limit=3)
        assert len(rows) <= 3
        assert all(r["hero_id"] == hero_id and r["start_time"] >= since for r in rows)
        assert [r["start_time"] for r in rows] == sorted((r["start_time"] for r in rows), reverse=True)
        assert all(r["match_mode"] == 4 for r in dl.players.match_history(SUBJECT, match_modes=[4]))

    def test_batches_rank_lookups_by_1000(self, dl: Deadlock, api: respx.Router) -> None:
        ranks = dl.players.ranks([*range(1, 2501), 1, 2])
        assert len(ranks) == 2500
        assert ranks[0].label == "Oracle 1"
        assert paths(api).count("/v1/players/rank") == 3

    def test_search_requires_text(self, dl: Deadlock) -> None:
        assert dl.players.search("test")[0]["personaname"] == "Test Player"
        with pytest.raises(DeadlockError):
            dl.players.search("  ")


class TestMatches:
    def test_scoreboard(self, dl: Deadlock) -> None:
        meta = fixture("match-metadata")["match_info"]
        s = dl.matches.scoreboard(MATCH_ID)
        assert s.match_id == MATCH_ID
        assert [len(t) for t in s.teams] == [6, 6]
        assert all(p.won for p in s.winners)
        assert len(s.winners) == 6
        assert all(not p.hero_name.startswith("Hero ") for p in s.players)
        assert any(p.final_items for p in s.players)
        assert sum(p.kills for p in s.players) == sum(p["kills"] for p in meta["players"])
        for team in s.teams:
            assert [p.net_worth for p in team] == sorted((p.net_worth for p in team), reverse=True)

    def test_bulk_metadata_is_split_by_1000(self, api: respx.Router) -> None:
        def answer(request: httpx.Request) -> httpx.Response:
            ids = request.url.params["match_ids"].split(",")
            return httpx.Response(200, json=[{"match_id": int(i)} for i in ids])

        route = api.get(url__regex=r".*/v1/matches/metadata.*").mock(side_effect=answer)
        with Deadlock(retry=None) as dl:
            rows = dl.matches.get_many(list(range(1500)))
        assert len(rows) == 1500
        assert route.call_count == 2
        assert route.calls[0].request.url.params["include_info"] == "true"

    def test_active_for_one_or_many_players(self, dl: Deadlock, api: respx.Router) -> None:
        assert dl.matches.active()
        dl.matches.active(players=[SUBJECT])
        dl.matches.active(players=[SUBJECT, 1002])
        urls = [str(c.request.url) for c in api.calls]
        assert f"account_id={SUBJECT}" in urls[1]
        assert "account_ids=1001%2C1002" in urls[2]


class TestHeroesAndItems:
    def test_finds_heroes_by_id_name_and_class(self, dl: Deadlock) -> None:
        heroes = dl.heroes.list(only_active=False)
        hero = next(h for h in heroes if " " in h["name"])
        for key in (hero["id"], hero["name"].upper(), hero["class_name"]):
            found = dl.heroes.get(key)
            assert found
            assert found["id"] == hero["id"]
        assert dl.heroes.get("definitely not a hero") is None
        with pytest.raises(DeadlockError) as info:
            dl.heroes.require("nope")
        assert info.value.code == "NOT_FOUND"

    def test_hero_stats_add_up_to_12_heroes_per_match(self, dl: Deadlock) -> None:
        stats = dl.heroes.stats()
        assert 11.9 < sum(s.pick_rate for s in stats) < 12.1
        assert all(s.confidence <= s.win_rate for s in stats)

    def test_tier_list_ranked_by_confidence(self, dl: Deadlock, api: respx.Router) -> None:
        tiers = dl.heroes.tier_list(min_matches=1, min_average_badge=81)
        assert tiers[0].tier == "S"
        assert tiers[-1].tier == "D"
        assert [t.position for t in tiers] == list(range(1, len(tiers) + 1))
        assert [t.confidence for t in tiers] == sorted((t.confidence for t in tiers), reverse=True)
        stats_call = next(c for c in api.calls if c.request.url.path.endswith("hero-stats"))
        assert stats_call.request.url.params["min_average_badge"] == "81"

    def test_counters_and_synergies(self, dl: Deadlock) -> None:
        hero_id = fixture("hero-counter-stats")[0]["hero_id"]
        counters = dl.heroes.counters(hero_id, min_matches=1)
        mates = dl.heroes.synergies(hero_id, min_matches=1)
        assert len(counters) > 5
        assert all(m.hero_id != hero_id for m in [*counters, *mates])
        worst = worst_matchups(counters)
        assert worst[0].win_rate < 0.5 < counters[0].win_rate

    def test_items(self, dl: Deadlock) -> None:
        shop = dl.items.shop(tier=1)
        assert shop
        assert all(i["item_tier"] == 1 and i["shopable"] for i in shop)
        vitality = dl.items.list(type="upgrade", slot="vitality")
        assert all(i.get("item_slot_type") == "vitality" for i in vitality)
        stats = dl.items.stats(min_matches=1)
        assert stats
        assert all(s.name != str(s.item_id) for s in stats)
        upgrade = shop[0]
        found = dl.items.get(upgrade["name"].lower())
        assert found
        assert found["id"] == upgrade["id"]

    def test_search_forgives_typos(self, dl: Deadlock) -> None:
        hero: Any = dl.heroes.list()[0]
        typo = hero["name"][:-1] + ("y" if hero["name"][-1] != "y" else "x")
        hits = dl.search(typo)
        assert hits
        assert hits[0]["id"] == hero["id"]
        assert dl.search("") == []


class TestMeta:
    def test_leaderboard(self, dl: Deadlock, api: respx.Router) -> None:
        rows = dl.leaderboard.get("eu", limit=5)
        assert len(rows) == 5
        assert rows[0].rank == 1
        assert "/v1/leaderboard/Europe" in paths(api)
        with_heroes = next(r for r in rows if r.top_hero_ids)
        assert not with_heroes.top_heroes[0].startswith("Hero ")
        with pytest.raises(DeadlockError):
            dl.leaderboard.get("mars")
        found = dl.leaderboard.find("player 2", "eu")
        assert found
        assert found.rank == 2

    def test_patches(self, dl: Deadlock) -> None:
        notes = dl.patches.list()
        assert notes[0].published_at >= notes[-1].published_at
        assert notes[0].url.startswith("https://")
        latest = dl.patches.latest()
        assert latest
        assert latest.title == notes[0].title

    def test_sql(self, dl: Deadlock, api: respx.Router) -> None:
        assert dl.sql.query("SELECT 1")[0]["hero_id"] == 1
        assert api.calls.last.request.url.params["query"] == "SELECT 1"
        assert "match_player" in dl.sql.tables()
        with pytest.raises(DeadlockError):
            dl.sql.query(" ")

    def test_attribution(self) -> None:
        assert ATTRIBUTION["url"] == "https://deadlock-api.com"


def test_fixtures_hold_no_real_account_ids() -> None:
    assert {m["account_id"] for m in fixture("match-history")} == {SUBJECT}
