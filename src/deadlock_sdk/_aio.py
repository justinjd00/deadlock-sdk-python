"""Concurrency helpers for the async client. ``_sio.py`` holds the sync twins."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import Any


async def gather(*aws: Awaitable[Any]) -> list[Any]:
    """Runs awaitables concurrently and returns their results in order."""
    return list(await asyncio.gather(*aws))


async def optional(call: Callable[[], Awaitable[Any]], *codes: str) -> Any:
    """Returns ``None`` instead of raising when ``call`` fails with one of the given error codes."""
    from .errors import DeadlockError

    try:
        return await call()
    except DeadlockError as error:
        if error.code in codes:
            return None
        raise
