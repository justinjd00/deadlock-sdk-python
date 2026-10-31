"""Shared test setup: a fake Deadlock API answering from anonymized real responses."""

from __future__ import annotations

import json
import re
from collections.abc import Iterator
from functools import cache
from pathlib import Path
from typing import Any

import httpx
import pytest
import respx

from deadlock_sdk import AsyncDeadlock, Deadlock

FIXTURES = Path(__file__).parent / "fixtures"
BASE = "https://api.deadlock-api.com"
SUBJECT = 1001


@cache
def _load(name: str) -> str:
    return (FIXTURES / f"{name}.json").read_text()


def fixture(name: str) -> Any:
    return json.loads(_load(name))


MATCH_ID: int = fixture("match-metadata")["match_info"]["match_id"]


def _heroes(request: httpx.Request) -> httpx.Response:
    heroes = fixture("heroes")
    if request.url.params.get("only_active") == "true":
        heroes = [h for h in heroes if h["player_selectable"] and not h["disabled"]]
    return httpx.Response(200, json=heroes)


def _ranks_batch(request: httpx.Request) -> httpx.Response:
    ids = request.url.params["account_ids"].split(",")
    return httpx.Response(200, json=[{"account_id": int(i), "badge": 81} for i in ids])


ROUTES: list[tuple[str, Any]] = [
    (r"/v1/assets/heroes", _heroes),
    (r"/v1/assets/items", "items"),
    (r"/v1/assets/ranks", "ranks"),
    (r"/v1/analytics/hero-stats", "hero-stats"),
    (r"/v1/analytics/hero-counter-stats", "hero-counter-stats"),
    (r"/v1/analytics/hero-synergy-stats", "hero-synergy-stats"),
    (r"/v1/analytics/item-stats", "item-stats"),
    (r"/v1/matches/\d+/metadata", "match-metadata"),
    (r"/v1/matches/active", "active"),
    (r"/v1/players/\d+/match-history", "match-history"),
    (r"/v1/players/\d+/rank", "rank"),
    (r"/v1/players/rank", _ranks_batch),
    (r"/v1/players/steam", "steam"),
    (r"/v1/players/steam-search", "steam"),
    (r"/v1/leaderboard/[A-Za-z]+(/\d+)?", "leaderboard"),
    (r"/v1/patches", "patches"),
    (r"/v1/sql/tables", ["match_info", "match_player"]),
    (r"/v1/sql", "SQL"),
]


def _install(router: respx.Router) -> None:
    for pattern, answer in ROUTES:
        route = router.get(url__regex=rf"^{re.escape(BASE)}{pattern}(\?.*)?$", name=pattern)
        if callable(answer):
            route.mock(side_effect=answer)
        elif answer == "SQL":
            route.mock(return_value=httpx.Response(200, text='[{"hero_id": 1, "games": 10}]'))
        elif isinstance(answer, str):
            route.mock(
                return_value=httpx.Response(
                    200, content=_load(answer), headers={"content-type": "application/json"}
                )
            )
        else:
            route.mock(return_value=httpx.Response(200, json=answer))


@pytest.fixture
def api() -> Iterator[respx.Router]:
    """The fake API. Unknown paths fail the test instead of reaching the network."""
    with respx.mock(assert_all_called=False, assert_all_mocked=True) as router:
        _install(router)
        yield router


@pytest.fixture
def dl(api: respx.Router) -> Iterator[Deadlock]:
    client = Deadlock(retry=None, throttle=False, user_agent=None)
    yield client
    client.close()


@pytest.fixture
async def adl(api: respx.Router) -> Any:
    client = AsyncDeadlock(retry=None, throttle=False, user_agent=None)
    yield client
    await client.close()


def paths(router: respx.Router) -> list[str]:
    return [call.request.url.path for call in router.calls]
