"""Generated from https://api.deadlock-api.com/openapi.json by scripts/generate.py. Do not edit by hand."""

# ruff: noqa
# fmt: off
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal, TypedDict, overload

from typing_extensions import NotRequired, TypeAlias

from .schemas import *  # noqa: F403

if TYPE_CHECKING:
    from .._options import CallOptions


GetPath: TypeAlias = Literal["/v1/analytics/ability-max-first-stats", "/v1/analytics/ability-order-stats", "/v1/analytics/ability-order-tree", "/v1/analytics/badge-distribution", "/v1/analytics/buff-stats", "/v1/analytics/build-item-stats", "/v1/analytics/game-stats", "/v1/analytics/hero-ban-stats", "/v1/analytics/hero-build-stats/{hero_id}", "/v1/analytics/hero-comb-stats", "/v1/analytics/hero-counter-stats", "/v1/analytics/hero-stats", "/v1/analytics/hero-swap-stats", "/v1/analytics/hero-synergy-stats", "/v1/analytics/item-flow-stats", "/v1/analytics/item-permutation-stats", "/v1/analytics/item-stats", "/v1/analytics/kill-death-stats", "/v1/analytics/lane-matchup-stats", "/v1/analytics/lane-soul-curve", "/v1/analytics/player-performance-curve", "/v1/analytics/player-stats/metrics", "/v1/analytics/scoreboards/heroes", "/v1/analytics/scoreboards/players", "/v1/assets/accolades", "/v1/assets/accolades/by-name/{name}", "/v1/assets/accolades/{accolade_id}", "/v1/assets/build-tags", "/v1/assets/build-tags/by-name/{name}", "/v1/assets/build-tags/{build_tag_id}", "/v1/assets/client-versions", "/v1/assets/colors", "/v1/assets/convars", "/v1/assets/convars/{name}", "/v1/assets/fonts", "/v1/assets/generic-data", "/v1/assets/heroes", "/v1/assets/heroes/by-name/{name}", "/v1/assets/heroes/{hero_id}", "/v1/assets/icons", "/v1/assets/images", "/v1/assets/items", "/v1/assets/items/by-hero-id/{id}", "/v1/assets/items/by-slot-type/{slot_type}", "/v1/assets/items/by-type/{type}", "/v1/assets/items/{id_or_class_name}", "/v1/assets/loot-tables", "/v1/assets/map", "/v1/assets/misc-entities", "/v1/assets/misc-entities/{id_or_classname}", "/v1/assets/models", "/v1/assets/modifiers", "/v1/assets/modifiers/{id_or_classname}", "/v1/assets/npc-units", "/v1/assets/npc-units/{id_or_classname}", "/v1/assets/ranked-seasons", "/v1/assets/ranks", "/v1/assets/ranks/{tier}", "/v1/assets/ranks/{tier}/{subrank}/image", "/v1/assets/sounds", "/v1/assets/steam-info", "/v1/assets/steam-info/all", "/v1/builds", "/v1/builds/by-author/{account_id}", "/v1/builds/{hero_id}/{build_id}", "/v1/commands/resolve", "/v1/commands/variables/available", "/v1/commands/variables/resolve", "/v1/commands/widgets/versions", "/v1/crosshair/code/image", "/v1/crosshair/code/settings", "/v1/crosshair/settings/code", "/v1/crosshair/settings/image", "/v1/graphql", "/v1/info", "/v1/info/health", "/v1/leaderboard/{region}", "/v1/leaderboard/{region}/raw", "/v1/leaderboard/{region}/{hero_id}", "/v1/leaderboard/{region}/{hero_id}/raw", "/v1/matches/active", "/v1/matches/active/raw", "/v1/matches/custom/{party_id}/match-id", "/v1/matches/demo/live/query", "/v1/matches/demo/query/{job_id}", "/v1/matches/demo/schema", "/v1/matches/live/urls", "/v1/matches/metadata", "/v1/matches/recently-fetched", "/v1/matches/{match_id}/live/url", "/v1/matches/{match_id}/metadata", "/v1/matches/{match_id}/metadata/raw", "/v1/matches/{match_id}/salts", "/v1/patches", "/v1/patches/big-days", "/v1/patron/steam-accounts", "/v1/patron/steam-accounts/{account_id}/bot-friend", "/v1/players/hero-stats", "/v1/players/mmr", "/v1/players/mmr/distribution", "/v1/players/mmr/distribution/{hero_id}", "/v1/players/mmr/{hero_id}", "/v1/players/rank", "/v1/players/rank-predict/image", "/v1/players/rank/distribution", "/v1/players/rank/image", "/v1/players/steam", "/v1/players/steam-search", "/v1/players/{account_id}/enemy-stats", "/v1/players/{account_id}/ingest-status", "/v1/players/{account_id}/match-history", "/v1/players/{account_id}/mate-stats", "/v1/players/{account_id}/mmr-history", "/v1/players/{account_id}/mmr-history/{hero_id}", "/v1/players/{account_id}/rank", "/v1/players/{account_id}/rank-predict", "/v1/players/{account_id}/rank-predict/image", "/v1/players/{account_id}/rank/image", "/v1/sql", "/v1/sql/tables", "/v1/sql/tables/{table}/schema", "/v2/patches"]

RESPONSE_KIND: dict[str, str] = {
    "/v1/assets/ranks/{tier}/{subrank}/image": "bytes",
    "/v1/commands/resolve": "text",
    "/v1/crosshair/code/image": "bytes",
    "/v1/crosshair/settings/image": "bytes",
    "/v1/graphql": "text",
    "/v1/leaderboard/{region}/raw": "bytes",
    "/v1/leaderboard/{region}/{hero_id}/raw": "bytes",
    "/v1/matches/active/raw": "bytes",
    "/v1/matches/demo/live/query": "text",
    "/v1/matches/{match_id}/metadata/raw": "bytes",
    "/v1/players/rank-predict/image": "bytes",
    "/v1/players/rank/image": "bytes",
    "/v1/players/{account_id}/rank-predict/image": "bytes",
    "/v1/players/{account_id}/rank/image": "bytes",
    "/v1/sql": "text",
}


class AbilityMaxFirstStatsGetQuery(TypedDict):
    hero_id: int
    """See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_ability_upgrades: NotRequired[int | None]
    """Filter players based on their minimum number of ability upgrades over the whole match."""
    max_ability_upgrades: NotRequired[int | None]
    """Filter players based on their maximum number of ability upgrades over the whole match."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    min_matches: NotRequired[int | None]
    """The minimum number of matches played for an ability order (on `/ability-order-tree`: an order prefix, on `/ability-max-first-stats`: an ability) to be included in the response."""
    account_id: NotRequired[int | None]
    """Filter for matches with a specific player account ID."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""
    hero_build_id: NotRequired[int | None]
    """Only players who started the match with this hero build selected. Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}>"""
    include_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    exclude_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    ability_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats>"""
    ability_unlock_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""


class AbilityOrderStatsGetQuery(TypedDict):
    hero_id: int
    """See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_ability_upgrades: NotRequired[int | None]
    """Filter players based on their minimum number of ability upgrades over the whole match."""
    max_ability_upgrades: NotRequired[int | None]
    """Filter players based on their maximum number of ability upgrades over the whole match."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    min_matches: NotRequired[int | None]
    """The minimum number of matches played for an ability order (on `/ability-order-tree`: an order prefix, on `/ability-max-first-stats`: an ability) to be included in the response."""
    account_id: NotRequired[int | None]
    """Filter for matches with a specific player account ID."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""
    hero_build_id: NotRequired[int | None]
    """Only players who started the match with this hero build selected. Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}>"""
    include_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    exclude_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    ability_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats>"""
    ability_unlock_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""


class AbilityOrderTreeGetQuery(TypedDict):
    hero_id: int
    """See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_ability_upgrades: NotRequired[int | None]
    """Filter players based on their minimum number of ability upgrades over the whole match."""
    max_ability_upgrades: NotRequired[int | None]
    """Filter players based on their maximum number of ability upgrades over the whole match."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    min_matches: NotRequired[int | None]
    """The minimum number of matches played for an ability order (on `/ability-order-tree`: an order prefix, on `/ability-max-first-stats`: an ability) to be included in the response."""
    account_id: NotRequired[int | None]
    """Filter for matches with a specific player account ID."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""
    hero_build_id: NotRequired[int | None]
    """Only players who started the match with this hero build selected. Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}>"""
    include_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    exclude_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    ability_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats>"""
    ability_unlock_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""


class BadgeDistributionGetQuery(TypedDict):
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). Values below the start of the first ranked season (1785430800) are clamped to it. **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    is_high_skill_range_parties: NotRequired[bool | None]
    """Filter matches based on whether they are in the high skill range."""
    is_low_pri_pool: NotRequired[bool | None]
    """Filter matches based on whether they are in the low priority pool."""
    is_new_player_pool: NotRequired[bool | None]
    """Filter matches based on whether they are in the new player pool."""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""


class BuffStatsGetQuery(TypedDict):
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    hero_ids: NotRequired[list[int] | None]
    """Comma separated list of hero ids to include. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""


class BuildItemStatsGetQuery(TypedDict):
    hero_id: NotRequired[int | None]
    """Filter builds based on the hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    min_last_updated_unix_timestamp: NotRequired[int | None]
    """Filter builds based on their last updated time (Unix timestamp). **Default:** 30 days ago."""
    max_last_updated_unix_timestamp: NotRequired[int | None]
    """Filter builds based on their last updated time (Unix timestamp)."""


class GameStatsGetQuery(TypedDict):
    bucket: NotRequired[Literal["no_bucket", "avg_badge", "start_time_hour", "start_time_day", "start_time_week", "start_time_month"]]
    """Bucket allows you to group the stats by a specific field."""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> Only works for `game_modes` with badge data (e.g. `normal`, not `street_brawl`)."""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks> Only works for `game_modes` with badge data (e.g. `normal`, not `street_brawl`)."""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    hero_ids: NotRequired[list[int] | None]
    """Comma separated list of hero ids to include. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    include_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    exclude_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    ability_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats>"""
    ability_unlock_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""


class HeroBanStatsGetQuery(TypedDict):
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    bucket: NotRequired[Literal["no_bucket", "avg_badge", "start_time_hour", "start_time_day", "start_time_week", "start_time_month"]]
    """Bucket allows you to group the stats by a specific field."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. **Minimum:** March 1, 2026."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""


class HeroBuildStatsGetPath(TypedDict):
    hero_id: int
    """The hero ID to fetch build stats for. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""


class HeroBuildStatsGetQuery(TypedDict):
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    bucket: NotRequired[Literal["no_bucket", "avg_badge", "start_time_day", "start_time_week", "duration"]]
    """Bucket allows you to group the stats by a specific field. `min_matches` applies to each build and bucket."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. **Minimum:** March 1, 2026."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    hero_build_id: NotRequired[int | None]
    """Filter results for a specific hero build."""
    include_performance: NotRequired[bool | None]
    """Add the performance totals (kills, souls, damage, healing, accuracy, match length, average badge) to every build. They make the query read about three times as much data, so they are left out unless asked for."""
    min_matches: NotRequired[int | None]
    """The minimum number of matches played for a build to be included in the response."""
    account_id: NotRequired[int | None]
    """Filter for matches with a specific player account ID."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""
    ability_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats>"""
    ability_unlock_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""


class HeroCombStatsGetQuery(TypedDict):
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    include_hero_ids: NotRequired[list[int] | None]
    """Comma separated list of hero ids to include. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    exclude_hero_ids: NotRequired[list[int] | None]
    """Comma separated list of hero ids to exclude. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    include_enemy_hero_ids: NotRequired[list[int] | None]
    """Comma separated list of enemy hero ids to include. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    exclude_enemy_hero_ids: NotRequired[list[int] | None]
    """Comma separated list of enemy hero ids to exclude. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    min_matches: NotRequired[int | None]
    """The minimum number of matches played for a hero combination to be included in the response."""
    max_matches: NotRequired[int | None]
    """The maximum number of matches played for a hero combination to be included in the response."""
    comb_size: NotRequired[int | None]
    """The combination size to return."""
    account_id: NotRequired[int | None]
    """Filter for matches with a specific player account ID."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""


class HeroCountersStatsGetQuery(TypedDict):
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_enemy_networth: NotRequired[int | None]
    """Filter enemy players based on their net worth."""
    max_enemy_networth: NotRequired[int | None]
    """Filter enemy players based on their net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    same_lane_filter: NotRequired[bool | None]
    """When `true`, only considers matchups where both `hero_id` and `enemy_hero_id` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane."""
    min_matches: NotRequired[int | None]
    """The minimum number of matches played for a hero combination to be included in the response."""
    max_matches: NotRequired[int | None]
    """The maximum number of matches played for a hero combination to be included in the response."""
    account_id: NotRequired[int | None]
    """Filter for matches with a specific player account ID."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""
    hero_build_id: NotRequired[int | None]
    """Only matchups where `hero_id`'s player started the match with this hero build selected. Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}>"""


class HeroStatsGetQuery(TypedDict):
    bucket: NotRequired[Literal["no_bucket", "avg_badge", "start_time_hour", "start_time_day", "start_time_week", "start_time_month"]]
    """Bucket allows you to group the stats by a specific field."""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    min_hero_matches: NotRequired[int | None]
    """Filter players based on the number of matches they have played with a specific hero within the filtered time range (all durations, even with a duration filter)."""
    max_hero_matches: NotRequired[int | None]
    """Filter players based on the number of matches they have played with a specific hero within the filtered time range (all durations, even with a duration filter)."""
    min_hero_matches_total: NotRequired[int | None]
    """Filter players based on the number of matches they have played with a specific hero in their entire history, counting only matches of the selected `game_mode`."""
    max_hero_matches_total: NotRequired[int | None]
    """Filter players based on the number of matches they have played with a specific hero in their entire history, counting only matches of the selected `game_mode`."""
    hero_matches_total_buckets: NotRequired[list[int] | None]
    """Comma separated list of entire-history hero match counts, each the lower bound of a bucket that ends where the next one starts (the last one is open-ended), e.g. `1,25,100` for 1-24, 25-99 and 100+ matches. Groups each player's matches by their entire-history match count on the hero (counted like `min_hero_matches_total`), and the `bucket` of each row is the lower bound of its bucket. Players below the first bound are left out. Only with `bucket=no_bucket`, at most 10 bounds."""
    include_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    exclude_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    ability_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats>"""
    ability_unlock_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    account_id: NotRequired[int | None]
    """Filter for matches with a specific player account ID."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""


class HeroSwapStatsGetQuery(TypedDict):
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    bucket: NotRequired[Literal["no_bucket", "avg_badge", "start_time_hour", "start_time_day", "start_time_week", "start_time_month"]]
    """Bucket allows you to group the stats by a specific field."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago. **Minimum:** March 1, 2026."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""


class HeroSynergiesStatsGetQuery(TypedDict):
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    same_lane_filter: NotRequired[bool | None]
    """When `true`, only considers matchups where both `hero_id1` and `hero_id2` were assigned to the same lane (e.g., both Mid Lane). When `false`, considers all matchups regardless of assigned lane."""
    min_matches: NotRequired[int | None]
    """The minimum number of matches played for a hero combination to be included in the response."""
    max_matches: NotRequired[int | None]
    """The maximum number of matches played for a hero combination to be included in the response."""
    account_id: NotRequired[int | None]
    """Filter for matches with a specific player account ID."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""


class ItemFlowStatsGetQuery(TypedDict):
    phase_interval_s: NotRequired[int | None]
    """Deprecated/unused. `normal` mode uses fixed phase boundaries (0-9m, 9-20m, 20-30m, 30m+) aligned to the stats time-series; `street_brawl` columns are rounds."""
    phase_count: NotRequired[int | None]
    """Number of columns for `street_brawl` (rounds). Ignored for `normal`, which has fixed time phases. **Default:** 4."""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    hero_ids: NotRequired[str | None]
    """Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    min_matches: NotRequired[int | None]
    """The minimum number of matches for a node or edge to be included in the response."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""
    include_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    exclude_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    ability_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats>"""
    ability_unlock_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    locked_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids forming a "locked" build path. Pairs positionally with `locked_columns`: the i-th item must have been bought in the i-th `locked_columns` stage. See more: <https://api.deadlock-api.com/v1/assets/items>"""
    locked_columns: NotRequired[list[int] | None]
    """Comma separated 0-based stage column indices for each `locked_item_ids` entry (time phase for `normal`, round for `street_brawl`). Must have the same length as `locked_item_ids`."""


class ItemPermutationStatsGetQuery(TypedDict):
    item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids. See more: <https://api.deadlock-api.com/v1/assets/items>"""
    comb_size: NotRequired[int | None]
    """The combination size to return."""
    min_matches: NotRequired[int | None]
    """The minimum number of matches for an item combination to be included in the response."""
    max_matches: NotRequired[int | None]
    """The maximum number of matches for an item combination to be included in the response."""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    hero_ids: NotRequired[str | None]
    """Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    hero_id: NotRequired[int | None]
    """Filter matches based on the hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    account_id: NotRequired[int | None]
    """Filter for matches with a specific player account ID."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""
    ability_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats>"""
    ability_unlock_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    include_corrupted_items: NotRequired[bool | None]
    """Count corrupted items (build 6712+: a T3/T4 upgrade the Broker swapped for a corrupted version with the same item id) as the normal item. **Default:** `false`, corrupted purchases are ignored."""


class ItemStatsGetQuery(TypedDict):
    bucket: NotRequired[Literal["no_bucket", "hero", "team", "start_time_hour", "start_time_day", "start_time_week", "start_time_month", "game_time_min", "game_time_normalized_percentage", "net_worth_by_1000", "net_worth_by_2000", "net_worth_by_3000", "net_worth_by_5000", "net_worth_by_10000"]]
    """Bucket allows you to group the stats by a specific field."""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    hero_ids: NotRequired[str | None]
    """Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    hero_id: NotRequired[int | None]
    """Filter matches based on the hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    enemy_hero_ids: NotRequired[str | None]
    """Filter to matches where one or more of these heroes were on the opposing team. Comma separated. When set, returns "what items beat hero(es) X?" stats. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    enemy_hero_ids_all_match: NotRequired[bool | None]
    """When `true`, requires *all* of the specified `enemy_hero_ids` to be on the same enemy team. When `false` (default), matches if *any* of the specified hero(es) are on the enemy team. Ignored when `enemy_hero_ids` is unset."""
    min_enemy_networth: NotRequired[int | None]
    """Filter the specified enemy hero(es) by their final net worth. Ignored when `enemy_hero_ids` is unset."""
    max_enemy_networth: NotRequired[int | None]
    """Filter the specified enemy hero(es) by their final net worth. Ignored when `enemy_hero_ids` is unset."""
    same_lane_filter: NotRequired[bool | None]
    """When `true`, only counts buyers in the same `assigned_lane` as one of the specified enemy heroes. Ignored when `enemy_hero_ids` is unset. **Default:** `false`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    include_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to include. See more: <https://api.deadlock-api.com/v1/assets/items>"""
    exclude_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to exclude. See more: <https://api.deadlock-api.com/v1/assets/items>"""
    ability_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats>"""
    ability_unlock_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    hero_build_id: NotRequired[int | None]
    """Only players who started the match with this hero build selected (the first build they had selected when the game started). Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}>"""
    min_matches: NotRequired[int | None]
    """The minimum number of matches played for an item to be included in the response."""
    max_matches: NotRequired[int | None]
    """The maximum number of matches played for a hero combination to be included in the response."""
    account_id: NotRequired[int | None]
    """Filter for matches with a specific player account ID."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""
    min_bought_at_s: NotRequired[int | None]
    """Filter items bought after this game time (seconds)."""
    max_bought_at_s: NotRequired[int | None]
    """Filter items bought before this game time (seconds)."""
    item_order: NotRequired[list[str] | None]
    """Filter by purchase order. Each value is a comma-separated, ordered list of item ids (e.g. `1396247347,3977876567`). This is a *constraint*, not an inclusion filter: for each adjacent pair in the list, a match is excluded only when the player bought **both** items but bought the later one first. Builds missing either item are unaffected. Repeat the parameter for multiple independent orderings. See more: <https://api.deadlock-api.com/v1/assets/items>"""
    corrupted_items: NotRequired[Literal["exclude", "include", "only"] | None]
    """How to count corrupted items (build 6712+: a T3/T4 upgrade that the Broker swapped for a corrupted version with the same item id). `exclude`: only normal purchases. `include`: corrupted purchases count as the normal item. `only`: only corrupted purchases, so each row describes the corrupted variant of `item_id`. Compare it with the same request using `exclude`. Corrupted items only exist in matches from 2026-09-29 on, so `only` ignores earlier time and match-id bounds. `include` and `only` skip the pre-aggregated rollups, so those requests are slower. **Default:** `exclude`, or `include` if the deprecated `include_corrupted_items=true` is set."""
    include_corrupted_items: NotRequired[bool | None]
    """Deprecated alias of `corrupted_items=include`. `corrupted_items` takes precedence when both are set."""
    enhanced_items: NotRequired[Literal["include", "exclude", "only"]]
    """How to count enhanced items (Street Brawl only: a draft pick that is the enhanced version of an upgrade, with the same item id). `include`: enhanced purchases count as the normal item. `exclude`: only normal purchases. `only`: only enhanced purchases, so each row describes the enhanced variant of `item_id`. Compare it with the same request using `exclude`. Matches before 2026-04-08 do not record which purchases were enhanced, so `exclude` and `only` ignore earlier time and match-id bounds. `exclude` and `only` require `game_mode=street_brawl` and skip the pre-aggregated rollups, so those requests are slower. **Default:** `include`."""


class KillDeathStatsGetQuery(TypedDict):
    team: NotRequired[int | None]
    """Filter by team number."""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    account_ids: NotRequired[list[int] | None]
    """Filter matches by account IDs of players that participated in the match."""
    hero_ids: NotRequired[str | None]
    """Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    is_high_skill_range_parties: NotRequired[bool | None]
    """Filter matches based on whether they are in the high skill range."""
    is_low_pri_pool: NotRequired[bool | None]
    """Filter matches based on whether they are in the low priority pool."""
    is_new_player_pool: NotRequired[bool | None]
    """Filter matches based on whether they are in the new player pool."""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_kills_per_raster: NotRequired[int | None]
    """Filter Raster cells based on minimum kills."""
    max_kills_per_raster: NotRequired[int | None]
    """Filter Raster cells based on maximum kills."""
    min_deaths_per_raster: NotRequired[int | None]
    """Filter Raster cells based on minimum deaths."""
    max_deaths_per_raster: NotRequired[int | None]
    """Filter Raster cells based on maximum deaths."""
    min_game_time_s: NotRequired[int | None]
    """Filter kills based on their game time."""
    max_game_time_s: NotRequired[int | None]
    """Filter kills based on their game time."""


class LaneMatchupStatsGetQuery(TypedDict):
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    sample_time_s: NotRequired[int | None]
    """Seconds into the match the stat readings are taken at. **Default:** 900. Matchups whose match ended earlier are still counted in `wins` and `matches_played`, but contribute no reading; `sample_matches` reports how many did."""
    assigned_lanes: NotRequired[str | None]
    """Comma separated list of `assigned_lane` values to restrict the response to. See the `lane_info` array of <https://api.deadlock-api.com/v1/assets/generic-data>."""
    hero_ids: NotRequired[list[int] | None]
    """Comma separated list of hero ids the *ally* duo has to be drawn from, or a single hero id the *ally* duo has to include. Omit to return every duo. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    enemy_hero_ids: NotRequired[list[int] | None]
    """Comma separated list of hero ids the *enemy* duo has to be drawn from, or a single hero id the *enemy* duo has to include. Omit to return every duo. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    stats: NotRequired[str | None]
    """Comma separated list of extra per-tick stats to report, at most 8. **Default:** none."""
    group_by: NotRequired[str | None]
    """Comma separated list of dimensions to group by. Valid values: `assigned_lane`, `hero_ids`, `enemy_hero_ids`. **Default:** all three."""
    min_matches: NotRequired[int | None]
    """The minimum number of lane matchups behind a row for it to be included in the response."""
    max_matches: NotRequired[int | None]
    """The maximum number of lane matchups behind a row for it to be included in the response."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""


class LaneSoulCurveGetQuery(TypedDict):
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    min_time_s: NotRequired[int | None]
    """Earliest sample to return, in seconds into the match. **Default:** 180."""
    max_time_s: NotRequired[int | None]
    """Latest sample to return, in seconds into the match. Omit to follow every matchup to the end of its match."""
    assigned_lanes: NotRequired[str | None]
    """Comma separated list of `assigned_lane` values to restrict the response to. See the `lane_info` array of <https://api.deadlock-api.com/v1/assets/generic-data>."""
    hero_ids: NotRequired[list[int] | None]
    """Comma separated list of hero ids the *ally* duo has to be drawn from, or a single hero id the *ally* duo has to include. Omit to return every duo. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    enemy_hero_ids: NotRequired[list[int] | None]
    """Comma separated list of hero ids the *enemy* duo has to be drawn from, or a single hero id the *enemy* duo has to include. Omit to return every duo. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    stats: NotRequired[str | None]
    """Comma separated list of extra per-tick stats to return curves for, at most 8. **Default:** none."""
    group_by: NotRequired[str | None]
    """Comma separated list of dimensions to group by. Valid values: `assigned_lane`, `hero_ids`, `enemy_hero_ids`. **Default:** all three."""
    min_matches: NotRequired[int | None]
    """The minimum number of lane matchups behind a row for it to be included in the response."""
    max_matches: NotRequired[int | None]
    """The maximum number of lane matchups behind a row for it to be included in the response."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""


class PlayerPerformanceCurveGetQuery(TypedDict):
    resolution: NotRequired[int | None]
    """Resolution for relative game times in percent (0-100). **Default:** 10 (buckets of 10%). Set to **0** to use absolute game time (seconds)."""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    hero_ids: NotRequired[str | None]
    """Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    hero_build_id: NotRequired[int | None]
    """Only players who started the match with this hero build selected. Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}>"""
    include_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    exclude_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    ability_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats>"""
    ability_unlock_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""


class PlayerStatsMetricsGetQuery(TypedDict):
    hero_ids: NotRequired[str | None]
    """Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_matches: NotRequired[int | None]
    """The maximum number of matches to analyze."""
    include_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to include (only players who have purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    exclude_item_ids: NotRequired[list[int] | None]
    """Comma separated list of item ids to exclude (only players who have not purchased these items). See more: <https://api.deadlock-api.com/v1/assets/items>"""
    ability_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players whose ability upgrade order starts with exactly this sequence (one entry per ability point spent, unlocks included; see `ability_unlock_order_prefix` to match only the unlock order). See more: <https://api.deadlock-api.com/v1/analytics/ability-order-stats>"""
    ability_unlock_order_prefix: NotRequired[list[int] | None]
    """Comma separated list of ability ids: only players who unlocked (put their first point into) their abilities in exactly this order, e.g. `a,b` for players who unlocked `a` first and `b` second. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""
    include_buff_metrics: NotRequired[bool]
    """Also return the permanent buff (power-up) pickup metrics `permanent_buffs`, `permanent_buffs_per_min` and `first_permanent_buff_time_s`. Off by default because the buff columns are not in the per-hero projection, which roughly doubles the cost of hero-filtered requests. `first_permanent_buff_time_s` only covers matches since build 6712 (2026-09-29), which record pickup times; its values are `null` when the filter matches none of them."""


class HeroScoreboardGetQuery(TypedDict):
    sort_by: Literal["matches", "rank", "peak_rank", "wins", "losses", "winrate", "max_kills_per_match", "avg_kills_per_match", "kills", "max_deaths_per_match", "avg_deaths_per_match", "deaths", "max_damage_taken_per_match", "avg_damage_taken_per_match", "damage_taken", "max_assists_per_match", "avg_assists_per_match", "assists", "max_net_worth_per_match", "avg_net_worth_per_match", "net_worth", "max_last_hits_per_match", "avg_last_hits_per_match", "last_hits", "max_denies_per_match", "avg_denies_per_match", "denies", "max_player_level_per_match", "avg_player_level_per_match", "player_level", "max_creep_kills_per_match", "avg_creep_kills_per_match", "creep_kills", "max_neutral_kills_per_match", "avg_neutral_kills_per_match", "neutral_kills", "max_creep_damage_per_match", "avg_creep_damage_per_match", "creep_damage", "max_player_damage_per_match", "avg_player_damage_per_match", "player_damage", "max_neutral_damage_per_match", "avg_neutral_damage_per_match", "neutral_damage", "max_boss_damage_per_match", "avg_boss_damage_per_match", "boss_damage", "max_max_health_per_match", "avg_max_health_per_match", "max_health", "max_shots_hit_per_match", "avg_shots_hit_per_match", "shots_hit", "max_shots_missed_per_match", "avg_shots_missed_per_match", "shots_missed", "max_hero_bullets_hit_per_match", "avg_hero_bullets_hit_per_match", "hero_bullets_hit", "max_hero_bullets_hit_crit_per_match", "avg_hero_bullets_hit_crit_per_match", "hero_bullets_hit_crit", "max_permanent_buffs_per_match", "avg_permanent_buffs_per_match", "permanent_buffs"]
    """The field to sort by."""
    sort_direction: NotRequired[Literal["desc", "asc"]]
    """The direction to sort heroes in."""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    min_matches: NotRequired[int | None]
    """Filter by min number of matches played."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    account_id: NotRequired[int | None]
    """Filter for matches with a specific player account ID."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""


class PlayerScoreboardGetQuery(TypedDict):
    sort_by: Literal["matches", "rank", "peak_rank", "wins", "losses", "winrate", "max_kills_per_match", "avg_kills_per_match", "kills", "max_deaths_per_match", "avg_deaths_per_match", "deaths", "max_damage_taken_per_match", "avg_damage_taken_per_match", "damage_taken", "max_assists_per_match", "avg_assists_per_match", "assists", "max_net_worth_per_match", "avg_net_worth_per_match", "net_worth", "max_last_hits_per_match", "avg_last_hits_per_match", "last_hits", "max_denies_per_match", "avg_denies_per_match", "denies", "max_player_level_per_match", "avg_player_level_per_match", "player_level", "max_creep_kills_per_match", "avg_creep_kills_per_match", "creep_kills", "max_neutral_kills_per_match", "avg_neutral_kills_per_match", "neutral_kills", "max_creep_damage_per_match", "avg_creep_damage_per_match", "creep_damage", "max_player_damage_per_match", "avg_player_damage_per_match", "player_damage", "max_neutral_damage_per_match", "avg_neutral_damage_per_match", "neutral_damage", "max_boss_damage_per_match", "avg_boss_damage_per_match", "boss_damage", "max_max_health_per_match", "avg_max_health_per_match", "max_health", "max_shots_hit_per_match", "avg_shots_hit_per_match", "shots_hit", "max_shots_missed_per_match", "avg_shots_missed_per_match", "shots_missed", "max_hero_bullets_hit_per_match", "avg_hero_bullets_hit_per_match", "hero_bullets_hit", "max_hero_bullets_hit_crit_per_match", "avg_hero_bullets_hit_crit_per_match", "hero_bullets_hit_crit", "max_permanent_buffs_per_match", "avg_permanent_buffs_per_match", "permanent_buffs"]
    """The field to sort by."""
    sort_direction: NotRequired[Literal["desc", "asc"]]
    """The direction to sort players in."""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    hero_id: NotRequired[int | None]
    """Filter matches based on the hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    hero_build_id: NotRequired[int | None]
    """Only matches the player started with this hero build selected. Matches without a processed demo record no build. See more: <https://api.deadlock-api.com/v1/analytics/hero-build-stats/{hero_id}>"""
    min_matches: NotRequired[int | None]
    """The minimum number of matches played for a player to be included in the scoreboard."""
    max_matches: NotRequired[int | None]
    """The maximum number of matches played for a hero combination to be included in the response."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    start: NotRequired[int | None]
    """The rank to start fetching players from (1-based, like `rank`)."""
    limit: NotRequired[int | None]
    """The maximum number of players to fetch."""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""


class ListAccoladesGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetAccoladeByNameGetPath(TypedDict):
    name: str
    """Accolade `class_name` (e.g. `kills`) or `tracked_stat_name`"""


class GetAccoladeByNameGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetAccoladeGetPath(TypedDict):
    accolade_id: int
    """Accolade id (`m_unAccoladeID`)"""


class GetAccoladeGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class ListBuildTagsGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetBuildTagByNameGetPath(TypedDict):
    name: str
    """Build tag `class_name` (e.g. `citadel_build_tag_weapon`)"""


class GetBuildTagByNameGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetBuildTagGetPath(TypedDict):
    build_tag_id: int
    """Build tag id (murmurhash2 of `class_name`)"""


class GetBuildTagGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class ListColorsGetQuery(TypedDict):
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class ListConvarsGetQuery(TypedDict):
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetConvarGetPath(TypedDict):
    name: str
    """Convar name, e.g. `citadel_corrupted_item_shop_restock_interval`"""


class GetConvarGetQuery(TypedDict):
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetGenericDataGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class ListHeroesGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""
    only_active: NotRequired[bool | None]
    """When true, hides heroes that aren't player-selectable or are disabled / in-development."""


class GetHeroByNameGetPath(TypedDict):
    name: str
    """Hero class name (e.g. `hero_atlas`) or short name (e.g. `atlas`)"""


class GetHeroByNameGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetHeroGetPath(TypedDict):
    hero_id: int
    """Hero id (`m_HeroID`)"""


class GetHeroGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class ListItemsGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetItemsByHeroIdGetPath(TypedDict):
    id: int
    """Hero id (`m_HeroID`)."""


class GetItemsByHeroIdGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetItemsBySlotTypeGetPath(TypedDict):
    slot_type: ItemSlotType
    """Slot type: `weapon`, `spirit`, or `vitality`."""


class GetItemsBySlotTypeGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetItemsByTypeGetPath(TypedDict):
    type: ItemType
    """Item type: `ability`, `weapon`, or `upgrade`."""


class GetItemsByTypeGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetItemGetPath(TypedDict):
    id_or_class_name: str
    """Numeric `id` or string `class_name`."""


class GetItemGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class ListLootTablesGetQuery(TypedDict):
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetMapGetQuery(TypedDict):
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class ListMiscEntitiesGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetMiscEntityGetPath(TypedDict):
    id_or_classname: str
    """Misc entity id (`murmurhash2(class_name)`) or `class_name`"""


class GetMiscEntityGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class ListModifiersGetQuery(TypedDict):
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetModifierGetPath(TypedDict):
    id_or_classname: str
    """Modifier id (`murmurhash2(class_name)`) or `class_name`"""


class GetModifierGetQuery(TypedDict):
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class ListNpcUnitsGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetNpcUnitGetPath(TypedDict):
    id_or_classname: str
    """NPC unit id (`murmurhash2(class_name)`) or `class_name`"""


class GetNpcUnitGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class ListRankedSeasonsGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class ListRanksGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class GetRankGetPath(TypedDict):
    tier: int
    """Rank tier (0-11)"""


class GetRankGetQuery(TypedDict):
    language: NotRequired[Literal["brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german", "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish", "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish", "ukrainian", "vietnamese"] | None]
    """Language code. Defaults to `english`."""
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class SubrankImageGetPath(TypedDict):
    tier: int
    """Rank tier (1-11)"""
    subrank: int
    """Division within the tier (1-6)"""


class SubrankImageGetQuery(TypedDict):
    format: NotRequired[Literal["png", "webp"]]
    """Image format. Defaults to `png`. Supported: `png`, `webp`."""


class GetSteamInfoGetQuery(TypedDict):
    client_version: NotRequired[int | None]
    """Client/game version (e.g. `6518`). Defaults to the latest known version."""


class SearchBuildsGetQuery(TypedDict):
    min_unix_timestamp: NotRequired[int]
    """Filter builds based on their `last_updated` time (Unix timestamp)."""
    max_unix_timestamp: NotRequired[int]
    """Filter builds based on their `last_updated` time (Unix timestamp)."""
    min_published_unix_timestamp: NotRequired[int]
    """Filter builds based on their published time (Unix timestamp)."""
    max_published_unix_timestamp: NotRequired[int]
    """Filter builds based on their published time (Unix timestamp)."""
    sort_by: NotRequired[Literal["weekly_favorites", "favorites", "ignores", "reports", "updated_at", "published_at", "version"]]
    """The field to sort the builds by."""
    start: NotRequired[int]
    """The index of the first build to return."""
    limit: NotRequired[int]
    """The maximum number of builds to return."""
    sort_direction: NotRequired[Literal["desc", "asc"]]
    """The direction to sort the builds in."""
    search_name: NotRequired[str]
    """Search for builds with a name containing this string."""
    search_description: NotRequired[str]
    """Search for builds with a description containing this string."""
    only_latest: NotRequired[bool]
    """Only return the latest version of each build. The filters do not pick the version: a build whose latest version fails them is left out."""
    language: NotRequired[int]
    """Filter builds by language."""
    build_language: NotRequired[Literal["English", "German", "French", "Italian", "Korean", "SpanishSpain", "ChineseSimplified", "Russian", "Thai", "Japanese", "PortuguesePortugal", "Polish", "Czech", "Turkish", "PortugueseBrazil", "Ukrainian", "SpanishLatinAmerica", "Vietnamese"]]
    """Filter builds by language."""
    build_id: NotRequired[int]
    """Filter builds by ID."""
    version: NotRequired[int]
    """Filter builds by version."""
    hero_id: NotRequired[int]
    """Filter builds by hero ID. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    tag: NotRequired[int]
    """Filter builds by tag."""
    rollup_category: NotRequired[int]
    """Filter builds by rollup category."""
    author_id: NotRequired[int]
    """The author's `SteamID3`"""


class FetchBuildsByAuthorLiveGetPath(TypedDict):
    account_id: int
    """The players `SteamID3`"""


class FetchBuildLiveGetPath(TypedDict):
    hero_id: int
    """The hero ID of the build. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    build_id: int
    """The build ID to fetch."""


class FetchBuildLiveGetQuery(TypedDict):
    force_refetch: NotRequired[bool]
    """Fetch the build from the Game Coordinator even if it is already in the database."""


class CommandResolveGetQuery(TypedDict):
    region: NotRequired[Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"]]
    """The players region"""
    account_id: int
    """The players `SteamID3`"""
    template: NotRequired[str]
    """The command template to resolve"""
    hero_name: NotRequired[str | None]
    """Hero name to check for hero specific stats"""


class VariablesResolveGetQuery(TypedDict):
    region: NotRequired[Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"]]
    account_id: int
    variables: NotRequired[str]
    """Variables to resolve, separated by commas."""
    hero_name: NotRequired[str | None]
    """Hero name to check for hero specific stats"""


class CodeImageGetQuery(TypedDict):
    code: str
    """Crosshair share code, as copied from the game's crosshair settings (`DL.…`), or crosshair console commands (`citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245`)."""
    screen_height: NotRequired[int]
    """Height of the screen to render for, in pixels. Crosshair sizes scale with it."""
    scale: NotRequired[int]
    """Enlarges the image, drawing every pixel as a `scale`-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels."""


class CodeSettingsGetQuery(TypedDict):
    code: str
    """Crosshair share code, as copied from the game's crosshair settings (`DL.…`), or crosshair console commands (`citadel_crosshair_dot_size 4; citadel_crosshair_color_r 245`)."""


class SettingsCodeGetQuery(TypedDict):
    themed: NotRequired[bool]
    """Use the hero's own crosshair instead of these settings."""
    pip_gap_static: NotRequired[bool]
    """Keep the pips at a fixed distance instead of spreading them with weapon spread."""
    pip_width: NotRequired[int]
    pip_height: NotRequired[int]
    pip_gap: NotRequired[int]
    pip_opacity: NotRequired[float]
    """0 to 1."""
    pip_outline_border: NotRequired[int]
    pip_outline_gap: NotRequired[int]
    pip_outline_opacity: NotRequired[float]
    """0 to 1."""
    dot_size: NotRequired[int]
    dot_opacity: NotRequired[float]
    """0 to 1."""
    dot_outline_border: NotRequired[int]
    dot_outline_gap: NotRequired[int]
    dot_outline_opacity: NotRequired[float]
    """0 to 1."""
    color_r: NotRequired[int]
    color_g: NotRequired[int]
    color_b: NotRequired[int]
    outline_color_r: NotRequired[int]
    outline_color_g: NotRequired[int]
    outline_color_b: NotRequired[int]


class SettingsImageGetQuery(TypedDict):
    themed: NotRequired[bool]
    """Use the hero's own crosshair instead of these settings."""
    pip_gap_static: NotRequired[bool]
    """Keep the pips at a fixed distance instead of spreading them with weapon spread."""
    pip_width: NotRequired[int]
    pip_height: NotRequired[int]
    pip_gap: NotRequired[int]
    pip_opacity: NotRequired[float]
    """0 to 1."""
    pip_outline_border: NotRequired[int]
    pip_outline_gap: NotRequired[int]
    pip_outline_opacity: NotRequired[float]
    """0 to 1."""
    dot_size: NotRequired[int]
    dot_opacity: NotRequired[float]
    """0 to 1."""
    dot_outline_border: NotRequired[int]
    dot_outline_gap: NotRequired[int]
    dot_outline_opacity: NotRequired[float]
    """0 to 1."""
    color_r: NotRequired[int]
    color_g: NotRequired[int]
    color_b: NotRequired[int]
    outline_color_r: NotRequired[int]
    outline_color_g: NotRequired[int]
    outline_color_b: NotRequired[int]
    screen_height: NotRequired[int]
    """Height of the screen to render for, in pixels. Crosshair sizes scale with it."""
    scale: NotRequired[int]
    """Enlarges the image, drawing every pixel as a `scale`-sized square, for a picture larger than the crosshair itself (a link preview). Lowered when the image would pass 2048 pixels."""


class LeaderboardGetPath(TypedDict):
    region: Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"]
    """The region to fetch the leaderboard for."""


class LeaderboardGetQuery(TypedDict):
    leaderboard_id: NotRequired[int]
    """Leaderboard to fetch, e.g. a ranked season's `leaderboard_id` from <https://api.deadlock-api.com/v1/assets/ranked-seasons>. Defaults to the current one."""


class LeaderboardRawGetPath(TypedDict):
    region: Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"]
    """The region to fetch the leaderboard for."""


class LeaderboardRawGetQuery(TypedDict):
    leaderboard_id: NotRequired[int]
    """Leaderboard to fetch, e.g. a ranked season's `leaderboard_id` from <https://api.deadlock-api.com/v1/assets/ranked-seasons>. Defaults to the current one."""


class LeaderboardHeroGetPath(TypedDict):
    region: Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"]
    """The region to fetch the leaderboard for."""
    hero_id: int
    """The hero ID to fetch the leaderboard for. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""


class LeaderboardHeroGetQuery(TypedDict):
    leaderboard_id: NotRequired[int]
    """Leaderboard to fetch, e.g. a ranked season's `leaderboard_id` from <https://api.deadlock-api.com/v1/assets/ranked-seasons>. Defaults to the current one."""


class LeaderboardHeroRawGetPath(TypedDict):
    region: Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"]
    """The region to fetch the leaderboard for."""
    hero_id: int
    """The hero ID to fetch the leaderboard for. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""


class LeaderboardHeroRawGetQuery(TypedDict):
    leaderboard_id: NotRequired[int]
    """Leaderboard to fetch, e.g. a ranked season's `leaderboard_id` from <https://api.deadlock-api.com/v1/assets/ranked-seasons>. Defaults to the current one."""


class ActiveMatchesGetQuery(TypedDict):
    account_id: NotRequired[int | None]
    """The account ID to filter active matches by (`SteamID3`)"""
    account_ids: NotRequired[list[int] | None]
    """Comma separated list of account ids to include"""


class GetCustomGetPath(TypedDict):
    party_id: int


class LiveQueryGetQuery(TypedDict):
    query: str
    """SQL query to run over the broadcast's entity/event tables (see `/demo/schema`)."""
    match_id: NotRequired[int | None]
    """Match to spectate and stream. Provide this or `broadcast_url`; `broadcast_url` wins if both are given. Resolving a match spectates its lobby and is rate-limited."""
    broadcast_url: NotRequired[str | None]
    """Explicit broadcast base URL (from `/live/urls`). Provide this or `match_id`."""


class StatusGetPath(TypedDict):
    job_id: str
    """Job id returned by POST /demo/query"""


class SchemaGetQuery(TypedDict):
    match_id: NotRequired[int | None]
    """Match to read the schema for. If omitted, the schema of the most recent match we have a demo for is returned. When set, the demo's salts are fetched (rate limited) if they are not already stored."""


class BulkMetadataGetQuery(TypedDict):
    include_info: NotRequired[bool]
    """Include match info in the response."""
    include_more_info: NotRequired[bool]
    """Include more match info in the response."""
    include_objectives: NotRequired[bool]
    """Include objectives in the response."""
    include_mid_boss: NotRequired[bool]
    """Include midboss in the response."""
    include_player_info: NotRequired[bool]
    """Include player info in the response."""
    include_player_kda: NotRequired[bool]
    """Include only K/D/A fields (`kills`, `deaths`, `assists`) for players."""
    include_player_items: NotRequired[bool]
    """Include player items in the response."""
    include_player_stats: NotRequired[bool]
    """Include player stats in the response."""
    include_player_final_stats: NotRequired[bool]
    """Include only the final per-player stats (last sample of every `stats.*` time-series) as a single `final_stats` object. Far cheaper than `include_player_stats`, which returns the whole array per field."""
    include_player_death_details: NotRequired[bool]
    """Include player death details in the response."""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. Omit or pass empty string for no filter."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    match_ids: NotRequired[list[int] | None]
    """Comma separated list of match ids, limited by `limit`"""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    is_high_skill_range_parties: NotRequired[bool | None]
    """Filter matches based on whether they are in the high skill range."""
    is_low_pri_pool: NotRequired[bool | None]
    """Filter matches based on whether they are in the low priority pool."""
    is_new_player_pool: NotRequired[bool | None]
    """Filter matches based on whether they are in the new player pool."""
    account_ids: NotRequired[list[int] | None]
    """Filter matches by account IDs of players that participated in the match."""
    only_filtered_players: NotRequired[bool]
    """Only include the players matching `account_ids` in the `players` array instead of all players of the match. Requires `account_ids`."""
    hero_ids: NotRequired[str | None]
    """Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    item_filter_hero_id: NotRequired[int | None]
    """Hero ID to scope item filters to. Required when using `include_item_ids` or `exclude_item_ids`."""
    include_item_ids: NotRequired[str | None]
    """Comma separated list of item ids to include. Requires `item_filter_hero_id`. Returns matches where a player on the specified hero has ALL of these items."""
    exclude_item_ids: NotRequired[str | None]
    """Comma separated list of item ids to exclude. Requires `item_filter_hero_id`. Returns matches where a player on the specified hero has NONE of these items."""
    extra_match_columns: NotRequired[str | None]
    """Comma separated list of extra match-level columns to include in the response. Each column is aggregated with `any(...)`. Only alphanumeric characters, underscores, and dots (for nested field access) are allowed. Example: `objectives_mask_team0,team_score`."""
    extra_player_columns: NotRequired[str | None]
    """Comma separated list of extra player-level columns to include in the response. Each column is added inside the player tuple. Only alphanumeric characters, underscores, and dots (for nested field access) are allowed. Example: `stats.player_damage,stats.player_healing`. Implicitly enables player fields."""
    order_by: NotRequired[Literal["match_id", "start_time", "average_badge"]]
    """The field to order the results by."""
    order_direction: NotRequired[Literal["desc", "asc"]]
    """The direction to order the results by."""
    limit: NotRequired[int]
    """The maximum number of matches to return."""
    format: NotRequired[Literal["json", "ndjson"]]
    """The response format. Valid values: `json` (a JSON array), `ndjson` (newline-delimited JSON objects)."""


class UrlGetPath(TypedDict):
    match_id: int
    """The match ID"""


class MetadataGetPath(TypedDict):
    match_id: int
    """The match ID"""


class MetadataGetQuery(TypedDict):
    is_custom: NotRequired[bool | None]
    disable_steam: NotRequired[bool | None]
    """If `true`, skip the Steam fallback when the metadata is not available in S3 and return an error instead."""


class MetadataRawGetPath(TypedDict):
    match_id: int
    """The match ID"""


class MetadataRawGetQuery(TypedDict):
    is_custom: NotRequired[bool | None]
    disable_steam: NotRequired[bool | None]
    """If `true`, skip the Steam fallback when the metadata is not available in S3 and return an error instead."""


class SaltsGetPath(TypedDict):
    match_id: int
    """The match ID"""


class SaltsGetQuery(TypedDict):
    disable_steam: NotRequired[bool | None]
    """If `true`, skip the Steam fallback when the salts are not available in Clickhouse and return an error instead."""


class BotFriendStatusGetPath(TypedDict):
    account_id: str
    """The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint"""


class PlayerHeroStatsGetQuery(TypedDict):
    account_ids: list[int]
    """Comma separated list of account ids, in `SteamID3` or `SteamID64` format."""
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    match_mode: NotRequired[str | None]
    """Filter matches based on the match mode. Valid values: `unranked`, `private_lobby`, `coop_bot`, `ranked`, `server_test`, `tutorial`, `hero_labs`. **Default:** `ranked,unranked`."""
    hero_ids: NotRequired[str | None]
    """Filter matches based on the hero IDs. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    max_networth: NotRequired[int | None]
    """Filter players based on their final net worth."""
    min_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    max_average_badge: NotRequired[int | None]
    """Filter matches based on the average badge level (tier = first digits, subtier = last digit) of *both* teams involved. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""


class MmrGetQuery(TypedDict):
    account_ids: list[int]
    """Comma separated list of account ids, in `SteamID3` or `SteamID64` format."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""


class MmrDistributionGetQuery(TypedDict):
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    is_high_skill_range_parties: NotRequired[bool | None]
    """Filter matches based on whether they are in the high skill range."""
    is_low_pri_pool: NotRequired[bool | None]
    """Filter matches based on whether they are in the low priority pool."""
    is_new_player_pool: NotRequired[bool | None]
    """Filter matches based on whether they are in the new player pool."""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""


class HeroMmrDistributionGetPath(TypedDict):
    hero_id: int
    """The hero ID to fetch the MMR history for. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""


class HeroMmrDistributionGetQuery(TypedDict):
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    is_high_skill_range_parties: NotRequired[bool | None]
    """Filter matches based on whether they are in the high skill range."""
    is_low_pri_pool: NotRequired[bool | None]
    """Filter matches based on whether they are in the low priority pool."""
    is_new_player_pool: NotRequired[bool | None]
    """Filter matches based on whether they are in the new player pool."""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""


class HeroMmrGetPath(TypedDict):
    hero_id: int
    """The hero ID to fetch the MMR history for. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""


class HeroMmrGetQuery(TypedDict):
    account_ids: list[int]
    """Comma separated list of account ids, in `SteamID3` or `SteamID64` format."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""


class RankBatchGetQuery(TypedDict):
    account_ids: list[int]
    """Comma separated list of account ids, in `SteamID3` or `SteamID64` format."""


class RankPredictAvgImageGetQuery(TypedDict):
    account_ids: list[int]
    """Comma-separated list of account IDs (max 12)."""
    format: NotRequired[Literal["png", "webp"]]
    """Image format. Defaults to `png`. Supported: `png`, `webp`."""


class RankDistributionGetQuery(TypedDict):
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    is_high_skill_range_parties: NotRequired[bool | None]
    """Filter matches based on whether they are in the high skill range."""
    is_low_pri_pool: NotRequired[bool | None]
    """Filter matches based on whether they are in the low priority pool."""
    is_new_player_pool: NotRequired[bool | None]
    """Filter matches based on whether they are in the new player pool."""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""


class RankAvgImageGetQuery(TypedDict):
    account_ids: list[int]
    """Comma-separated list of account IDs (max 12)."""
    format: NotRequired[Literal["png", "webp"]]
    """Image format. Defaults to `png`. Supported: `png`, `webp`."""


class SteamGetQuery(TypedDict):
    account_ids: list[int]
    """Comma separated list of account ids, in `SteamID3` or `SteamID64` format."""
    refresh: NotRequired[bool]
    """Refresh the listed profiles from the Steam Web API before returning."""


class SteamSearchGetQuery(TypedDict):
    search_query: str
    """Search query for Steam profiles."""
    limit: NotRequired[int | None]
    """Maximum number of profiles to return."""
    min_matches_played_last_30d: NotRequired[int | None]
    """Only return profiles that have played at least this many matches in the last 30 days. Defaults to 5 to filter out inactive/empty profiles and keep search responsive."""
    min_last_team_avg_badge: NotRequired[int | None]
    """Only return profiles whose `last_team_avg_badge` is at least this value. Defaults to 0 (no filter). Profiles with no recorded badge are stored as 0 and are excluded when this is set above 0."""
    matches_played_weight: NotRequired[float | None]
    """Weight applied to `log1p(matches_played_last_30d)` when reranking candidates. The final score per profile is `jaro_winkler(personaname_lc, query) + weight * log1p(matches_played)`. Set to 0 to rank purely by string similarity; raise it to bias toward active/popular players."""


class EnemyStatsGetPath(TypedDict):
    account_id: int
    """The players `SteamID3`"""


class EnemyStatsGetQuery(TypedDict):
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    min_matches_played: NotRequired[int | None]
    """Filter based on the number of matches played."""
    max_matches_played: NotRequired[int | None]
    """Filter based on the number of matches played."""


class IngestStatusGetPath(TypedDict):
    account_id: int
    """The players `SteamID3`"""


class MatchHistoryGetPath(TypedDict):
    account_id: int
    """The players `SteamID3`"""


class MatchHistoryGetQuery(TypedDict):
    force_refetch: NotRequired[bool]
    """Refetch the match history from Steam, even if it is already cached in `ClickHouse`. Only use this if you are sure that the data in `ClickHouse` is outdated. Enabling this flag results in a strict rate limit."""


class MateStatsGetPath(TypedDict):
    account_id: int
    """The players `SteamID3`"""


class MateStatsGetQuery(TypedDict):
    game_mode: NotRequired[Literal["normal", "street_brawl", "explore_n_y_c", "internal", "internal02"] | None]
    """Filter matches based on their game mode. Valid values: `normal`, `street_brawl`. **Default:** `normal`."""
    min_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    max_unix_timestamp: NotRequired[int | None]
    """Filter matches based on their start time (Unix timestamp)."""
    min_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    max_duration_s: NotRequired[int | None]
    """Filter matches based on their duration in seconds (up to 7000s)."""
    min_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    max_match_id: NotRequired[int | None]
    """Filter matches based on their ID."""
    min_matches_played: NotRequired[int | None]
    """Filter based on the number of matches played."""
    max_matches_played: NotRequired[int | None]
    """Filter based on the number of matches played."""
    same_party: NotRequired[bool]
    """Filter based on whether the mates were on the same party. Two players are considered to be in the same party if they were on the same team and are Steam friends as of the match start time (per the `steam_profiles` friends list)."""


class MmrHistoryGetPath(TypedDict):
    account_id: int
    """The players `SteamID3`"""


class HeroMmrHistoryGetPath(TypedDict):
    account_id: int
    """The players `SteamID3`"""
    hero_id: int
    """The hero ID to fetch the MMR history for. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""


class RankGetPath(TypedDict):
    account_id: int
    """The players `SteamID3`"""


class RankPredictGetPath(TypedDict):
    account_id: int
    """The players `SteamID3`"""


class RankPredictImageGetPath(TypedDict):
    account_id: int
    """The players `SteamID3`"""


class RankPredictImageGetQuery(TypedDict):
    format: NotRequired[Literal["png", "webp"]]
    """Image format. Defaults to `png`. Supported: `png`, `webp`."""


class RankImageGetPath(TypedDict):
    account_id: int
    """The players `SteamID3`"""


class RankImageGetQuery(TypedDict):
    format: NotRequired[Literal["png", "webp"]]
    """Image format. Defaults to `png`. Supported: `png`, `webp`."""


class SqlGetQuery(TypedDict):
    query: str
    """The SQL query to execute. It must follow the `DuckDB` SQL syntax."""
    format: NotRequired[Literal["json", "ndjson"]]
    """The response format. Valid values: `json` (a JSON array), `ndjson` (newline-delimited JSON objects)."""


class TableSchemaGetPath(TypedDict):
    table: str
    """The name of the table to fetch the schema for."""


class TypedGetMixin:
    """Typed overloads for every GET endpoint. Implemented by the client."""

    @overload
    def get(self, path: Literal["/v1/analytics/ability-max-first-stats"], *, query: AbilityMaxFirstStatsGetQuery, options: CallOptions | None = None) -> list[AnalyticsAbilityMaxFirstStats]:
        """Ability Max First Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/ability-order-stats"], *, query: AbilityOrderStatsGetQuery, options: CallOptions | None = None) -> list[AnalyticsAbilityOrderStats]:
        """Ability Order Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/ability-order-tree"], *, query: AbilityOrderTreeGetQuery, options: CallOptions | None = None) -> list[AnalyticsAbilityOrderTreeNode]:
        """Ability Order Tree"""

    @overload
    def get(self, path: Literal["/v1/analytics/badge-distribution"], *, query: BadgeDistributionGetQuery | None = None, options: CallOptions | None = None) -> list[BadgeDistribution]:
        """Badge Distribution"""

    @overload
    def get(self, path: Literal["/v1/analytics/buff-stats"], *, query: BuffStatsGetQuery | None = None, options: CallOptions | None = None) -> list[AnalyticsBuffStats]:
        """Buff Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/build-item-stats"], *, query: BuildItemStatsGetQuery | None = None, options: CallOptions | None = None) -> list[BuildItemStats]:
        """Build Item Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/game-stats"], *, query: GameStatsGetQuery | None = None, options: CallOptions | None = None) -> list[AnalyticsGameStats]:
        """Game Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/hero-ban-stats"], *, query: HeroBanStatsGetQuery | None = None, options: CallOptions | None = None) -> list[HeroBanStats]:
        """Hero Ban Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/hero-build-stats/{hero_id}"], *, path_params: HeroBuildStatsGetPath, query: HeroBuildStatsGetQuery | None = None, options: CallOptions | None = None) -> list[HeroBuildStats]:
        """Hero Build Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/hero-comb-stats"], *, query: HeroCombStatsGetQuery | None = None, options: CallOptions | None = None) -> list[HeroCombStats]:
        """Hero Comb Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/hero-counter-stats"], *, query: HeroCountersStatsGetQuery | None = None, options: CallOptions | None = None) -> list[HeroCounterStats]:
        """Hero Counter Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/hero-stats"], *, query: HeroStatsGetQuery | None = None, options: CallOptions | None = None) -> list[AnalyticsHeroStats]:
        """Hero Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/hero-swap-stats"], *, query: HeroSwapStatsGetQuery | None = None, options: CallOptions | None = None) -> list[HeroSwapStats]:
        """Hero Swap Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/hero-synergy-stats"], *, query: HeroSynergiesStatsGetQuery | None = None, options: CallOptions | None = None) -> list[HeroSynergyStats]:
        """Hero Synergy Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/item-flow-stats"], *, query: ItemFlowStatsGetQuery | None = None, options: CallOptions | None = None) -> ItemFlowStats:
        """Item Flow Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/item-permutation-stats"], *, query: ItemPermutationStatsGetQuery | None = None, options: CallOptions | None = None) -> list[ItemPermutationStats]:
        """Item Permutation Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/item-stats"], *, query: ItemStatsGetQuery | None = None, options: CallOptions | None = None) -> list[ItemStats]:
        """Item Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/kill-death-stats"], *, query: KillDeathStatsGetQuery | None = None, options: CallOptions | None = None) -> list[KillDeathStats]:
        """Kill Death Stats"""

    @overload
    def get(self, path: Literal["/v1/analytics/lane-matchup-stats"], *, query: LaneMatchupStatsGetQuery | None = None, options: CallOptions | None = None) -> list[LaneMatchupStats]:
        """Lane Matchup Stats (Subject to Change)"""

    @overload
    def get(self, path: Literal["/v1/analytics/lane-soul-curve"], *, query: LaneSoulCurveGetQuery | None = None, options: CallOptions | None = None) -> list[LaneSoulCurve]:
        """Lane Soul Curve (Subject to Change)"""

    @overload
    def get(self, path: Literal["/v1/analytics/player-performance-curve"], *, query: PlayerPerformanceCurveGetQuery | None = None, options: CallOptions | None = None) -> list[PlayerPerformanceCurvePoint]:
        """Player Performance Curve"""

    @overload
    def get(self, path: Literal["/v1/analytics/player-stats/metrics"], *, query: PlayerStatsMetricsGetQuery | None = None, options: CallOptions | None = None) -> HashMap:
        """Player Stats Metrics"""

    @overload
    def get(self, path: Literal["/v1/analytics/scoreboards/heroes"], *, query: HeroScoreboardGetQuery, options: CallOptions | None = None) -> list[HeroEntry]:
        """Hero Scoreboard"""

    @overload
    def get(self, path: Literal["/v1/analytics/scoreboards/players"], *, query: PlayerScoreboardGetQuery, options: CallOptions | None = None) -> list[PlayerEntry]:
        """Player Scoreboard"""

    @overload
    def get(self, path: Literal["/v1/assets/accolades"], *, query: ListAccoladesGetQuery | None = None, options: CallOptions | None = None) -> list[Accolade]:
        """List Accolades"""

    @overload
    def get(self, path: Literal["/v1/assets/accolades/by-name/{name}"], *, path_params: GetAccoladeByNameGetPath, query: GetAccoladeByNameGetQuery | None = None, options: CallOptions | None = None) -> Accolade:
        """Get Accolade By Name"""

    @overload
    def get(self, path: Literal["/v1/assets/accolades/{accolade_id}"], *, path_params: GetAccoladeGetPath, query: GetAccoladeGetQuery | None = None, options: CallOptions | None = None) -> Accolade:
        """Get Accolade"""

    @overload
    def get(self, path: Literal["/v1/assets/build-tags"], *, query: ListBuildTagsGetQuery | None = None, options: CallOptions | None = None) -> list[BuildTag]:
        """List Build Tags"""

    @overload
    def get(self, path: Literal["/v1/assets/build-tags/by-name/{name}"], *, path_params: GetBuildTagByNameGetPath, query: GetBuildTagByNameGetQuery | None = None, options: CallOptions | None = None) -> BuildTag:
        """Get Build Tag By Name"""

    @overload
    def get(self, path: Literal["/v1/assets/build-tags/{build_tag_id}"], *, path_params: GetBuildTagGetPath, query: GetBuildTagGetQuery | None = None, options: CallOptions | None = None) -> BuildTag:
        """Get Build Tag"""

    @overload
    def get(self, path: Literal["/v1/assets/client-versions"], *, options: CallOptions | None = None) -> list[int]:
        """List Client Versions"""

    @overload
    def get(self, path: Literal["/v1/assets/colors"], *, query: ListColorsGetQuery | None = None, options: CallOptions | None = None) -> dict[str, Color]:
        """List Colors"""

    @overload
    def get(self, path: Literal["/v1/assets/convars"], *, query: ListConvarsGetQuery | None = None, options: CallOptions | None = None) -> dict[str, Convar]:
        """List Convars"""

    @overload
    def get(self, path: Literal["/v1/assets/convars/{name}"], *, path_params: GetConvarGetPath, query: GetConvarGetQuery | None = None, options: CallOptions | None = None) -> Convar:
        """Get Convar"""

    @overload
    def get(self, path: Literal["/v1/assets/fonts"], *, options: CallOptions | None = None) -> Any:
        """Fonts Index"""

    @overload
    def get(self, path: Literal["/v1/assets/generic-data"], *, query: GetGenericDataGetQuery | None = None, options: CallOptions | None = None) -> GenericData:
        """Get Generic Data"""

    @overload
    def get(self, path: Literal["/v1/assets/heroes"], *, query: ListHeroesGetQuery | None = None, options: CallOptions | None = None) -> list[Hero]:
        """List Heroes"""

    @overload
    def get(self, path: Literal["/v1/assets/heroes/by-name/{name}"], *, path_params: GetHeroByNameGetPath, query: GetHeroByNameGetQuery | None = None, options: CallOptions | None = None) -> Hero:
        """Get Hero By Name"""

    @overload
    def get(self, path: Literal["/v1/assets/heroes/{hero_id}"], *, path_params: GetHeroGetPath, query: GetHeroGetQuery | None = None, options: CallOptions | None = None) -> Hero:
        """Get Hero"""

    @overload
    def get(self, path: Literal["/v1/assets/icons"], *, options: CallOptions | None = None) -> Any:
        """Icons Index"""

    @overload
    def get(self, path: Literal["/v1/assets/images"], *, options: CallOptions | None = None) -> Any:
        """Images Index"""

    @overload
    def get(self, path: Literal["/v1/assets/items"], *, query: ListItemsGetQuery | None = None, options: CallOptions | None = None) -> list[Item]:
        """List Items"""

    @overload
    def get(self, path: Literal["/v1/assets/items/by-hero-id/{id}"], *, path_params: GetItemsByHeroIdGetPath, query: GetItemsByHeroIdGetQuery | None = None, options: CallOptions | None = None) -> list[Item]:
        """List Items By Hero"""

    @overload
    def get(self, path: Literal["/v1/assets/items/by-slot-type/{slot_type}"], *, path_params: GetItemsBySlotTypeGetPath, query: GetItemsBySlotTypeGetQuery | None = None, options: CallOptions | None = None) -> list[Item]:
        """List Items By Slot Type"""

    @overload
    def get(self, path: Literal["/v1/assets/items/by-type/{type}"], *, path_params: GetItemsByTypeGetPath, query: GetItemsByTypeGetQuery | None = None, options: CallOptions | None = None) -> list[Item]:
        """List Items By Type"""

    @overload
    def get(self, path: Literal["/v1/assets/items/{id_or_class_name}"], *, path_params: GetItemGetPath, query: GetItemGetQuery | None = None, options: CallOptions | None = None) -> Item:
        """Get Item"""

    @overload
    def get(self, path: Literal["/v1/assets/loot-tables"], *, query: ListLootTablesGetQuery | None = None, options: CallOptions | None = None) -> dict[str, LootTable]:
        """List Loot Tables"""

    @overload
    def get(self, path: Literal["/v1/assets/map"], *, query: GetMapGetQuery | None = None, options: CallOptions | None = None) -> MapData:
        """Map"""

    @overload
    def get(self, path: Literal["/v1/assets/misc-entities"], *, query: ListMiscEntitiesGetQuery | None = None, options: CallOptions | None = None) -> list[MiscEntity]:
        """List Misc Entities"""

    @overload
    def get(self, path: Literal["/v1/assets/misc-entities/{id_or_classname}"], *, path_params: GetMiscEntityGetPath, query: GetMiscEntityGetQuery | None = None, options: CallOptions | None = None) -> MiscEntity:
        """Get Misc Entity"""

    @overload
    def get(self, path: Literal["/v1/assets/models"], *, options: CallOptions | None = None) -> Any:
        """Models Index"""

    @overload
    def get(self, path: Literal["/v1/assets/modifiers"], *, query: ListModifiersGetQuery | None = None, options: CallOptions | None = None) -> list[Modifier]:
        """List Modifiers"""

    @overload
    def get(self, path: Literal["/v1/assets/modifiers/{id_or_classname}"], *, path_params: GetModifierGetPath, query: GetModifierGetQuery | None = None, options: CallOptions | None = None) -> Modifier:
        """Get Modifier"""

    @overload
    def get(self, path: Literal["/v1/assets/npc-units"], *, query: ListNpcUnitsGetQuery | None = None, options: CallOptions | None = None) -> list[NpcUnit]:
        """List NPC Units"""

    @overload
    def get(self, path: Literal["/v1/assets/npc-units/{id_or_classname}"], *, path_params: GetNpcUnitGetPath, query: GetNpcUnitGetQuery | None = None, options: CallOptions | None = None) -> NpcUnit:
        """Get NPC Unit"""

    @overload
    def get(self, path: Literal["/v1/assets/ranked-seasons"], *, query: ListRankedSeasonsGetQuery | None = None, options: CallOptions | None = None) -> list[RankedSeason]:
        """List Ranked Seasons"""

    @overload
    def get(self, path: Literal["/v1/assets/ranks"], *, query: ListRanksGetQuery | None = None, options: CallOptions | None = None) -> list[Rank]:
        """List Ranks"""

    @overload
    def get(self, path: Literal["/v1/assets/ranks/{tier}"], *, path_params: GetRankGetPath, query: GetRankGetQuery | None = None, options: CallOptions | None = None) -> Rank:
        """Get Rank"""

    @overload
    def get(self, path: Literal["/v1/assets/ranks/{tier}/{subrank}/image"], *, path_params: SubrankImageGetPath, query: SubrankImageGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Rank Subrank Image"""

    @overload
    def get(self, path: Literal["/v1/assets/sounds"], *, options: CallOptions | None = None) -> Any:
        """Sounds Index"""

    @overload
    def get(self, path: Literal["/v1/assets/steam-info"], *, query: GetSteamInfoGetQuery | None = None, options: CallOptions | None = None) -> SteamInfo:
        """Get Steam Info"""

    @overload
    def get(self, path: Literal["/v1/assets/steam-info/all"], *, options: CallOptions | None = None) -> list[SteamInfo]:
        """Get All Steam Infos"""

    @overload
    def get(self, path: Literal["/v1/builds"], *, query: SearchBuildsGetQuery | None = None, options: CallOptions | None = None) -> list[Build]:
        """Search"""

    @overload
    def get(self, path: Literal["/v1/builds/by-author/{account_id}"], *, path_params: FetchBuildsByAuthorLiveGetPath, options: CallOptions | None = None) -> list[Build]:
        """Fetch Live by Author"""

    @overload
    def get(self, path: Literal["/v1/builds/{hero_id}/{build_id}"], *, path_params: FetchBuildLiveGetPath, query: FetchBuildLiveGetQuery | None = None, options: CallOptions | None = None) -> Build:
        """Fetch Live"""

    @overload
    def get(self, path: Literal["/v1/commands/resolve"], *, query: CommandResolveGetQuery, options: CallOptions | None = None) -> str:
        """Resolve Command"""

    @overload
    def get(self, path: Literal["/v1/commands/variables/available"], *, options: CallOptions | None = None) -> list[VariableDescription]:
        """Available Variables"""

    @overload
    def get(self, path: Literal["/v1/commands/variables/resolve"], *, query: VariablesResolveGetQuery, options: CallOptions | None = None) -> dict[str, str]:
        """Resolve Variables"""

    @overload
    def get(self, path: Literal["/v1/commands/widgets/versions"], *, options: CallOptions | None = None) -> dict[str, int]:
        """Widget Versions"""

    @overload
    def get(self, path: Literal["/v1/crosshair/code/image"], *, query: CodeImageGetQuery, options: CallOptions | None = None) -> bytes:
        """Crosshair Code Image"""

    @overload
    def get(self, path: Literal["/v1/crosshair/code/settings"], *, query: CodeSettingsGetQuery, options: CallOptions | None = None) -> Settings:
        """Crosshair Code Settings"""

    @overload
    def get(self, path: Literal["/v1/crosshair/settings/code"], *, query: SettingsCodeGetQuery | None = None, options: CallOptions | None = None) -> CrosshairCode:
        """Crosshair Settings Code"""

    @overload
    def get(self, path: Literal["/v1/crosshair/settings/image"], *, query: SettingsImageGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Crosshair Settings Image"""

    @overload
    def get(self, path: Literal["/v1/graphql"], *, options: CallOptions | None = None) -> str:
        """GraphQL Playground"""

    @overload
    def get(self, path: Literal["/v1/info"], *, options: CallOptions | None = None) -> APIInfo:
        """API Info"""

    @overload
    def get(self, path: Literal["/v1/info/health"], *, options: CallOptions | None = None) -> Status:
        """Health Check"""

    @overload
    def get(self, path: Literal["/v1/leaderboard/{region}"], *, path_params: LeaderboardGetPath, query: LeaderboardGetQuery | None = None, options: CallOptions | None = None) -> Leaderboard:
        """Leaderboard"""

    @overload
    def get(self, path: Literal["/v1/leaderboard/{region}/raw"], *, path_params: LeaderboardRawGetPath, query: LeaderboardRawGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Leaderboard as Protobuf"""

    @overload
    def get(self, path: Literal["/v1/leaderboard/{region}/{hero_id}"], *, path_params: LeaderboardHeroGetPath, query: LeaderboardHeroGetQuery | None = None, options: CallOptions | None = None) -> Leaderboard:
        """Hero Leaderboard"""

    @overload
    def get(self, path: Literal["/v1/leaderboard/{region}/{hero_id}/raw"], *, path_params: LeaderboardHeroRawGetPath, query: LeaderboardHeroRawGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Hero Leaderboard as Protobuf"""

    @overload
    def get(self, path: Literal["/v1/matches/active"], *, query: ActiveMatchesGetQuery | None = None, options: CallOptions | None = None) -> list[ActiveMatch]:
        """Active"""

    @overload
    def get(self, path: Literal["/v1/matches/active/raw"], *, options: CallOptions | None = None) -> bytes:
        """Active as Protobuf"""

    @overload
    def get(self, path: Literal["/v1/matches/custom/{party_id}/match-id"], *, path_params: GetCustomGetPath, options: CallOptions | None = None) -> GetCustomMatchIdResponse:
        """Get Match ID"""

    @overload
    def get(self, path: Literal["/v1/matches/demo/live/query"], *, query: LiveQueryGetQuery, options: CallOptions | None = None) -> str:
        """Live Demo Query (SSE)"""

    @overload
    def get(self, path: Literal["/v1/matches/demo/query/{job_id}"], *, path_params: StatusGetPath, options: CallOptions | None = None) -> DemoQueryStatusResponse:
        """Demo Query Status"""

    @overload
    def get(self, path: Literal["/v1/matches/demo/schema"], *, query: SchemaGetQuery | None = None, options: CallOptions | None = None) -> DemoSchemaResponse:
        """Demo Schema"""

    @overload
    def get(self, path: Literal["/v1/matches/live/urls"], *, options: CallOptions | None = None) -> list[LiveUrl]:
        """Live Broadcast URLs"""

    @overload
    def get(self, path: Literal["/v1/matches/metadata"], *, query: BulkMetadataGetQuery | None = None, options: CallOptions | None = None) -> list[dict[str, Any]]:
        """Bulk Metadata"""

    @overload
    def get(self, path: Literal["/v1/matches/recently-fetched"], *, options: CallOptions | None = None) -> list[ClickhouseMatchInfo]:
        """Recently Fetched"""

    @overload
    def get(self, path: Literal["/v1/matches/{match_id}/live/url"], *, path_params: UrlGetPath, options: CallOptions | None = None) -> MatchSpectateResponse:
        """Live Broadcast URL"""

    @overload
    def get(self, path: Literal["/v1/matches/{match_id}/metadata"], *, path_params: MetadataGetPath, query: MetadataGetQuery | None = None, options: CallOptions | None = None) -> dict[str, Any]:
        """Metadata"""

    @overload
    def get(self, path: Literal["/v1/matches/{match_id}/metadata/raw"], *, path_params: MetadataRawGetPath, query: MetadataRawGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Metadata as Protobuf"""

    @overload
    def get(self, path: Literal["/v1/matches/{match_id}/salts"], *, path_params: SaltsGetPath, query: SaltsGetQuery | None = None, options: CallOptions | None = None) -> MatchSaltsResponse:
        """Salts"""

    @overload
    def get(self, path: Literal["/v1/patches"], *, options: CallOptions | None = None) -> list[Patch]:
        """Notes"""

    @overload
    def get(self, path: Literal["/v1/patches/big-days"], *, options: CallOptions | None = None) -> list[str]:
        """Big Days"""

    @overload
    def get(self, path: Literal["/v1/patron/steam-accounts"], *, options: CallOptions | None = None) -> ListSteamAccountsResponse:
        """List Prioritized Steam Accounts"""

    @overload
    def get(self, path: Literal["/v1/patron/steam-accounts/{account_id}/bot-friend"], *, path_params: BotFriendStatusGetPath, options: CallOptions | None = None) -> BotFriendStatus:
        """Prioritized Steam Account Bot Friend Status"""

    @overload
    def get(self, path: Literal["/v1/players/hero-stats"], *, query: PlayerHeroStatsGetQuery, options: CallOptions | None = None) -> list[HeroStats]:
        """Hero Stats"""

    @overload
    def get(self, path: Literal["/v1/players/mmr"], *, query: MmrGetQuery, options: CallOptions | None = None) -> list[MMRHistory]:
        """Batch MMR (Deprecated)"""

    @overload
    def get(self, path: Literal["/v1/players/mmr/distribution"], *, query: MmrDistributionGetQuery | None = None, options: CallOptions | None = None) -> list[DistributionEntry]:
        """MMR Distribution (Deprecated)"""

    @overload
    def get(self, path: Literal["/v1/players/mmr/distribution/{hero_id}"], *, path_params: HeroMmrDistributionGetPath, query: HeroMmrDistributionGetQuery | None = None, options: CallOptions | None = None) -> list[DistributionEntry]:
        """Hero MMR Distribution (Deprecated)"""

    @overload
    def get(self, path: Literal["/v1/players/mmr/{hero_id}"], *, path_params: HeroMmrGetPath, query: HeroMmrGetQuery, options: CallOptions | None = None) -> list[MMRHistory]:
        """Batch Hero MMR (Deprecated)"""

    @overload
    def get(self, path: Literal["/v1/players/rank"], *, query: RankBatchGetQuery, options: CallOptions | None = None) -> list[AccountRank]:
        """Batch Rank"""

    @overload
    def get(self, path: Literal["/v1/players/rank-predict/image"], *, query: RankPredictAvgImageGetQuery, options: CallOptions | None = None) -> bytes:
        """Rank Predict Avg Image (Deprecated)"""

    @overload
    def get(self, path: Literal["/v1/players/rank/distribution"], *, query: RankDistributionGetQuery | None = None, options: CallOptions | None = None) -> list[RankDistributionEntry]:
        """Rank Distribution"""

    @overload
    def get(self, path: Literal["/v1/players/rank/image"], *, query: RankAvgImageGetQuery, options: CallOptions | None = None) -> bytes:
        """Rank Avg Image"""

    @overload
    def get(self, path: Literal["/v1/players/steam"], *, query: SteamGetQuery, options: CallOptions | None = None) -> list[SteamProfile]:
        """Batch Steam Profile"""

    @overload
    def get(self, path: Literal["/v1/players/steam-search"], *, query: SteamSearchGetQuery, options: CallOptions | None = None) -> list[SteamProfile]:
        """Steam Profile Search"""

    @overload
    def get(self, path: Literal["/v1/players/{account_id}/enemy-stats"], *, path_params: EnemyStatsGetPath, query: EnemyStatsGetQuery | None = None, options: CallOptions | None = None) -> list[EnemyStats]:
        """Enemy Stats"""

    @overload
    def get(self, path: Literal["/v1/players/{account_id}/ingest-status"], *, path_params: IngestStatusGetPath, options: CallOptions | None = None) -> IngestStatusResponse:
        """Ingest Status"""

    @overload
    def get(self, path: Literal["/v1/players/{account_id}/match-history"], *, path_params: MatchHistoryGetPath, query: MatchHistoryGetQuery | None = None, options: CallOptions | None = None) -> list[PlayerMatchHistoryEntry]:
        """Match History"""

    @overload
    def get(self, path: Literal["/v1/players/{account_id}/mate-stats"], *, path_params: MateStatsGetPath, query: MateStatsGetQuery | None = None, options: CallOptions | None = None) -> list[MateStats]:
        """Mate Stats"""

    @overload
    def get(self, path: Literal["/v1/players/{account_id}/mmr-history"], *, path_params: MmrHistoryGetPath, options: CallOptions | None = None) -> list[MMRHistory]:
        """MMR History (Deprecated)"""

    @overload
    def get(self, path: Literal["/v1/players/{account_id}/mmr-history/{hero_id}"], *, path_params: HeroMmrHistoryGetPath, options: CallOptions | None = None) -> list[MMRHistory]:
        """Hero MMR History (Deprecated)"""

    @overload
    def get(self, path: Literal["/v1/players/{account_id}/rank"], *, path_params: RankGetPath, options: CallOptions | None = None) -> RankResponse:
        """Rank"""

    @overload
    def get(self, path: Literal["/v1/players/{account_id}/rank-predict"], *, path_params: RankPredictGetPath, options: CallOptions | None = None) -> RankResponse:
        """Rank Predict (Deprecated)"""

    @overload
    def get(self, path: Literal["/v1/players/{account_id}/rank-predict/image"], *, path_params: RankPredictImageGetPath, query: RankPredictImageGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Rank Predict Image (Deprecated)"""

    @overload
    def get(self, path: Literal["/v1/players/{account_id}/rank/image"], *, path_params: RankImageGetPath, query: RankImageGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Rank Image"""

    @overload
    def get(self, path: Literal["/v1/sql"], *, query: SqlGetQuery, options: CallOptions | None = None) -> str:
        """Query"""

    @overload
    def get(self, path: Literal["/v1/sql/tables"], *, options: CallOptions | None = None) -> list[str]:
        """List Tables"""

    @overload
    def get(self, path: Literal["/v1/sql/tables/{table}/schema"], *, path_params: TableSchemaGetPath, options: CallOptions | None = None) -> dict[str, str]:
        """Table Schema"""

    @overload
    def get(self, path: Literal["/v2/patches"], *, options: CallOptions | None = None) -> list[FeedItem]:
        """Notes"""

    def get(self, path: str, *, path_params: Any = None, query: Any = None, options: Any = None) -> Any:
        return self._request_get(path, path_params, query, options)

    def _request_get(self, path: str, path_params: Any, query: Any, options: Any) -> Any:
        raise NotImplementedError


class AsyncTypedGetMixin:
    """Async counterpart of TypedGetMixin."""

    @overload
    async def get(self, path: Literal["/v1/analytics/ability-max-first-stats"], *, query: AbilityMaxFirstStatsGetQuery, options: CallOptions | None = None) -> list[AnalyticsAbilityMaxFirstStats]:
        """Ability Max First Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/ability-order-stats"], *, query: AbilityOrderStatsGetQuery, options: CallOptions | None = None) -> list[AnalyticsAbilityOrderStats]:
        """Ability Order Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/ability-order-tree"], *, query: AbilityOrderTreeGetQuery, options: CallOptions | None = None) -> list[AnalyticsAbilityOrderTreeNode]:
        """Ability Order Tree"""

    @overload
    async def get(self, path: Literal["/v1/analytics/badge-distribution"], *, query: BadgeDistributionGetQuery | None = None, options: CallOptions | None = None) -> list[BadgeDistribution]:
        """Badge Distribution"""

    @overload
    async def get(self, path: Literal["/v1/analytics/buff-stats"], *, query: BuffStatsGetQuery | None = None, options: CallOptions | None = None) -> list[AnalyticsBuffStats]:
        """Buff Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/build-item-stats"], *, query: BuildItemStatsGetQuery | None = None, options: CallOptions | None = None) -> list[BuildItemStats]:
        """Build Item Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/game-stats"], *, query: GameStatsGetQuery | None = None, options: CallOptions | None = None) -> list[AnalyticsGameStats]:
        """Game Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/hero-ban-stats"], *, query: HeroBanStatsGetQuery | None = None, options: CallOptions | None = None) -> list[HeroBanStats]:
        """Hero Ban Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/hero-build-stats/{hero_id}"], *, path_params: HeroBuildStatsGetPath, query: HeroBuildStatsGetQuery | None = None, options: CallOptions | None = None) -> list[HeroBuildStats]:
        """Hero Build Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/hero-comb-stats"], *, query: HeroCombStatsGetQuery | None = None, options: CallOptions | None = None) -> list[HeroCombStats]:
        """Hero Comb Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/hero-counter-stats"], *, query: HeroCountersStatsGetQuery | None = None, options: CallOptions | None = None) -> list[HeroCounterStats]:
        """Hero Counter Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/hero-stats"], *, query: HeroStatsGetQuery | None = None, options: CallOptions | None = None) -> list[AnalyticsHeroStats]:
        """Hero Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/hero-swap-stats"], *, query: HeroSwapStatsGetQuery | None = None, options: CallOptions | None = None) -> list[HeroSwapStats]:
        """Hero Swap Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/hero-synergy-stats"], *, query: HeroSynergiesStatsGetQuery | None = None, options: CallOptions | None = None) -> list[HeroSynergyStats]:
        """Hero Synergy Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/item-flow-stats"], *, query: ItemFlowStatsGetQuery | None = None, options: CallOptions | None = None) -> ItemFlowStats:
        """Item Flow Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/item-permutation-stats"], *, query: ItemPermutationStatsGetQuery | None = None, options: CallOptions | None = None) -> list[ItemPermutationStats]:
        """Item Permutation Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/item-stats"], *, query: ItemStatsGetQuery | None = None, options: CallOptions | None = None) -> list[ItemStats]:
        """Item Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/kill-death-stats"], *, query: KillDeathStatsGetQuery | None = None, options: CallOptions | None = None) -> list[KillDeathStats]:
        """Kill Death Stats"""

    @overload
    async def get(self, path: Literal["/v1/analytics/lane-matchup-stats"], *, query: LaneMatchupStatsGetQuery | None = None, options: CallOptions | None = None) -> list[LaneMatchupStats]:
        """Lane Matchup Stats (Subject to Change)"""

    @overload
    async def get(self, path: Literal["/v1/analytics/lane-soul-curve"], *, query: LaneSoulCurveGetQuery | None = None, options: CallOptions | None = None) -> list[LaneSoulCurve]:
        """Lane Soul Curve (Subject to Change)"""

    @overload
    async def get(self, path: Literal["/v1/analytics/player-performance-curve"], *, query: PlayerPerformanceCurveGetQuery | None = None, options: CallOptions | None = None) -> list[PlayerPerformanceCurvePoint]:
        """Player Performance Curve"""

    @overload
    async def get(self, path: Literal["/v1/analytics/player-stats/metrics"], *, query: PlayerStatsMetricsGetQuery | None = None, options: CallOptions | None = None) -> HashMap:
        """Player Stats Metrics"""

    @overload
    async def get(self, path: Literal["/v1/analytics/scoreboards/heroes"], *, query: HeroScoreboardGetQuery, options: CallOptions | None = None) -> list[HeroEntry]:
        """Hero Scoreboard"""

    @overload
    async def get(self, path: Literal["/v1/analytics/scoreboards/players"], *, query: PlayerScoreboardGetQuery, options: CallOptions | None = None) -> list[PlayerEntry]:
        """Player Scoreboard"""

    @overload
    async def get(self, path: Literal["/v1/assets/accolades"], *, query: ListAccoladesGetQuery | None = None, options: CallOptions | None = None) -> list[Accolade]:
        """List Accolades"""

    @overload
    async def get(self, path: Literal["/v1/assets/accolades/by-name/{name}"], *, path_params: GetAccoladeByNameGetPath, query: GetAccoladeByNameGetQuery | None = None, options: CallOptions | None = None) -> Accolade:
        """Get Accolade By Name"""

    @overload
    async def get(self, path: Literal["/v1/assets/accolades/{accolade_id}"], *, path_params: GetAccoladeGetPath, query: GetAccoladeGetQuery | None = None, options: CallOptions | None = None) -> Accolade:
        """Get Accolade"""

    @overload
    async def get(self, path: Literal["/v1/assets/build-tags"], *, query: ListBuildTagsGetQuery | None = None, options: CallOptions | None = None) -> list[BuildTag]:
        """List Build Tags"""

    @overload
    async def get(self, path: Literal["/v1/assets/build-tags/by-name/{name}"], *, path_params: GetBuildTagByNameGetPath, query: GetBuildTagByNameGetQuery | None = None, options: CallOptions | None = None) -> BuildTag:
        """Get Build Tag By Name"""

    @overload
    async def get(self, path: Literal["/v1/assets/build-tags/{build_tag_id}"], *, path_params: GetBuildTagGetPath, query: GetBuildTagGetQuery | None = None, options: CallOptions | None = None) -> BuildTag:
        """Get Build Tag"""

    @overload
    async def get(self, path: Literal["/v1/assets/client-versions"], *, options: CallOptions | None = None) -> list[int]:
        """List Client Versions"""

    @overload
    async def get(self, path: Literal["/v1/assets/colors"], *, query: ListColorsGetQuery | None = None, options: CallOptions | None = None) -> dict[str, Color]:
        """List Colors"""

    @overload
    async def get(self, path: Literal["/v1/assets/convars"], *, query: ListConvarsGetQuery | None = None, options: CallOptions | None = None) -> dict[str, Convar]:
        """List Convars"""

    @overload
    async def get(self, path: Literal["/v1/assets/convars/{name}"], *, path_params: GetConvarGetPath, query: GetConvarGetQuery | None = None, options: CallOptions | None = None) -> Convar:
        """Get Convar"""

    @overload
    async def get(self, path: Literal["/v1/assets/fonts"], *, options: CallOptions | None = None) -> Any:
        """Fonts Index"""

    @overload
    async def get(self, path: Literal["/v1/assets/generic-data"], *, query: GetGenericDataGetQuery | None = None, options: CallOptions | None = None) -> GenericData:
        """Get Generic Data"""

    @overload
    async def get(self, path: Literal["/v1/assets/heroes"], *, query: ListHeroesGetQuery | None = None, options: CallOptions | None = None) -> list[Hero]:
        """List Heroes"""

    @overload
    async def get(self, path: Literal["/v1/assets/heroes/by-name/{name}"], *, path_params: GetHeroByNameGetPath, query: GetHeroByNameGetQuery | None = None, options: CallOptions | None = None) -> Hero:
        """Get Hero By Name"""

    @overload
    async def get(self, path: Literal["/v1/assets/heroes/{hero_id}"], *, path_params: GetHeroGetPath, query: GetHeroGetQuery | None = None, options: CallOptions | None = None) -> Hero:
        """Get Hero"""

    @overload
    async def get(self, path: Literal["/v1/assets/icons"], *, options: CallOptions | None = None) -> Any:
        """Icons Index"""

    @overload
    async def get(self, path: Literal["/v1/assets/images"], *, options: CallOptions | None = None) -> Any:
        """Images Index"""

    @overload
    async def get(self, path: Literal["/v1/assets/items"], *, query: ListItemsGetQuery | None = None, options: CallOptions | None = None) -> list[Item]:
        """List Items"""

    @overload
    async def get(self, path: Literal["/v1/assets/items/by-hero-id/{id}"], *, path_params: GetItemsByHeroIdGetPath, query: GetItemsByHeroIdGetQuery | None = None, options: CallOptions | None = None) -> list[Item]:
        """List Items By Hero"""

    @overload
    async def get(self, path: Literal["/v1/assets/items/by-slot-type/{slot_type}"], *, path_params: GetItemsBySlotTypeGetPath, query: GetItemsBySlotTypeGetQuery | None = None, options: CallOptions | None = None) -> list[Item]:
        """List Items By Slot Type"""

    @overload
    async def get(self, path: Literal["/v1/assets/items/by-type/{type}"], *, path_params: GetItemsByTypeGetPath, query: GetItemsByTypeGetQuery | None = None, options: CallOptions | None = None) -> list[Item]:
        """List Items By Type"""

    @overload
    async def get(self, path: Literal["/v1/assets/items/{id_or_class_name}"], *, path_params: GetItemGetPath, query: GetItemGetQuery | None = None, options: CallOptions | None = None) -> Item:
        """Get Item"""

    @overload
    async def get(self, path: Literal["/v1/assets/loot-tables"], *, query: ListLootTablesGetQuery | None = None, options: CallOptions | None = None) -> dict[str, LootTable]:
        """List Loot Tables"""

    @overload
    async def get(self, path: Literal["/v1/assets/map"], *, query: GetMapGetQuery | None = None, options: CallOptions | None = None) -> MapData:
        """Map"""

    @overload
    async def get(self, path: Literal["/v1/assets/misc-entities"], *, query: ListMiscEntitiesGetQuery | None = None, options: CallOptions | None = None) -> list[MiscEntity]:
        """List Misc Entities"""

    @overload
    async def get(self, path: Literal["/v1/assets/misc-entities/{id_or_classname}"], *, path_params: GetMiscEntityGetPath, query: GetMiscEntityGetQuery | None = None, options: CallOptions | None = None) -> MiscEntity:
        """Get Misc Entity"""

    @overload
    async def get(self, path: Literal["/v1/assets/models"], *, options: CallOptions | None = None) -> Any:
        """Models Index"""

    @overload
    async def get(self, path: Literal["/v1/assets/modifiers"], *, query: ListModifiersGetQuery | None = None, options: CallOptions | None = None) -> list[Modifier]:
        """List Modifiers"""

    @overload
    async def get(self, path: Literal["/v1/assets/modifiers/{id_or_classname}"], *, path_params: GetModifierGetPath, query: GetModifierGetQuery | None = None, options: CallOptions | None = None) -> Modifier:
        """Get Modifier"""

    @overload
    async def get(self, path: Literal["/v1/assets/npc-units"], *, query: ListNpcUnitsGetQuery | None = None, options: CallOptions | None = None) -> list[NpcUnit]:
        """List NPC Units"""

    @overload
    async def get(self, path: Literal["/v1/assets/npc-units/{id_or_classname}"], *, path_params: GetNpcUnitGetPath, query: GetNpcUnitGetQuery | None = None, options: CallOptions | None = None) -> NpcUnit:
        """Get NPC Unit"""

    @overload
    async def get(self, path: Literal["/v1/assets/ranked-seasons"], *, query: ListRankedSeasonsGetQuery | None = None, options: CallOptions | None = None) -> list[RankedSeason]:
        """List Ranked Seasons"""

    @overload
    async def get(self, path: Literal["/v1/assets/ranks"], *, query: ListRanksGetQuery | None = None, options: CallOptions | None = None) -> list[Rank]:
        """List Ranks"""

    @overload
    async def get(self, path: Literal["/v1/assets/ranks/{tier}"], *, path_params: GetRankGetPath, query: GetRankGetQuery | None = None, options: CallOptions | None = None) -> Rank:
        """Get Rank"""

    @overload
    async def get(self, path: Literal["/v1/assets/ranks/{tier}/{subrank}/image"], *, path_params: SubrankImageGetPath, query: SubrankImageGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Rank Subrank Image"""

    @overload
    async def get(self, path: Literal["/v1/assets/sounds"], *, options: CallOptions | None = None) -> Any:
        """Sounds Index"""

    @overload
    async def get(self, path: Literal["/v1/assets/steam-info"], *, query: GetSteamInfoGetQuery | None = None, options: CallOptions | None = None) -> SteamInfo:
        """Get Steam Info"""

    @overload
    async def get(self, path: Literal["/v1/assets/steam-info/all"], *, options: CallOptions | None = None) -> list[SteamInfo]:
        """Get All Steam Infos"""

    @overload
    async def get(self, path: Literal["/v1/builds"], *, query: SearchBuildsGetQuery | None = None, options: CallOptions | None = None) -> list[Build]:
        """Search"""

    @overload
    async def get(self, path: Literal["/v1/builds/by-author/{account_id}"], *, path_params: FetchBuildsByAuthorLiveGetPath, options: CallOptions | None = None) -> list[Build]:
        """Fetch Live by Author"""

    @overload
    async def get(self, path: Literal["/v1/builds/{hero_id}/{build_id}"], *, path_params: FetchBuildLiveGetPath, query: FetchBuildLiveGetQuery | None = None, options: CallOptions | None = None) -> Build:
        """Fetch Live"""

    @overload
    async def get(self, path: Literal["/v1/commands/resolve"], *, query: CommandResolveGetQuery, options: CallOptions | None = None) -> str:
        """Resolve Command"""

    @overload
    async def get(self, path: Literal["/v1/commands/variables/available"], *, options: CallOptions | None = None) -> list[VariableDescription]:
        """Available Variables"""

    @overload
    async def get(self, path: Literal["/v1/commands/variables/resolve"], *, query: VariablesResolveGetQuery, options: CallOptions | None = None) -> dict[str, str]:
        """Resolve Variables"""

    @overload
    async def get(self, path: Literal["/v1/commands/widgets/versions"], *, options: CallOptions | None = None) -> dict[str, int]:
        """Widget Versions"""

    @overload
    async def get(self, path: Literal["/v1/crosshair/code/image"], *, query: CodeImageGetQuery, options: CallOptions | None = None) -> bytes:
        """Crosshair Code Image"""

    @overload
    async def get(self, path: Literal["/v1/crosshair/code/settings"], *, query: CodeSettingsGetQuery, options: CallOptions | None = None) -> Settings:
        """Crosshair Code Settings"""

    @overload
    async def get(self, path: Literal["/v1/crosshair/settings/code"], *, query: SettingsCodeGetQuery | None = None, options: CallOptions | None = None) -> CrosshairCode:
        """Crosshair Settings Code"""

    @overload
    async def get(self, path: Literal["/v1/crosshair/settings/image"], *, query: SettingsImageGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Crosshair Settings Image"""

    @overload
    async def get(self, path: Literal["/v1/graphql"], *, options: CallOptions | None = None) -> str:
        """GraphQL Playground"""

    @overload
    async def get(self, path: Literal["/v1/info"], *, options: CallOptions | None = None) -> APIInfo:
        """API Info"""

    @overload
    async def get(self, path: Literal["/v1/info/health"], *, options: CallOptions | None = None) -> Status:
        """Health Check"""

    @overload
    async def get(self, path: Literal["/v1/leaderboard/{region}"], *, path_params: LeaderboardGetPath, query: LeaderboardGetQuery | None = None, options: CallOptions | None = None) -> Leaderboard:
        """Leaderboard"""

    @overload
    async def get(self, path: Literal["/v1/leaderboard/{region}/raw"], *, path_params: LeaderboardRawGetPath, query: LeaderboardRawGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Leaderboard as Protobuf"""

    @overload
    async def get(self, path: Literal["/v1/leaderboard/{region}/{hero_id}"], *, path_params: LeaderboardHeroGetPath, query: LeaderboardHeroGetQuery | None = None, options: CallOptions | None = None) -> Leaderboard:
        """Hero Leaderboard"""

    @overload
    async def get(self, path: Literal["/v1/leaderboard/{region}/{hero_id}/raw"], *, path_params: LeaderboardHeroRawGetPath, query: LeaderboardHeroRawGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Hero Leaderboard as Protobuf"""

    @overload
    async def get(self, path: Literal["/v1/matches/active"], *, query: ActiveMatchesGetQuery | None = None, options: CallOptions | None = None) -> list[ActiveMatch]:
        """Active"""

    @overload
    async def get(self, path: Literal["/v1/matches/active/raw"], *, options: CallOptions | None = None) -> bytes:
        """Active as Protobuf"""

    @overload
    async def get(self, path: Literal["/v1/matches/custom/{party_id}/match-id"], *, path_params: GetCustomGetPath, options: CallOptions | None = None) -> GetCustomMatchIdResponse:
        """Get Match ID"""

    @overload
    async def get(self, path: Literal["/v1/matches/demo/live/query"], *, query: LiveQueryGetQuery, options: CallOptions | None = None) -> str:
        """Live Demo Query (SSE)"""

    @overload
    async def get(self, path: Literal["/v1/matches/demo/query/{job_id}"], *, path_params: StatusGetPath, options: CallOptions | None = None) -> DemoQueryStatusResponse:
        """Demo Query Status"""

    @overload
    async def get(self, path: Literal["/v1/matches/demo/schema"], *, query: SchemaGetQuery | None = None, options: CallOptions | None = None) -> DemoSchemaResponse:
        """Demo Schema"""

    @overload
    async def get(self, path: Literal["/v1/matches/live/urls"], *, options: CallOptions | None = None) -> list[LiveUrl]:
        """Live Broadcast URLs"""

    @overload
    async def get(self, path: Literal["/v1/matches/metadata"], *, query: BulkMetadataGetQuery | None = None, options: CallOptions | None = None) -> list[dict[str, Any]]:
        """Bulk Metadata"""

    @overload
    async def get(self, path: Literal["/v1/matches/recently-fetched"], *, options: CallOptions | None = None) -> list[ClickhouseMatchInfo]:
        """Recently Fetched"""

    @overload
    async def get(self, path: Literal["/v1/matches/{match_id}/live/url"], *, path_params: UrlGetPath, options: CallOptions | None = None) -> MatchSpectateResponse:
        """Live Broadcast URL"""

    @overload
    async def get(self, path: Literal["/v1/matches/{match_id}/metadata"], *, path_params: MetadataGetPath, query: MetadataGetQuery | None = None, options: CallOptions | None = None) -> dict[str, Any]:
        """Metadata"""

    @overload
    async def get(self, path: Literal["/v1/matches/{match_id}/metadata/raw"], *, path_params: MetadataRawGetPath, query: MetadataRawGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Metadata as Protobuf"""

    @overload
    async def get(self, path: Literal["/v1/matches/{match_id}/salts"], *, path_params: SaltsGetPath, query: SaltsGetQuery | None = None, options: CallOptions | None = None) -> MatchSaltsResponse:
        """Salts"""

    @overload
    async def get(self, path: Literal["/v1/patches"], *, options: CallOptions | None = None) -> list[Patch]:
        """Notes"""

    @overload
    async def get(self, path: Literal["/v1/patches/big-days"], *, options: CallOptions | None = None) -> list[str]:
        """Big Days"""

    @overload
    async def get(self, path: Literal["/v1/patron/steam-accounts"], *, options: CallOptions | None = None) -> ListSteamAccountsResponse:
        """List Prioritized Steam Accounts"""

    @overload
    async def get(self, path: Literal["/v1/patron/steam-accounts/{account_id}/bot-friend"], *, path_params: BotFriendStatusGetPath, options: CallOptions | None = None) -> BotFriendStatus:
        """Prioritized Steam Account Bot Friend Status"""

    @overload
    async def get(self, path: Literal["/v1/players/hero-stats"], *, query: PlayerHeroStatsGetQuery, options: CallOptions | None = None) -> list[HeroStats]:
        """Hero Stats"""

    @overload
    async def get(self, path: Literal["/v1/players/mmr"], *, query: MmrGetQuery, options: CallOptions | None = None) -> list[MMRHistory]:
        """Batch MMR (Deprecated)"""

    @overload
    async def get(self, path: Literal["/v1/players/mmr/distribution"], *, query: MmrDistributionGetQuery | None = None, options: CallOptions | None = None) -> list[DistributionEntry]:
        """MMR Distribution (Deprecated)"""

    @overload
    async def get(self, path: Literal["/v1/players/mmr/distribution/{hero_id}"], *, path_params: HeroMmrDistributionGetPath, query: HeroMmrDistributionGetQuery | None = None, options: CallOptions | None = None) -> list[DistributionEntry]:
        """Hero MMR Distribution (Deprecated)"""

    @overload
    async def get(self, path: Literal["/v1/players/mmr/{hero_id}"], *, path_params: HeroMmrGetPath, query: HeroMmrGetQuery, options: CallOptions | None = None) -> list[MMRHistory]:
        """Batch Hero MMR (Deprecated)"""

    @overload
    async def get(self, path: Literal["/v1/players/rank"], *, query: RankBatchGetQuery, options: CallOptions | None = None) -> list[AccountRank]:
        """Batch Rank"""

    @overload
    async def get(self, path: Literal["/v1/players/rank-predict/image"], *, query: RankPredictAvgImageGetQuery, options: CallOptions | None = None) -> bytes:
        """Rank Predict Avg Image (Deprecated)"""

    @overload
    async def get(self, path: Literal["/v1/players/rank/distribution"], *, query: RankDistributionGetQuery | None = None, options: CallOptions | None = None) -> list[RankDistributionEntry]:
        """Rank Distribution"""

    @overload
    async def get(self, path: Literal["/v1/players/rank/image"], *, query: RankAvgImageGetQuery, options: CallOptions | None = None) -> bytes:
        """Rank Avg Image"""

    @overload
    async def get(self, path: Literal["/v1/players/steam"], *, query: SteamGetQuery, options: CallOptions | None = None) -> list[SteamProfile]:
        """Batch Steam Profile"""

    @overload
    async def get(self, path: Literal["/v1/players/steam-search"], *, query: SteamSearchGetQuery, options: CallOptions | None = None) -> list[SteamProfile]:
        """Steam Profile Search"""

    @overload
    async def get(self, path: Literal["/v1/players/{account_id}/enemy-stats"], *, path_params: EnemyStatsGetPath, query: EnemyStatsGetQuery | None = None, options: CallOptions | None = None) -> list[EnemyStats]:
        """Enemy Stats"""

    @overload
    async def get(self, path: Literal["/v1/players/{account_id}/ingest-status"], *, path_params: IngestStatusGetPath, options: CallOptions | None = None) -> IngestStatusResponse:
        """Ingest Status"""

    @overload
    async def get(self, path: Literal["/v1/players/{account_id}/match-history"], *, path_params: MatchHistoryGetPath, query: MatchHistoryGetQuery | None = None, options: CallOptions | None = None) -> list[PlayerMatchHistoryEntry]:
        """Match History"""

    @overload
    async def get(self, path: Literal["/v1/players/{account_id}/mate-stats"], *, path_params: MateStatsGetPath, query: MateStatsGetQuery | None = None, options: CallOptions | None = None) -> list[MateStats]:
        """Mate Stats"""

    @overload
    async def get(self, path: Literal["/v1/players/{account_id}/mmr-history"], *, path_params: MmrHistoryGetPath, options: CallOptions | None = None) -> list[MMRHistory]:
        """MMR History (Deprecated)"""

    @overload
    async def get(self, path: Literal["/v1/players/{account_id}/mmr-history/{hero_id}"], *, path_params: HeroMmrHistoryGetPath, options: CallOptions | None = None) -> list[MMRHistory]:
        """Hero MMR History (Deprecated)"""

    @overload
    async def get(self, path: Literal["/v1/players/{account_id}/rank"], *, path_params: RankGetPath, options: CallOptions | None = None) -> RankResponse:
        """Rank"""

    @overload
    async def get(self, path: Literal["/v1/players/{account_id}/rank-predict"], *, path_params: RankPredictGetPath, options: CallOptions | None = None) -> RankResponse:
        """Rank Predict (Deprecated)"""

    @overload
    async def get(self, path: Literal["/v1/players/{account_id}/rank-predict/image"], *, path_params: RankPredictImageGetPath, query: RankPredictImageGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Rank Predict Image (Deprecated)"""

    @overload
    async def get(self, path: Literal["/v1/players/{account_id}/rank/image"], *, path_params: RankImageGetPath, query: RankImageGetQuery | None = None, options: CallOptions | None = None) -> bytes:
        """Rank Image"""

    @overload
    async def get(self, path: Literal["/v1/sql"], *, query: SqlGetQuery, options: CallOptions | None = None) -> str:
        """Query"""

    @overload
    async def get(self, path: Literal["/v1/sql/tables"], *, options: CallOptions | None = None) -> list[str]:
        """List Tables"""

    @overload
    async def get(self, path: Literal["/v1/sql/tables/{table}/schema"], *, path_params: TableSchemaGetPath, options: CallOptions | None = None) -> dict[str, str]:
        """Table Schema"""

    @overload
    async def get(self, path: Literal["/v2/patches"], *, options: CallOptions | None = None) -> list[FeedItem]:
        """Notes"""

    async def get(self, path: str, *, path_params: Any = None, query: Any = None, options: Any = None) -> Any:
        return await self._request_get(path, path_params, query, options)

    async def _request_get(self, path: str, path_params: Any, query: Any, options: Any) -> Any:
        raise NotImplementedError
