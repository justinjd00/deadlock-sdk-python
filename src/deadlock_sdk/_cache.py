"""A small TTL + LRU cache with per resource lifetimes."""

from __future__ import annotations

import time
from collections import OrderedDict
from dataclasses import dataclass, field
from typing import Any, Literal, Protocol

CacheResource = Literal[
    "assets", "analytics", "players", "matches", "live", "leaderboard", "builds", "patches", "other"
]

#: Seconds each kind of data stays fresh. Finished matches never change, live data does every few seconds.
DEFAULT_TTL: dict[CacheResource, float] = {
    "assets": 3600,
    "analytics": 1800,
    "players": 120,
    "matches": 86400,
    "live": 20,
    "leaderboard": 600,
    "builds": 900,
    "patches": 3600,
    "other": 300,
}


def resource_for(path: str) -> CacheResource:
    if path.startswith(("/v1/assets", "/v2/assets")):
        return "assets"
    if path.startswith("/v1/matches/active"):
        return "live"
    if path.startswith("/v1/matches"):
        return "matches"
    if path.startswith("/v1/analytics"):
        return "analytics"
    if path.startswith("/v1/players"):
        return "players"
    if path.startswith("/v1/leaderboard"):
        return "leaderboard"
    if path.startswith("/v1/builds"):
        return "builds"
    if "/patches" in path:
        return "patches"
    return "other"


class CacheStore(Protocol):
    """Anything with get/set/clear works, e.g. a thin wrapper around Redis."""

    def get(self, key: str) -> Any | None: ...
    def set(self, key: str, value: Any, ttl: float) -> None: ...
    def clear(self) -> None: ...


@dataclass
class MemoryCache:
    """In-process LRU cache. Thread safe enough for the GIL, not shared between processes."""

    max_entries: int = 500
    _data: OrderedDict[str, tuple[float, Any]] = field(default_factory=OrderedDict, repr=False)

    def get(self, key: str) -> Any | None:
        entry = self._data.get(key)
        if entry is None:
            return None
        expires, value = entry
        if time.monotonic() >= expires:
            self._data.pop(key, None)
            return None
        self._data.move_to_end(key)
        return value

    def set(self, key: str, value: Any, ttl: float) -> None:
        self._data[key] = (time.monotonic() + ttl, value)
        self._data.move_to_end(key)
        while len(self._data) > self.max_entries:
            self._data.popitem(last=False)

    def clear(self) -> None:
        self._data.clear()

    def __len__(self) -> int:
        return len(self._data)
