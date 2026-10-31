"""The async client is generated into the sync one, these make sure both really behave the same."""

from __future__ import annotations

import asyncio
import subprocess
import sys
from pathlib import Path

import respx

from deadlock_sdk import AsyncDeadlock, Deadlock

from .conftest import MATCH_ID, SUBJECT


async def test_summary_runs_requests_concurrently(adl: AsyncDeadlock, api: respx.Router) -> None:
    s = await adl.players.summary(SUBJECT)
    assert s.account_id == SUBJECT
    assert s.rank is not None
    called = [c.request.url.path for c in api.calls]
    # One request per endpoint, even though rank and summary both need the rank assets.
    assert len(called) == len(set(called))


async def test_async_and_sync_agree(adl: AsyncDeadlock, dl: Deadlock) -> None:
    a_board, a_tiers, a_lb = await asyncio.gather(
        adl.matches.scoreboard(MATCH_ID), adl.heroes.tier_list(min_matches=1), adl.leaderboard.get("eu")
    )
    assert a_board == dl.matches.scoreboard(MATCH_ID)
    assert a_tiers == dl.heroes.tier_list(min_matches=1)
    assert a_lb == dl.leaderboard.get("eu")


async def test_async_context_manager(api: respx.Router) -> None:
    async with AsyncDeadlock(retry=None) as dl:
        assert (await dl.patches.latest()) is not None


def test_generated_sync_client_is_up_to_date() -> None:
    root = Path(__file__).resolve().parent.parent
    done = subprocess.run(
        [sys.executable, str(root / "scripts" / "unasync.py"), "--check"], capture_output=True, text=True
    )
    assert done.returncode == 0, done.stdout + done.stderr
