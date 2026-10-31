"""The async client. ``scripts/unasync.py`` turns this file into ``_sync_client.py``.

Edit this file, then run ``python scripts/unasync.py``. CI fails when the two drift.
"""

from __future__ import annotations

import builtins
from collections.abc import Callable, Mapping, Sequence
from difflib import SequenceMatcher
from types import TracebackType
from typing import Any, cast

import httpx

from . import _logic as logic
from ._aio import gather, optional
from ._cache import DEFAULT_TTL, CacheResource, CacheStore, MemoryCache, resource_for
from ._generated.api import RESPONSE_KIND, AsyncTypedGetMixin
from ._generated.schemas import (
    AccountRank,
    ActiveMatch,
    APIInfo,
    Build,
    EnemyStats,
    Hero,
    HeroStats,
    Item,
    MateStats,
    PlayerMatchHistoryEntry,
    Rank,
    SteamProfile,
    Upgrade,
)
from ._http import (
    DEFAULT_BASE_URL,
    DEFAULT_USER_AGENT,
    AsyncTransport,
    Query,
    RateLimit,
    RetryEvent,
    RetryPolicy,
)
from ._options import DEFAULT_OPTIONS, CallOptions, Language, fill_path
from .errors import DeadlockError, invalid_input
from .helpers import (
    Badge,
    PlayerInput,
    chunk,
    decode_badge,
    normalize_region,
    normalize_text,
    to_account_id,
    unique,
)
from .models import (
    HeroStat,
    ItemStat,
    LeaderboardRow,
    MatchMetadata,
    Matchup,
    PatchNote,
    PlayerRank,
    PlayerSummary,
    Scoreboard,
    TierEntry,
)

BATCH = 1000

#: Credit line for UIs. The Deadlock API asks nothing formal, but credit keeps it alive.
ATTRIBUTION = {"text": "Data from the Deadlock API", "url": "https://deadlock-api.com"}


def _ts(value: Any) -> int | None:
    """Unix seconds from a datetime, date-like or number."""
    if value is None:
        return None
    if hasattr(value, "timestamp"):
        return int(value.timestamp())
    return int(value)


class AsyncApi(AsyncTypedGetMixin):
    """Typed access to every endpoint. ``get`` autocompletes paths and checks parameters."""

    def __init__(self, client: AsyncDeadlock) -> None:
        self._client = client

    async def _request_get(self, path: str, path_params: Any, query: Any, options: Any) -> Any:
        kind = RESPONSE_KIND.get(path, "json")
        return await self._client._get(fill_path(path, path_params), query, options, kind)

    async def request(
        self,
        method: str,
        path: str,
        *,
        path_params: Mapping[str, Any] | None = None,
        query: Query | None = None,
        json: Any = None,
        options: CallOptions | None = None,
    ) -> Any:
        """Untyped escape hatch for POST and friends. Never cached."""
        o = options or DEFAULT_OPTIONS
        return await self._client._transport.request(
            method.upper(), fill_path(path, path_params), query=query, body=json, timeout=o.timeout
        )


class AsyncDeadlock:
    """Async client for the Deadlock API.

    >>> async with AsyncDeadlock() as dl:
    ...     summary = await dl.players.summary("[U:1:22202]")
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
        retry: RetryPolicy | None = RetryPolicy(),  # noqa: B008 - immutable
        throttle: bool = True,
        cache: CacheStore | bool = True,
        ttl: Mapping[CacheResource, float] | None = None,
        language: Language | None = None,
        user_agent: str | None = DEFAULT_USER_AGENT,
        headers: Mapping[str, str] | None = None,
        http_client: httpx.AsyncClient | None = None,
        on_retry: Callable[[RetryEvent], None] | None = None,
    ) -> None:
        self._transport = AsyncTransport(
            client=http_client,
            base_url=base_url,
            api_key=api_key,
            timeout=timeout,
            retry=retry,
            throttle=throttle,
            headers=headers,
            user_agent=user_agent,
            on_retry=on_retry,
        )
        self._cache: CacheStore | None = MemoryCache() if cache is True else None if cache is False else cache
        self._ttl: dict[CacheResource, float] = {**DEFAULT_TTL, **(ttl or {})}
        self.language = language

        self.api = AsyncApi(self)
        self.players = AsyncPlayers(self)
        self.matches = AsyncMatches(self)
        self.heroes = AsyncHeroes(self)
        self.items = AsyncItems(self)
        self.ranks = AsyncRanks(self)
        self.leaderboard = AsyncLeaderboard(self)
        self.builds = AsyncBuilds(self)
        self.patches = AsyncPatches(self)
        self.analytics = AsyncAnalytics(self)
        self.sql = AsyncSql(self)

    async def _get(
        self, path: str, query: Query | None, options: CallOptions | None, kind: Any = "json"
    ) -> Any:
        o = options or DEFAULT_OPTIONS
        if self._cache is None or kind == "bytes":
            return await self._transport.request("GET", path, query=query, kind=kind, timeout=o.timeout)
        key = f"{kind} {self._transport.url(path)}?{sorted((query or {}).items(), key=lambda kv: kv[0])}"
        if not o.fresh:
            hit = self._cache.get(key)
            if hit is not None:
                return hit
        value = await self._transport.request("GET", path, query=query, kind=kind, timeout=o.timeout)
        if value is not None:
            self._cache.set(key, value, self._ttl[resource_for(path)])
        return value

    def _lang(self, language: Language | None) -> dict[str, Any]:
        lang = language or self.language
        return {"language": lang} if lang else {}

    def rate_limit(self, path: str = "/v1/info") -> RateLimit | None:
        """Last rate limit state the API reported for a path."""
        return self._transport.rate_limit(path)

    def clear_cache(self) -> None:
        if self._cache is not None:
            self._cache.clear()

    async def info(self, options: CallOptions | None = None) -> APIInfo:
        """API health and table sizes."""
        return await self.api.get("/v1/info", options=options)

    async def search(
        self, text: str, *, limit: int = 10, options: CallOptions | None = None
    ) -> list[Hero | Item]:
        """Finds heroes and shop items by name, forgiving typos and spacing."""
        heroes, items = await gather(self.heroes.list(options=options), self.items.shop(options=options))
        want = normalize_text(text)
        if not want:
            return []

        def score(name: str) -> float:
            n = normalize_text(name)
            if not n:
                return 99
            if n == want:
                return 0
            if n.startswith(want):
                return 1
            if want in n:
                return 2
            # Similarity per word and for the whole name, 0.75 catches "hayz" but not "grit" for "geist".
            words = [normalize_text(w) for w in name.split()] + [n]
            best = max(SequenceMatcher(None, want, w).ratio() for w in words if w)
            return 4 - best if best >= 0.75 else 99

        ranked = sorted(
            [*((score(h["name"]), h) for h in heroes), *((score(str(i.get("name", ""))), i) for i in items)],
            key=lambda pair: pair[0],
        )
        return [entry for s, entry in ranked if s < 99][:limit]

    async def close(self) -> None:
        await self._transport.close()

    async def __aenter__(self) -> AsyncDeadlock:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        await self.close()


class _Resource:
    def __init__(self, client: AsyncDeadlock) -> None:
        self._c = client


class AsyncPlayers(_Resource):
    def resolve(self, player: PlayerInput) -> int:
        """Any Steam id format or profile URL to the account id the API uses."""
        return to_account_id(player)

    async def rank(self, player: PlayerInput, options: CallOptions | None = None) -> PlayerRank:
        """Current rank, decoded to tier, subrank, name and icon."""
        account_id = to_account_id(player)
        raw, ranks = await gather(
            self._c.api.get(
                "/v1/players/{account_id}/rank", path_params={"account_id": account_id}, options=options
            ),
            optional(lambda: self._c.ranks.list(options=options), "HTTP_ERROR", "SERVICE_BUSY"),
        )
        return logic.player_rank(account_id, raw, ranks)

    async def ranks(
        self, players: Sequence[PlayerInput], options: CallOptions | None = None
    ) -> list[PlayerRank]:
        """Ranks for many players, split into batches of 1000."""
        ids = unique(to_account_id(p) for p in players)
        ranks = await self._c.ranks.list(options=options)
        out: list[PlayerRank] = []
        for batch in chunk(ids, BATCH):
            rows: list[AccountRank] = await self._c.api.get(
                "/v1/players/rank", query={"account_ids": batch}, options=options
            )
            out += [logic.player_rank(r["account_id"], cast(Any, r), ranks) for r in rows]
        return out

    async def match_history(
        self,
        player: PlayerInput,
        *,
        limit: int | None = None,
        since: Any = None,
        match_modes: Sequence[int] | None = None,
        hero_id: int | None = None,
        force_refetch: bool = False,
        options: CallOptions | None = None,
    ) -> list[PlayerMatchHistoryEntry]:
        """Match history, newest first. ``since`` takes a datetime or unix seconds, ``match_modes=[4]`` is ranked.

        ``force_refetch`` asks the API to reload from Steam. It is strictly rate limited, use it sparingly.
        """
        rows = await self._c.api.get(
            "/v1/players/{account_id}/match-history",
            path_params={"account_id": to_account_id(player)},
            query={"force_refetch": True} if force_refetch else None,
            options=options,
        )
        return logic.filter_history(
            rows, limit=limit, since=_ts(since), match_modes=match_modes, hero_id=hero_id
        )

    async def summary(
        self, player: PlayerInput, *, matches: int = 50, options: CallOptions | None = None
    ) -> PlayerSummary:
        """Profile, rank, recent form and top heroes in one call. Private parts come back as ``None``."""
        account_id = to_account_id(player)
        tolerated = ("FORBIDDEN", "NOT_FOUND", "BAD_REQUEST")
        history, rank, profiles, heroes = await gather(
            self.match_history(account_id, limit=matches, options=options),
            optional(lambda: self.rank(account_id, options), *tolerated),
            optional(lambda: self.profiles([account_id], options=options), *tolerated),
            self._c.heroes.list(only_active=False, options=options),
        )
        return logic.player_summary(account_id, history, rank, (profiles or [None])[0], heroes)

    async def hero_stats(
        self, players: PlayerInput | Sequence[PlayerInput], options: CallOptions | None = None
    ) -> list[HeroStats]:
        """Per hero totals for one or more players."""
        items = [players] if isinstance(players, (int, str)) else list(players)
        ids = unique(to_account_id(p) for p in items)
        out: list[HeroStats] = []
        for batch in chunk(ids, BATCH):
            out += await self._c.api.get(
                "/v1/players/hero-stats", query={"account_ids": batch}, options=options
            )
        return out

    async def enemy_stats(self, player: PlayerInput, options: CallOptions | None = None) -> list[EnemyStats]:
        """Who this player faced most, and how it went."""
        return await self._c.api.get(
            "/v1/players/{account_id}/enemy-stats",
            path_params={"account_id": to_account_id(player)},
            options=options,
        )

    async def mate_stats(self, player: PlayerInput, options: CallOptions | None = None) -> list[MateStats]:
        """Who this player queued with most, and how it went."""
        return await self._c.api.get(
            "/v1/players/{account_id}/mate-stats",
            path_params={"account_id": to_account_id(player)},
            options=options,
        )

    async def search(
        self, name: str, *, limit: int = 10, options: CallOptions | None = None
    ) -> list[SteamProfile]:
        """Players by Steam name."""
        if not name.strip():
            raise invalid_input("Search text must not be empty")
        return await self._c.api.get(
            "/v1/players/steam-search", query={"search_query": name, "limit": limit}, options=options
        )

    async def profiles(
        self, players: Sequence[PlayerInput], *, refresh: bool = False, options: CallOptions | None = None
    ) -> list[SteamProfile]:
        """Steam profiles (name, avatar, country) in batches of 1000."""
        ids = unique(to_account_id(p) for p in players)
        out: list[SteamProfile] = []
        for batch in chunk(ids, BATCH):
            query: dict[str, Any] = {"account_ids": batch, **({"refresh": True} if refresh else {})}
            out += await self._c.api.get("/v1/players/steam", query=cast(Any, query), options=options)
        return out


class AsyncMatches(_Resource):
    async def get(self, match_id: int, options: CallOptions | None = None) -> MatchMetadata:
        """Full metadata of a finished match: item timeline, stat snapshots, objectives."""
        raw = await self._c.api.get(
            "/v1/matches/{match_id}/metadata", path_params={"match_id": match_id}, options=options
        )
        return cast(MatchMetadata, raw)

    async def get_many(
        self, match_ids: Sequence[int], *, options: CallOptions | None = None, **query: Any
    ) -> list[dict[str, Any]]:
        """Bulk metadata, split into requests of 1000. Pick parts with ``include_player_info=True`` and friends."""
        ids = unique(match_ids)
        out: list[dict[str, Any]] = []
        for batch in chunk(ids, BATCH):
            q = {"include_info": True, **query, "match_ids": batch, "limit": len(batch)}
            out += await self._c.api.get("/v1/matches/metadata", query=cast(Any, q), options=options)
        return out

    async def active(
        self, *, players: Sequence[PlayerInput] | None = None, options: CallOptions | None = None
    ) -> list[ActiveMatch]:
        """Top matches being played right now, optionally only those with the given players."""
        ids = [to_account_id(p) for p in players or []]
        query: Any = {"account_id": ids[0]} if len(ids) == 1 else {"account_ids": ids} if ids else None
        return await self._c.api.get("/v1/matches/active", query=query, options=options)

    async def scoreboard(self, match_id: int, options: CallOptions | None = None) -> Scoreboard:
        """Both teams with hero and item names, KDA, souls and damage."""
        meta, heroes, items = await gather(
            self.get(match_id, options),
            self._c.heroes.list(only_active=False, options=options),
            self._c.items.list(options=options),
        )
        return logic.scoreboard(meta, heroes, items)


class AsyncHeroes(_Resource):
    async def list(
        self,
        *,
        only_active: bool = True,
        language: Language | None = None,
        options: CallOptions | None = None,
    ) -> builtins.list[Hero]:
        """Heroes, only playable ones by default."""
        query: Any = {**self._c._lang(language), "only_active": only_active}
        return await self._c.api.get("/v1/assets/heroes", query=query, options=options)

    async def get(self, hero: int | str, options: CallOptions | None = None) -> Hero | None:
        """By id, name (``"lady geist"``) or class name (``"hero_haze"``)."""
        return logic.find_hero(await self.list(only_active=False, options=options), hero)

    async def require(self, hero: int | str, options: CallOptions | None = None) -> Hero:
        """Like ``get`` but raises ``NOT_FOUND``."""
        return logic.require_hero(await self.list(only_active=False, options=options), hero)

    async def stats(self, options: CallOptions | None = None, **query: Any) -> builtins.list[HeroStat]:
        """Win rate, pick rate, KDA, souls, damage and confidence per hero.

        Filters are the API's own, e.g. ``min_average_badge=81, min_unix_timestamp=...``.
        """
        rows, heroes = await gather(
            self._c.api.get("/v1/analytics/hero-stats", query=cast(Any, query), options=options),
            self.list(only_active=False, options=options),
        )
        return logic.hero_stats(rows, heroes)

    async def tier_list(
        self, *, min_matches: int = 100, options: CallOptions | None = None, **query: Any
    ) -> builtins.list[TierEntry]:
        """S to D, ranked by the Wilson lower bound so small samples cannot top the list."""
        return logic.tier_list(await self.stats(options, **query), min_matches)

    async def counters(
        self, hero: int | str, *, min_matches: int = 50, options: CallOptions | None = None, **query: Any
    ) -> builtins.list[Matchup]:
        """Matchups against every enemy, best first. ``reversed()`` or ``worst_matchups()`` for the bad ones."""
        target, heroes, rows = await gather(
            self.require(hero, options),
            self.list(only_active=False, options=options),
            self._c.api.get("/v1/analytics/hero-counter-stats", query=cast(Any, query), options=options),
        )
        return logic.counters(rows, target, heroes, min_matches)

    async def synergies(
        self, hero: int | str, *, min_matches: int = 50, options: CallOptions | None = None, **query: Any
    ) -> builtins.list[Matchup]:
        """Best teammates, by confidence adjusted win rate together."""
        target, heroes, rows = await gather(
            self.require(hero, options),
            self.list(only_active=False, options=options),
            self._c.api.get("/v1/analytics/hero-synergy-stats", query=cast(Any, query), options=options),
        )
        return logic.synergies(rows, target, heroes, min_matches)


class AsyncItems(_Resource):
    async def list(
        self,
        *,
        type: str | None = None,
        slot: str | None = None,
        tier: int | None = None,
        shopable: bool | None = None,
        language: Language | None = None,
        options: CallOptions | None = None,
    ) -> builtins.list[Item]:
        """All items, filtered locally so one cached request serves every filter."""
        items = await self._c.api.get(
            "/v1/assets/items", query=cast(Any, self._c._lang(language)) or None, options=options
        )
        return logic.filter_items(items, type=type, slot=slot, tier=tier, shopable=shopable)

    async def shop(
        self, *, slot: str | None = None, tier: int | None = None, options: CallOptions | None = None
    ) -> builtins.list[Upgrade]:
        """Buyable upgrades, optionally one shop column (``"weapon"``, ``"vitality"``, ``"spirit"``) and tier."""
        items = await self.list(type="upgrade", slot=slot, tier=tier, shopable=True, options=options)
        return cast("builtins.list[Upgrade]", items)

    async def get(self, item: int | str, options: CallOptions | None = None) -> Item | None:
        """By id, class name or display name. Prefers the buyable upgrade when names clash."""
        items = await self.list(options=options)
        if isinstance(item, int) or str(item).isdigit():
            return next((i for i in items if i["id"] == int(item)), None)
        by_class = next((i for i in items if i["class_name"] == item), None)
        if by_class:
            return by_class
        want = normalize_text(str(item))
        hits = [i for i in items if normalize_text(str(i.get("name") or "")) == want]
        shop = [i for i in hits if i.get("type") == "upgrade" and i.get("shopable")]
        return (shop or hits)[0] if (shop or hits) else None

    async def stats(
        self, *, min_matches: int = 100, options: CallOptions | None = None, **query: Any
    ) -> builtins.list[ItemStat]:
        """Win rate and average buy time per item, with names, best first."""
        rows, items = await gather(
            self._c.api.get("/v1/analytics/item-stats", query=cast(Any, query), options=options),
            self.list(options=options),
        )
        return logic.item_stats(rows, items, min_matches)


class AsyncRanks(_Resource):
    async def list(
        self, *, language: Language | None = None, options: CallOptions | None = None
    ) -> builtins.list[Rank]:
        """All rank tiers with names, colors and icons."""
        return await self._c.api.get(
            "/v1/assets/ranks", query=cast(Any, self._c._lang(language)) or None, options=options
        )

    async def decode(self, badge: int, options: CallOptions | None = None) -> Badge:
        """``115`` to Eternus 5 with the live icon."""
        return decode_badge(badge, cast(Any, await self.list(options=options)))


class AsyncLeaderboard(_Resource):
    async def get(
        self,
        region: str = "Europe",
        *,
        hero: int | str | None = None,
        limit: int | None = None,
        options: CallOptions | None = None,
    ) -> list[LeaderboardRow]:
        """A region's leaderboard (``"eu"``, ``"na"``, ``"Europe"``, ...), optionally for one hero."""
        r = normalize_region(region)
        if hero is None:
            board, heroes = await gather(
                self._c.api.get("/v1/leaderboard/{region}", path_params={"region": r}, options=options),
                self._c.heroes.list(only_active=False, options=options),
            )
        else:
            target = await self._c.heroes.require(hero, options)
            board, heroes = await gather(
                self._c.api.get(
                    "/v1/leaderboard/{region}/{hero_id}",
                    path_params={"region": r, "hero_id": target["id"]},
                    options=options,
                ),
                self._c.heroes.list(only_active=False, options=options),
            )
        rows = logic.leaderboard(board["entries"], heroes)
        return rows[:limit] if limit is not None else rows

    async def find(
        self, player: str | int, region: str = "Europe", *, options: CallOptions | None = None
    ) -> LeaderboardRow | None:
        """A player on a leaderboard by name or account id."""
        rows = await self.get(region, options=options)
        as_id = int(player) if isinstance(player, int) or str(player).isdigit() else None
        want = normalize_text(str(player))
        return next(
            (
                r
                for r in rows
                if (as_id is not None and as_id in r.account_ids) or normalize_text(r.name) == want
            ),
            None,
        )


class AsyncBuilds(_Resource):
    async def search(self, options: CallOptions | None = None, **query: Any) -> list[Build]:
        """Community builds. All API filters work: ``hero_id``, ``sort_by``, ``search_name``, ``language``."""
        return await self._c.api.get("/v1/builds", query=cast(Any, query) or None, options=options)

    async def for_hero(
        self,
        hero: int | str,
        *,
        limit: int = 10,
        sort_by: str = "weekly_favorites",
        options: CallOptions | None = None,
    ) -> list[Build]:
        """Most favorited current builds for a hero."""
        target = await self._c.heroes.require(hero, options)
        return await self.search(
            options, hero_id=target["id"], only_latest=True, sort_by=sort_by, limit=limit
        )

    async def by_author(self, player: PlayerInput, options: CallOptions | None = None) -> list[Build]:
        return await self._c.api.get(
            "/v1/builds/by-author/{account_id}",
            path_params={"account_id": to_account_id(player)},
            options=options,
        )


class AsyncPatches(_Resource):
    async def list(self, options: CallOptions | None = None) -> builtins.list[PatchNote]:
        """Patch notes, newest first."""
        return logic.patch_notes(await self._c.api.get("/v1/patches", options=options))

    async def latest(self, options: CallOptions | None = None) -> PatchNote | None:
        notes = await self.list(options)
        return notes[0] if notes else None


class AsyncAnalytics(_Resource):
    async def get(self, name: str, options: CallOptions | None = None, **query: Any) -> Any:
        """Any analytics endpoint by short name, e.g. ``"item-permutation-stats"``.

        For full typing use ``dl.api.get("/v1/analytics/...")``.
        """
        path = f"/v1/analytics/{name.strip('/')}"
        if "{" in path:
            raise invalid_input("Use dl.api.get for analytics endpoints with path parameters")
        return await self._c._get(path, query or None, options)


class AsyncSql(_Resource):
    async def query(self, sql: str, options: CallOptions | None = None) -> list[dict[str, Any]]:
        """Read only SQL (DuckDB syntax) over the public dataset. The timeout defaults to 120s."""
        import json

        if not sql.strip():
            raise invalid_input("SQL query must not be empty")
        o = options or CallOptions(timeout=120)
        if o.timeout is None:
            o = CallOptions(fresh=o.fresh, timeout=120)
        text = await self._c.api.get("/v1/sql", query={"query": sql, "format": "json"}, options=o)
        try:
            rows = json.loads(text)
        except ValueError as exc:
            raise DeadlockError(
                "SQL endpoint did not return JSON", code="INVALID_RESPONSE", body=text[:500]
            ) from exc
        return rows if isinstance(rows, list) else [rows]

    async def tables(self, options: CallOptions | None = None) -> list[str]:
        return await self._c.api.get("/v1/sql/tables", options=options)

    async def schema(self, table: str, options: CallOptions | None = None) -> list[dict[str, str]]:
        """Columns of a table. The spec says map, the API returns a list, both are handled."""
        raw: Any = await self._c.api.get(
            "/v1/sql/tables/{table}/schema", path_params={"table": table}, options=options
        )
        if isinstance(raw, list):
            return raw
        return [{"name": k, "type": v} for k, v in raw.items()]
