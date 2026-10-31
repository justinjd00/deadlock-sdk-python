"""Results the SDK computes on top of raw responses.

Raw endpoint responses are ``TypedDict`` (see ``deadlock_sdk.types``). Everything
the SDK derives is a frozen dataclass with attribute access, so editors complete
``summary.rank.label`` and ``to_dataframe()`` can flatten it.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any, Literal, TypedDict

from typing_extensions import NotRequired

from ._generated.schemas import (
    AnalyticsHeroStats,
    ItemStats,
    LeaderboardEntry,
    Patch,
    RankResponse,
    SteamProfile,
)
from .helpers import Badge

Tier = Literal["S", "A", "B", "C", "D"]


class _AsDict:
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)  # type: ignore[call-overload, no-any-return]


@dataclass(frozen=True)
class PlayerRank(Badge, _AsDict):
    account_id: int = 0
    raw: RankResponse | None = field(default=None, repr=False)


@dataclass(frozen=True)
class Streak(_AsDict):
    kind: Literal["win", "loss", "none"]
    count: int


@dataclass(frozen=True)
class HeroSummary(_AsDict):
    hero_id: int
    matches: int
    wins: int
    win_rate: float
    kda: float
    avg_net_worth: int
    #: Filled in by ``players.summary``.
    name: str = ""


@dataclass(frozen=True)
class HistorySummary(_AsDict):
    matches: int
    wins: int
    losses: int
    win_rate: float
    kills: int
    deaths: int
    assists: int
    kda: float
    avg_net_worth: int
    avg_last_hits: float
    avg_duration_s: int
    streak: Streak
    #: Sum of rank progress from ranked matches in this window.
    ranked_delta: int
    #: Most played first.
    heroes: list[HeroSummary]
    first_match_at: datetime | None
    last_match_at: datetime | None


@dataclass(frozen=True)
class PlayerSummary(_AsDict):
    account_id: int
    steam_id64: str
    #: ``None`` when Steam has no public profile cached.
    profile: SteamProfile | None
    #: ``None`` for unranked or private players.
    rank: PlayerRank | None
    recent: HistorySummary
    top_heroes: list[HeroSummary]


@dataclass(frozen=True)
class HeroStat(_AsDict):
    hero_id: int
    name: str
    matches: int
    wins: int
    win_rate: float
    #: Share of all matches that had this hero, 0..1.
    pick_rate: float
    kda: float
    avg_net_worth: int
    avg_player_damage: int
    #: Win rate lower bound at 95% confidence, used for ranking.
    confidence: float
    raw: AnalyticsHeroStats = field(repr=False)


@dataclass(frozen=True)
class TierEntry(HeroStat):
    tier: Tier = "B"
    #: 1 is best.
    position: int = 0


@dataclass(frozen=True)
class Matchup(_AsDict):
    hero_id: int
    name: str
    matches: int
    wins: int
    #: From the perspective of the hero you asked about.
    win_rate: float
    confidence: float


@dataclass(frozen=True)
class ItemStat(_AsDict):
    item_id: int
    name: str
    slot: str | None
    tier: int | None
    matches: int
    wins: int
    win_rate: float
    confidence: float
    avg_buy_time_s: int
    raw: ItemStats = field(repr=False)


@dataclass(frozen=True)
class ScoreboardPlayer(_AsDict):
    account_id: int
    hero_id: int
    hero_name: str
    team: int
    won: bool
    kills: int
    deaths: int
    assists: int
    kda: float
    net_worth: int
    last_hits: int
    denies: int
    level: int
    #: Damage dealt to players, from the last stat snapshot.
    player_damage: int | None
    #: Upgrades still held at the end, in purchase order.
    final_items: list[str]
    abandoned: bool


@dataclass(frozen=True)
class Scoreboard(_AsDict):
    match_id: int
    started_at: datetime
    duration_s: int
    winning_team: int
    game_mode: int
    match_mode: int
    #: Team 0 (Hidden King) and team 1 (Archmother), richest first.
    teams: tuple[list[ScoreboardPlayer], list[ScoreboardPlayer]]

    @property
    def winners(self) -> list[ScoreboardPlayer]:
        return self.teams[self.winning_team] if self.winning_team in (0, 1) else []

    @property
    def players(self) -> list[ScoreboardPlayer]:
        return [*self.teams[0], *self.teams[1]]


@dataclass(frozen=True)
class LeaderboardRow(_AsDict):
    rank: int
    name: str
    #: Leaderboards are keyed by name, so more than one account can match.
    account_ids: list[int]
    top_hero_ids: list[int]
    top_heroes: list[str]
    raw: LeaderboardEntry = field(repr=False)


@dataclass(frozen=True)
class PatchNote(_AsDict):
    title: str
    url: str
    published_at: datetime
    #: HTML body of the patch notes.
    html: str
    raw: Patch = field(repr=False)


# The match metadata endpoint is untyped in the spec. These cover what the SDK
# reads and stay open (TypedDict ignores unknown keys).


class MatchItemEvent(TypedDict):
    item_id: int
    game_time_s: int
    sold_time_s: NotRequired[int]
    upgrade_id: NotRequired[int]


class MatchStatSnapshot(TypedDict, total=False):
    time_stamp_s: int
    net_worth: int
    player_damage: int
    player_healing: int
    kills: int
    deaths: int
    assists: int


class MatchPlayer(TypedDict):
    account_id: int
    player_slot: int
    team: int
    hero_id: int
    kills: int
    deaths: int
    assists: int
    net_worth: int
    last_hits: int
    denies: int
    level: int
    items: NotRequired[list[MatchItemEvent]]
    stats: NotRequired[list[MatchStatSnapshot]]
    abandon_match_time_s: NotRequired[int]


class MatchInfo(TypedDict):
    match_id: int
    start_time: int
    duration_s: int
    winning_team: int
    game_mode: int
    match_mode: int
    players: list[MatchPlayer]
    average_badge_team0: NotRequired[int]
    average_badge_team1: NotRequired[int]


class MatchMetadata(TypedDict):
    match_info: MatchInfo
