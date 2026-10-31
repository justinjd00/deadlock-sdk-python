"""Generated from https://api.deadlock-api.com/openapi.json by scripts/generate.py. Do not edit by hand."""

# ruff: noqa
# fmt: off
from __future__ import annotations

from typing import Any, Literal, TypedDict

from typing_extensions import NotRequired, TypeAlias

__all__ = [
    "APIInfo",
    "Ability",
    "AbilityActivation",
    "AbilityDescription",
    "AbilityImbue",
    "AbilitySectionType",
    "AbilityTooltipDetails",
    "AbilityType",
    "AbilityVideos",
    "Accolade",
    "AccountRank",
    "ActiveMatch",
    "ActiveMatchGameMode",
    "ActiveMatchMode",
    "ActiveMatchPlayer",
    "ActiveMatchTeam",
    "ActiveMatchTeamStats",
    "AddSteamAccountRequest",
    "AnalyticsAbilityMaxFirstStats",
    "AnalyticsAbilityOrderStats",
    "AnalyticsAbilityOrderTreeNode",
    "AnalyticsBuffStats",
    "AnalyticsGameStats",
    "AnalyticsHeroStats",
    "BadgeDistribution",
    "BotFriendStatus",
    "BreakablePowerupLootParams",
    "Build",
    "BuildHero",
    "BuildHeroDetails",
    "BuildHeroDetailsAbilityOrder",
    "BuildHeroDetailsAbilityOrderCurrencyChange",
    "BuildHeroDetailsCategory",
    "BuildHeroDetailsCategoryAbility",
    "BuildItemStats",
    "BuildTag",
    "ClickhouseMatchInfo",
    "ClickhouseSalts",
    "Color",
    "ColorGradientStop",
    "ColumnSchema",
    "Convar",
    "ConvarType",
    "CorruptedItemImages",
    "CorruptedItemInfo",
    "CorruptedPenalty",
    "CorruptedPenaltyEffect",
    "CorruptedTooltipBackers",
    "CreateCustomRequest",
    "CreateCustomResponse",
    "CrosshairCode",
    "Curve",
    "CurveOrFloat",
    "DamageFlash",
    "DeleteSteamAccountResponse",
    "DemoQueryJobResponse",
    "DemoQueryRequest",
    "DemoQueryStatusResponse",
    "DemoSchemaResponse",
    "DependantAbilities",
    "DistributionEntry",
    "DraftBucket",
    "DraftBuckets",
    "EnemyStats",
    "FeedItem",
    "FeedbackKind",
    "FeedbackSubmission",
    "FeedbackTarget",
    "FlashData",
    "ForumPatch",
    "GameMode",
    "GenericData",
    "GetCustomMatchIdResponse",
    "GlitchSettings",
    "HashMap",
    "HashMap_HeroItemType_String",
    "HashMap_ItemSlotType_ItemSlotInfo",
    "HashMap_ItemSlotType_Vec_MapModCostBonus",
    "HashMap_ItemSlotType_Vec_PurchaseBonus",
    "HashMap_String_LevelInfo",
    "HashMap_String_Option_DraftBucketing",
    "HashMap_String_ScalingStat",
    "HashMap_String_String",
    "HashMap_String_f64",
    "Hero",
    "HeroBanStats",
    "HeroBuildStats",
    "HeroColors",
    "HeroCombStats",
    "HeroCounterStats",
    "HeroDescription",
    "HeroDevelopmentState",
    "HeroEntry",
    "HeroImages",
    "HeroPhysics",
    "HeroPopularItem",
    "HeroPopularItems",
    "HeroStats",
    "HeroStatsUI",
    "HeroStatsUIDisplay",
    "HeroSwapStats",
    "HeroSynergyStats",
    "HeroType",
    "HorizontalRecoil",
    "ImagePair",
    "IngestLiveUrl",
    "IngestStatusResponse",
    "Item",
    "ItemDraftRound",
    "ItemDraftRoundPerGameRound",
    "ItemFlowEdge",
    "ItemFlowLeaveOneOut",
    "ItemFlowNode",
    "ItemFlowStats",
    "ItemFlowSummary",
    "ItemGroup",
    "ItemPermutationStats",
    "ItemProperty",
    "ItemSlotType",
    "ItemStats",
    "ItemTooltipBacker",
    "ItemTooltipBackers",
    "ItemType",
    "JobStatus",
    "KillDeathStats",
    "LaneInfo",
    "LaneMatchupStat",
    "LaneMatchupStats",
    "LaneSoulCurve",
    "LaneStatCurve",
    "LastRankedMatch",
    "Leaderboard",
    "LeaderboardEntry",
    "ListSteamAccountsResponse",
    "LiveUrl",
    "LootEntry",
    "LootTable",
    "MMRHistory",
    "MapData",
    "MapDistrict",
    "MapEntities",
    "MapEntity",
    "MapImages",
    "MatchPlayer",
    "MatchSaltsResponse",
    "MatchSpectateResponse",
    "MateStats",
    "MiniMapOffsets",
    "MiscEntity",
    "Modifier",
    "ModifierValue",
    "NeutralCamp",
    "NeutralCampKind",
    "NewPlayerMetrics",
    "NpcUnit",
    "ObjectiveParams",
    "ObjectivePosition",
    "OutcomeToWeights",
    "OutputFormat",
    "Patch",
    "PatchCategory",
    "PatchGuid",
    "Pickup",
    "PlayerEntry",
    "PlayerMatchHistoryEntry",
    "PlayerPerformanceCurvePoint",
    "Rank",
    "RankDistributionEntry",
    "RankImages",
    "RankResponse",
    "RankedSeason",
    "RawAbilityUpgrade",
    "RawAbilityUpgradePropertyUpgrade",
    "RawCustomCrosshairSettings",
    "RawItemPropertyScaleFunctionSubclass",
    "RawItemWeaponInfoBulletSpeedCurve",
    "RawItemWeaponInfoBulletSpeedCurveSpline",
    "RawItemWeaponInfoInner",
    "RawWeaponInfoHorizontalRecoil",
    "RawWeaponInfoVerticalRecoil",
    "RecoilRange",
    "RegionMode",
    "RejuvParams",
    "ReplaceSteamAccountRequest",
    "RollType",
    "ScriptValues",
    "SeasonInterval",
    "ServerRegion",
    "Settings",
    "ShopSpiritStatsDisplay",
    "ShopStatDisplay",
    "ShopVitalityStatsDisplay",
    "ShopWeaponStatsDisplay",
    "SlotsSummary",
    "SourceLocation",
    "SpreadPenalty",
    "StartingStat",
    "StartingStats",
    "StatsDisplay",
    "StatsUsageFlag",
    "Status",
    "StatusServices",
    "SteamAccountListItem",
    "SteamAccountResponse",
    "SteamFriend",
    "SteamInfo",
    "SteamNews",
    "SteamProfile",
    "StreetBrawl",
    "Subclass_BulletResistModifier",
    "Subclass_EmpoweredModifierLevel",
    "Subclass_IntrinsicModifiers",
    "Subclass_ModifierDefinition",
    "Subclass_NeutralDamageGrowth",
    "Subclass_ObjectiveHealthGrowthPhase",
    "Subclass_ObjectiveRegen",
    "Subclass_RangedArmorModifier",
    "Subclass_TrooperDamageReduction",
    "TableSchemaResponse",
    "TableSize",
    "TeamModels",
    "TooltipDetailsBlock",
    "TooltipDetailsBlockProperty",
    "TooltipDetailsInfoSection",
    "Upgrade",
    "UpgradeDescription",
    "UpgradeProperty",
    "UpgradeTooltipImportantPropertyWithIcon",
    "UpgradeTooltipSection",
    "UpgradeTooltipSectionAttribute",
    "VariableCategory",
    "VariableDescription",
    "VerticalRecoil",
    "Viewport",
    "Weapon",
    "WeaponInfo",
    "ZiplanePath",
]


class APIInfo(TypedDict):
    fetched_matches_per_day: NotRequired[int | None]
    """The number of matches fetched in the last 24 hours."""
    table_sizes: NotRequired[dict[str, TableSize] | None]
    """The sizes of all tables in the database."""
    user_ingested_matches_last24h: NotRequired[int | None]
    """The number of matches ingested in the last 24 hours."""


class Ability(TypedDict):
    ability_type: NotRequired[AbilityType | None]
    behaviours: NotRequired[list[str] | None]
    boss_damage_scale: NotRequired[float | None]
    class_name: str
    dependant_abilities: NotRequired[list[str] | None]
    dependent_abilities: NotRequired[dict[str, DependantAbilities] | None]
    description: AbilityDescription
    grant_ammo_on_cast: NotRequired[bool | None]
    hero: NotRequired[int | None]
    heroes: NotRequired[list[int] | None]
    id: int
    image: NotRequired[str | None]
    image_webp: NotRequired[str | None]
    name: str
    properties: NotRequired[dict[str, ItemProperty] | None]
    start_trained: NotRequired[bool | None]
    tooltip_details: NotRequired[AbilityTooltipDetails | None]
    type: ItemType
    update_time: NotRequired[int | None]
    upgrades: NotRequired[list[RawAbilityUpgrade] | None]
    videos: NotRequired[AbilityVideos | None]
    weapon_info: NotRequired[RawItemWeaponInfoInner | None]


AbilityActivation: TypeAlias = "Literal[\"hold_toggle\", \"instant_cast\", \"on_button_is_down\", \"passive\", \"press\", \"press_toggle\", \"instant_cast_toggle\"]"


class AbilityDescription(TypedDict):
    active: NotRequired[str | None]
    desc: NotRequired[str | None]
    passive: NotRequired[str | None]
    quip: NotRequired[str | None]
    t1_desc: NotRequired[str | None]
    t2_desc: NotRequired[str | None]
    t3_desc: NotRequired[str | None]


AbilityImbue: TypeAlias = "Literal[\"imbue_active\", \"imbue_active_non_ult\", \"imbue_modifier_value\"]"


AbilitySectionType: TypeAlias = "Literal[\"innate\", \"active\", \"passive\"]"


class AbilityTooltipDetails(TypedDict):
    additional_header_properties: NotRequired[list[str] | None]
    info_sections: NotRequired[list[TooltipDetailsInfoSection] | None]


AbilityType: TypeAlias = "Literal[\"innate\", \"item\", \"signature\", \"ultimate\", \"weapon\", \"melee\", \"cosmetic\", \"held\"]"


class AbilityVideos(TypedDict):
    mp4: NotRequired[str | None]
    webm: NotRequired[str | None]


class Accolade(TypedDict):
    class_name: str
    description: str
    enabled_game_modes: NotRequired[list[str] | None]
    flavor_name: str
    id: int
    threshold_type: str
    tracked_stat_name: str


AccountRank: TypeAlias = "dict[str, Any]"


class ActiveMatch(TypedDict):
    compat_version: NotRequired[int | None]
    duration_s: NotRequired[int | None]
    game_mode: NotRequired[int | None]
    game_mode_parsed: NotRequired[ActiveMatchGameMode | None]
    game_mode_version: NotRequired[int | None]
    lobby_id: NotRequired[int | None]
    low_pri_pool: NotRequired[bool | None]
    match_id: NotRequired[int | None]
    match_mode: NotRequired[int | None]
    match_mode_parsed: NotRequired[ActiveMatchMode | None]
    match_score: NotRequired[int | None]
    net_worth_team_0: NotRequired[int | None]
    net_worth_team_1: NotRequired[int | None]
    objectives_mask_team0: NotRequired[int | None]
    objectives_mask_team1: NotRequired[int | None]
    open_spectator_slots: NotRequired[int | None]
    players: list[ActiveMatchPlayer]
    region_mode: NotRequired[int | None]
    region_mode_parsed: NotRequired[RegionMode | None]
    spectators: NotRequired[int | None]
    start_time: NotRequired[int | None]
    team_stats: list[ActiveMatchTeamStats]
    winning_team: NotRequired[int | None]
    winning_team_parsed: NotRequired[ActiveMatchTeam | None]


ActiveMatchGameMode: TypeAlias = "Literal[\"KECitadelGameModeInvalid\", \"KECitadelGameModeNormal\", \"KECitadelGameMode1v1Test\", \"KECitadelGameModeSandbox\", \"KECitadelGameModeStreetBrawl\"]"


ActiveMatchMode: TypeAlias = "Literal[\"Invalid\", \"Unranked\", \"PrivateLobby\", \"CoopBot\", \"Ranked\", \"ServerTest\", \"Tutorial\", \"HeroLabs\", \"NewPlayerPlacement\"]"


class ActiveMatchPlayer(TypedDict):
    abandoned: NotRequired[bool | None]
    account_id: NotRequired[int | None]
    hero_id: NotRequired[int | None]
    """See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    team: NotRequired[int | None]
    team_parsed: NotRequired[ActiveMatchTeam | None]


ActiveMatchTeam: TypeAlias = "Literal[\"Team0\", \"Team1\", \"Spectator\"]"


class ActiveMatchTeamStats(TypedDict):
    brawl_score: NotRequired[int | None]
    net_worth: NotRequired[int | None]
    objectives_mask: NotRequired[int | None]
    team: NotRequired[int | None]
    team_parsed: NotRequired[ActiveMatchTeam | None]


class AddSteamAccountRequest(TypedDict):
    """Request body for adding a Steam account"""
    steam_id3: int
    """Steam ID3 (32-bit unsigned integer format)"""


class AnalyticsAbilityMaxFirstStats(TypedDict):
    """The players who maxed one ability first, or (`ability_id` null) none."""
    ability_id: NotRequired[int | None]
    """The ability these players maxed first (unlocked and upgraded three times before any other), null for the players who maxed none. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    losses: int
    matches: int
    players: int
    """Distinct players, counted exactly."""
    wins: int


class AnalyticsAbilityOrderStats(TypedDict):
    abilities: list[int]
    """See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    avg_upgrade_times_s: list[float]
    """Average game time (in seconds) at which each upgrade in `abilities` was bought, index-aligned with `abilities`."""
    losses: int
    matches: int
    players: int
    total_assists: int
    total_deaths: int
    total_kills: int
    wins: int


class AnalyticsAbilityOrderTreeNode(TypedDict):
    """One node of the ability order tree: the players whose upgrade order starts with `abilities`."""
    abilities: list[int]
    """The order prefix: one entry per ability point spent, unlocks included. Its parent node is the prefix one entry shorter. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    avg_upgrade_time_s: float
    """Average game time (in seconds) at which the last upgrade in `abilities` was bought."""
    losses: int
    matches: int
    players: int
    """Distinct players, counted exactly."""
    total_assists: int
    total_deaths: int
    total_kills: int
    wins: int


class AnalyticsBuffStats(TypedDict):
    avg_first_pickup_time_s: NotRequired[float | None]
    """Average game time (seconds) of a player's first pickup of this buff type, over player-matches with timings, `null` without any."""
    avg_pickup_time_s: NotRequired[float | None]
    """Average game time (seconds) of the `timed_pickups`, `null` without any."""
    buff_type: str
    """Buff type, e.g. `hp_permanent_pickup_lv2`. Display names, units and colors: <https://api.deadlock-api.com/v1/assets/misc-entities> (`buff_type_name`)."""
    is_permanent: bool
    """Whether the buff is permanent. Temporary power-ups never carry pickup timings."""
    matches: int
    """Player-matches matching the filters (the same for every buff type). Average pickups per match: `pickups / matches`."""
    matches_with_pickup: int
    """Player-matches with at least one pickup of this buff type."""
    pickups: int
    """Total pickups of this buff type."""
    timed_matches: int
    """Player-matches matching the filters that record pickup timings (the same for every buff type): matches since build 6712 (2026-09-29) with at least one timed permanent pickup. Average stat gained per match: `total_stat_value / timed_matches`."""
    timed_pickups: int
    """Pickups of this buff type with a recorded game time and stat value (build 6712+)."""
    total_stat_value: float
    """Sum of the stat values granted by the `timed_pickups`, in the buff type's unit (`buff_type_value_unit` in the assets)."""


class AnalyticsGameStats(TypedDict):
    abandon_rate: float
    avg_accuracy: float
    avg_assists: float
    avg_boss_damage: float
    avg_creep_damage: float
    avg_creep_kills: float
    avg_crit_rate: float
    avg_damage_absorbed: float
    avg_damage_mitigated: float
    avg_deaths: float
    avg_denies: float
    avg_duration_s: float
    avg_ending_level: float
    avg_first_mid_boss_time_s: float
    avg_first_objective_destroyed_time_s: float
    avg_first_permanent_buff_time_s: NotRequired[float | None]
    """Average game time (seconds) of a player's first permanent buff pickup. Only matches since build 6712 (2026-09-29) record pickup times; `null` when the bucket has none."""
    avg_gold_ability_assassinate: float
    """Average souls per player per match from the Assassinate ability"""
    avg_gold_assists: float
    """Average souls per player per match from assists (part of the hero kill souls)"""
    avg_gold_boss: float
    avg_gold_boss_orb: float
    avg_gold_breakable: float
    """Average souls per player per match from breakables (crates, statues)"""
    avg_gold_death_loss: float
    avg_gold_denied: float
    avg_gold_item_cultist_sacrifice: float
    """Average souls per player per match from the Cultist Sacrifice item"""
    avg_gold_item_goose_egg: float
    """Average souls per player per match from the Golden Goose Egg item"""
    avg_gold_item_trophy_collector: float
    """Average souls per player per match from the Trophy Collector item"""
    avg_gold_lane_creep: float
    avg_gold_lane_creep_orbs: float
    avg_gold_neutral_creep: float
    avg_gold_neutral_creep_orbs: float
    avg_gold_player: float
    avg_gold_player_orbs: float
    avg_gold_team_bonus: float
    """Average souls per player per match from the team bonus"""
    avg_gold_treasure: float
    avg_heal_prevented: float
    avg_kd_ratio: float
    avg_kills: float
    avg_last_hits: float
    avg_max_health: float
    avg_net_worth: float
    avg_neutral_damage: float
    avg_neutral_kills: float
    avg_permanent_buffs: float
    """Average permanent buff (power-up) pickups per player per match. Buff types: <https://api.deadlock-api.com/v1/assets/misc-entities>"""
    avg_permanent_buffs_per_min: float
    """Average permanent buff pickups per player per minute of match time."""
    avg_player_damage: float
    avg_player_damage_taken: float
    avg_player_healing: float
    avg_possible_creeps: float
    avg_self_healing: float
    avg_tech_power: float
    avg_weapon_power: float
    bucket: int
    mid_boss_kill_rate: float
    team0_wins: int
    team1_wins: int
    total_matches: int
    total_players: int


class AnalyticsHeroStats(TypedDict):
    bucket: int
    bucket_matches_since_first_day: int
    """Sum of `matches` over all heroes in this bucket, counting only the UTC days from this hero's first match in the response on. A pick rate that leaves out the part of the range before the hero's release: `matches / bucket_matches_since_first_day` times the players per match. The hero's first day counts whole, so it still includes the hours before its first match."""
    hero_id: int
    """See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    losses: int
    matches: int
    matches_per_bucket: int
    permanent_buff_matches: int
    """Matches that carry buff pickup counts. Equals `matches`, except on account-scoped queries (`account_ids` without item or ability filters): those read a per-account table that only has buff counts for matches ingested since build 6712 (late September 2026)."""
    permanent_buff_timing_matches: int
    """Matches with pickup timings. Only matches since build 6712 (2026-09-29) record pickup times, and only players with at least one permanent pickup count here."""
    total_assists: int
    total_boss_damage: int
    total_creep_damage: int
    total_deaths: int
    total_denies: int
    total_first_permanent_buff_time_s: int
    """Sum of the game time (seconds) of each player's first permanent buff pickup, over the `permanent_buff_timing_matches` matches. Average: `total_first_permanent_buff_time_s / permanent_buff_timing_matches`."""
    total_kills: int
    total_last_hits: int
    total_max_health: int
    total_net_worth: int
    total_neutral_damage: int
    total_permanent_buffs: int
    """Sum of permanent buff (power-up) pickups over the `permanent_buff_matches` matches. Average per match: `total_permanent_buffs / permanent_buff_matches`. Buff types: <https://api.deadlock-api.com/v1/assets/misc-entities>"""
    total_player_damage: int
    total_player_damage_taken: int
    total_shots_hit: int
    total_shots_missed: int
    wins: int


class BadgeDistribution(TypedDict):
    badge_level: int
    """The badge level (tier = first digits, subtier = last digit). See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    total_matches: int
    """The total number of matches."""
    unique_players: int
    """The number of unique players whose rank on their latest ranked match in the filtered range is this badge level."""


class BotFriendStatus(TypedDict):
    """Whether a prioritized account is friends with one of the bots"""
    invites: list[str]
    """Friend invite links of bots to add, empty once `is_friend` is true"""
    is_friend: bool


class BreakablePowerupLootParams(TypedDict):
    loot_list_deck_size: NotRequired[int | None]
    pickups_by_match_time_mins: dict[str, dict[str, float]]
    """Match time in minutes (string key) from which a loot table applies, mapped to `{pickup_name: relative weight}`."""


class Build(TypedDict):
    hero_build: BuildHero
    num_favorites: NotRequired[int | None]
    num_ignores: NotRequired[int | None]
    num_reports: NotRequired[int | None]
    num_weekly_favorites: NotRequired[int | None]
    rollup_category: NotRequired[int | None]


class BuildHero(TypedDict):
    author_account_id: int
    description: NotRequired[str | None]
    details: BuildHeroDetails
    development_build: NotRequired[bool | None]
    hero_build_id: int
    hero_id: int
    """See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    language: int
    last_updated_timestamp: NotRequired[int | None]
    name: str
    origin_build_id: int
    publish_timestamp: NotRequired[int | None]
    tags: NotRequired[list[int]]
    version: int


class BuildHeroDetails(TypedDict):
    ability_order: NotRequired[BuildHeroDetailsAbilityOrder | None]
    mod_categories: list[BuildHeroDetailsCategory]


class BuildHeroDetailsAbilityOrder(TypedDict):
    currency_changes: NotRequired[list[BuildHeroDetailsAbilityOrderCurrencyChange] | None]


class BuildHeroDetailsAbilityOrderCurrencyChange(TypedDict):
    ability_id: int
    annotation: NotRequired[str | None]
    currency_type: int
    delta: int


class BuildHeroDetailsCategory(TypedDict):
    description: NotRequired[str | None]
    height: NotRequired[float | None]
    mods: NotRequired[list[BuildHeroDetailsCategoryAbility] | None]
    name: str
    optional: NotRequired[bool | None]
    width: NotRequired[float | None]


class BuildHeroDetailsCategoryAbility(TypedDict):
    ability_id: int
    annotation: NotRequired[str | None]
    imbue_target_ability_id: NotRequired[int | None]
    required_flex_slots: NotRequired[int | None]
    sell_priority: NotRequired[int | None]


class BuildItemStats(TypedDict):
    builds: int
    item_id: int
    """See more: <https://api.deadlock-api.com/v1/assets/items>"""


class BuildTag(TypedDict):
    class_name: str
    icon: str
    id: int
    label: str


class ClickhouseMatchInfo(TypedDict):
    average_badge: NotRequired[int | None]
    """See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    average_badge_team0: NotRequired[int | None]
    """See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    average_badge_team1: NotRequired[int | None]
    """See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    duration_s: int
    game_mode: int
    match_id: int
    match_mode: int
    players: list[MatchPlayer]
    start_time: int


class ClickhouseSalts(TypedDict):
    cluster_id: NotRequired[int | None]
    match_id: int
    metadata_salt: NotRequired[int | None]
    replay_salt: NotRequired[int | None]
    username: NotRequired[str | None]


class Color(TypedDict):
    """RGBA color emitted by KV3 as a 3- or 4-element integer array. Alpha defaults to 255 when omitted."""
    alpha: int
    blue: int
    green: int
    red: int


class ColorGradientStop(TypedDict):
    color: Color
    position: float
    """Position of the stop along the flash's lifetime, `0.0..=1.0`."""


class ColumnSchema(TypedDict):
    data_type: str
    """Arrow data type, rendered as its canonical textual form (e.g. `Int32`, `Utf8`)."""
    name: str
    nullable: bool


class Convar(TypedDict):
    default: dict[str, Any]
    """Default value, typed by `type`: a bool, number or string, `[r, g, b, a]` for `color`, and an array of floats for vectors / `qangle`."""
    description: NotRequired[str | None]
    """Help text shown by the in-game console."""
    flags: int
    """Raw `FCVAR_*` flag bits."""
    type: ConvarType


ConvarType: TypeAlias = "Literal[\"bool\", \"int16\", \"uint16\", \"int32\", \"uint32\", \"int64\", \"uint64\", \"float32\", \"float64\", \"string\", \"color\", \"vector2\", \"vector3\", \"vector4\", \"qangle\"]"
"""Value type of a convar (`EConVarType`)."""


class CorruptedItemImages(TypedDict):
    """Shop art for corrupted items (build 6711+). The game has no per-item corrupted icon: a corrupted item is its normal image drawn inside `frame`, with the tooltip backer of its `item_slot_type`."""
    frame: ImagePair
    frame_active: ImagePair
    """Frame for an active (usable) corrupted item."""
    tooltip_backers: CorruptedTooltipBackers


class CorruptedItemInfo(TypedDict):
    """Broker ("City Never Sleeps", build 6711+) corruption data of an upgrade."""
    excluded_penalties: list[str]
    """Names of corrupted penalty definitions (`generic_data`) that can never roll on this item."""
    property_upgrades: list[RawAbilityUpgradePropertyUpgrade]
    """Property bonuses the corrupted variant gains."""


class CorruptedPenalty(TypedDict):
    """A penalty that can be rolled onto a corrupted item (build 6711+)."""
    effects: list[CorruptedPenaltyEffect]
    name: str
    roll_weight: NotRequired[float | None]


class CorruptedPenaltyEffect(TypedDict):
    bonus_per_tier: list[float]
    """Penalty value indexed by item tier (same indexing as `item_price_per_tier`; tiers that can't be corrupted are `0`), in display units: distances are meters (source suffix `m` stripped), matching `postfix`."""
    css_class: NotRequired[str | None]
    display: bool
    """`false` for effects the game applies but doesn't list in tooltips."""
    display_type: NotRequired[str | None]
    label: NotRequired[str | None]
    """Localized stat label (from `loc_token_override`)."""
    loc_token_override: NotRequired[str | None]
    modifier_value: str
    """Modifier the penalty applies, e.g. `MODIFIER_VALUE_COOLDOWN_REDUCTION_PERCENTAGE`."""
    postfix: NotRequired[str | None]
    """Localized unit suffix, e.g. `%` or ` m`."""


class CorruptedTooltipBackers(TypedDict):
    """Corrupted item tooltip backers, one per item slot type."""
    spirit: ImagePair
    vitality: ImagePair
    weapon: ImagePair


class CreateCustomRequest(TypedDict):
    callback_url: NotRequired[str | None]
    """If a callback url is provided, we will send a POST request to this url when the match starts."""
    cheats_enabled: NotRequired[bool | None]
    corrupted_item_shop_spawn_minutes: NotRequired[int | None]
    """Minute of the match at which the Broker's corrupted item shop first spawns."""
    disable_auto_ready: NotRequired[bool | None]
    """If auto-ready is disabled, the bot will not automatically ready up. You need to call the `ready` endpoint to ready up."""
    duplicate_heroes_enabled: NotRequired[bool | None]
    game_mode: NotRequired[GameMode | None]
    is_publicly_visible: NotRequired[bool | None]
    min_roster_size: NotRequired[int | None]
    randomize_lanes: NotRequired[bool | None]
    server_region: NotRequired[ServerRegion | None]


class CreateCustomResponse(TypedDict):
    callback_secret: NotRequired[str | None]
    """If a callback url is provided, this is the secret that should be used to verify the callback. The secret is a base64 encoded random string. To verify it you should compare it with the X-Callback-Secret header. If no callback url is provided, this will be None."""
    party_code: str
    party_id: str


class CrosshairCode(TypedDict):
    code: str
    """Crosshair share code that can be imported in the game's crosshair settings."""


class Curve(TypedDict):
    base: NotRequired[float | None]
    per_minute_after_start: NotRequired[float | None]


CurveOrFloat: TypeAlias = "Curve | float"


class DamageFlash(TypedDict):
    bullet_damage: FlashData
    crit_damage: FlashData
    generic_damage: NotRequired[FlashData | None]
    healing_damage: FlashData
    melee_damage: FlashData
    tech_damage: FlashData


class DeleteSteamAccountResponse(TypedDict):
    """Response for deleting a Steam account"""
    message: str


class DemoQueryJobResponse(TypedDict):
    job_id: str
    """Stable id of the job; poll `/demo/query/{job_id}` for status and the result URL."""
    status: JobStatus


class DemoQueryRequest(TypedDict):
    format: NotRequired[OutputFormat]
    """Output format of the result artifact."""
    match_id: int
    """Match whose demo to query."""
    query: str
    """SQL query to run over the demo's entity/event tables (see `/demo/schema`)."""


class DemoQueryStatusResponse(TypedDict):
    error: NotRequired[str | None]
    """Failure reason, once `failed`."""
    estimated_wait_seconds: NotRequired[int | None]
    """Rough seconds until the result is ready, while `queued` or `running`."""
    format: OutputFormat
    job_id: str
    match_id: int
    result_url: NotRequired[str | None]
    """Public URL of the result artifact, once `done`. NDJSON results are zstd-compressed (`.ndjson.zst`); Parquet results are served as-is."""
    status: JobStatus


class DemoSchemaResponse(TypedDict):
    demo_url: str
    match_id: int
    tables: list[TableSchemaResponse]


class DependantAbilities(TypedDict):
    flags: NotRequired[list[str] | None]


class DistributionEntry(TypedDict):
    players: int
    rank: int


class DraftBucket(TypedDict):
    good: NotRequired[float | None]
    normal: NotRequired[float | None]


class DraftBuckets(TypedDict):
    bucket: NotRequired[DraftBucket | None]
    name: NotRequired[str | None]


class EnemyStats(TypedDict):
    enemy_id: int
    matches: list[int]
    matches_played: int
    wins: int
    """The amount of matches won against the enemy."""


FeedItem: TypeAlias = "dict[str, Any]"


FeedbackKind: TypeAlias = "Literal[\"annotation\", \"general\"]"


class FeedbackSubmission(TypedDict):
    build_id: NotRequired[str | None]
    comment: str
    element_text: NotRequired[str | None]
    kind: FeedbackKind
    nickname: NotRequired[str | None]
    page_url: str
    selector: NotRequired[str | None]
    source: NotRequired[SourceLocation | None]
    targets: NotRequired[list[FeedbackTarget]]
    """The annotated elements. Left empty for general feedback."""
    viewport: NotRequired[Viewport | None]


class FeedbackTarget(TypedDict):
    """One annotated element. A submission carries several when the visitor picked more than one."""
    element_text: NotRequired[str | None]
    selector: NotRequired[str | None]
    source: NotRequired[SourceLocation | None]


class FlashData(TypedDict):
    brightness: NotRequired[float | None]
    brightness_in_light_sensitivity_mode: NotRequired[float | None]
    color: Color
    """Flat flash color. From build 6711 on it is derived from the first `color_gradient` stop."""
    color_gradient: NotRequired[list[ColorGradientStop] | None]
    """Color gradient over the flash's lifetime (build 6711+)."""
    coverage: NotRequired[float | None]
    """Only present up to build 6701."""
    duration: float
    hardness: NotRequired[float | None]
    """Only present up to build 6701."""


class ForumPatch(TypedDict):
    category: PatchCategory
    content: str
    guid: PatchGuid
    link: str
    pub_date: str
    title: str


GameMode: TypeAlias = "Literal[\"normal\", \"street_brawl\", \"explore_n_y_c\", \"internal\", \"internal02\"]"


class GenericData(TypedDict):
    aim_spring_strength: list[float]
    armor_groups: list[ItemGroup]
    breakable_powerup_loot_params: NotRequired[BreakablePowerupLootParams | None]
    color_enemy: NotRequired[Color | None]
    color_friend: NotRequired[Color | None]
    color_team1: NotRequired[Color | None]
    color_team2: NotRequired[Color | None]
    corrupted_item_images: NotRequired[CorruptedItemImages | None]
    corrupted_penalties: NotRequired[list[CorruptedPenalty] | None]
    """Penalties that can be rolled onto corrupted items (build 6711+)."""
    damage_flash: DamageFlash
    enemy_objectives_and_zipline_color: NotRequired[Color | None]
    enemy_objectives_color: NotRequired[Color | None]
    enemy_zipline_color: NotRequired[Color | None]
    glitch_settings: GlitchSettings
    hero_kill_gold_share_frac: list[float]
    item_corruption_price_per_tier: NotRequired[list[int] | None]
    """Extra cost of corrupting an item, by item tier (build 6711+)."""
    item_price_per_tier: list[int]
    item_tooltip_backers: ItemTooltipBackers
    """Item tooltip backgrounds per slot type (the corrupted variants are in `corrupted_item_images`)."""
    lane_info: list[LaneInfo]
    map_districts: NotRequired[list[MapDistrict] | None]
    """District / building labels shown on the map (build 6711+)."""
    mini_map_offsets: list[MiniMapOffsets]
    minimap_team_combine_color: NotRequired[Color | None]
    minimap_team_rebels_color: NotRequired[Color | None]
    neutral_camp_respawn_timer_show_distance: NotRequired[float | None]
    """Distance within which a neutral camp's respawn timer is shown (build 6711+)."""
    new_player_metrics: list[NewPlayerMetrics]
    objective_params: ObjectiveParams
    rejuv_params: RejuvParams
    spirit_groups: list[ItemGroup]
    street_brawl: NotRequired[StreetBrawl | None]
    targeting_spring_strength: list[float]
    trooper_kill_gold_share_frac: list[float]
    weapon_groups: list[ItemGroup]


class GetCustomMatchIdResponse(TypedDict):
    match_id: int


class GlitchSettings(TypedDict):
    breakup_strength: float
    distort_strength: float
    frame_rate: float
    jump_strength: float
    quantize_scale: float
    quantize_strength: float
    scanline_strength: float
    speed: float
    strength: float
    uantize_type: float
    """Field name preserved as-is for `/v2/generic-data` compatibility."""
    white_noise_strength: float


class HashMapValue(TypedDict):
    avg: float
    percentile1: float
    percentile10: float
    percentile25: float
    percentile5: float
    percentile50: float
    percentile75: float
    percentile90: float
    percentile95: float
    percentile99: float
    std: float


HashMap: TypeAlias = "dict[str, HashMapValue]"


HashMap_HeroItemType_String: TypeAlias = "dict[str, str]"


class HashMap_ItemSlotType_ItemSlotInfoValue(TypedDict):
    max_purchases_for_tier: list[int]


HashMap_ItemSlotType_ItemSlotInfo: TypeAlias = "dict[str, HashMap_ItemSlotType_ItemSlotInfoValue]"


class HashMap_ItemSlotType_Vec_MapModCostBonusValueItem(TypedDict):
    bonus: float
    gold_threshold: int
    percent_on_graph: float


HashMap_ItemSlotType_Vec_MapModCostBonus: TypeAlias = "dict[str, list[HashMap_ItemSlotType_Vec_MapModCostBonusValueItem]]"


class HashMap_ItemSlotType_Vec_PurchaseBonusValueItem(TypedDict):
    tier: int
    value: str
    value_type: str


HashMap_ItemSlotType_Vec_PurchaseBonus: TypeAlias = "dict[str, list[HashMap_ItemSlotType_Vec_PurchaseBonusValueItem]]"


class HashMap_String_LevelInfoValue(TypedDict):
    bonus_currencies: NotRequired[list[str] | None]
    required_gold: int
    use_standard_upgrade: NotRequired[bool | None]


HashMap_String_LevelInfo: TypeAlias = "dict[str, HashMap_String_LevelInfoValue]"


class HashMap_String_Option_DraftBucketingValue1(TypedDict):
    bucket: NotRequired[str | None]
    weight: NotRequired[float | None]


HashMap_String_Option_DraftBucketing: TypeAlias = "dict[str, HashMap_String_Option_DraftBucketingValue1 | None]"


class HashMap_String_ScalingStatValue(TypedDict):
    scale: float
    scaling_stat: str


HashMap_String_ScalingStat: TypeAlias = "dict[str, HashMap_String_ScalingStatValue]"


HashMap_String_String: TypeAlias = "dict[str, str]"


HashMap_String_f64: TypeAlias = "dict[str, float]"


class Hero(TypedDict):
    assigned_players_only: bool
    """`m_bAssignedPlayersOnly` was removed in build 6711; always `false` since."""
    class_name: str
    colors: HeroColors
    complexity: int
    cost_bonuses: NotRequired[HashMap_ItemSlotType_Vec_MapModCostBonus | None]
    description: HeroDescription
    development_state: NotRequired[HeroDevelopmentState | None]
    disabled: bool
    gender: NotRequired[str | None]
    """Hero gender (`m_strHeroGender`, build 6711+), e.g. `male` / `female`."""
    gun_tag: NotRequired[str | None]
    hero_stats_ui: HeroStatsUI
    hero_type: NotRequired[HeroType | None]
    hideout_rich_presence: NotRequired[str | None]
    id: int
    images: HeroImages
    in_development: bool
    item_draft_bucketing: NotRequired[HashMap_String_Option_DraftBucketing | None]
    item_draft_weights: NotRequired[HashMap_String_f64 | None]
    item_slot_info: HashMap_ItemSlotType_ItemSlotInfo
    items: HashMap_HeroItemType_String
    level_info: HashMap_String_LevelInfo
    limited_testing: bool
    models: HashMap_String_String
    """3D model of the hero as a self-contained glTF binary (`.glb`), keyed by pose (e.g. `hero_select`, the hero select screen pose). Each file holds the skinned mesh, its skeleton and that pose's animation clip; weapons and props only sit in the hero's hands once the clip is applied. Uses `EXT_meshopt_compression` and `EXT_texture_webp`. Empty when the game files don't ship the hero's model."""
    name: str
    needs_testing: bool
    physics: HeroPhysics
    player_selectable: bool
    """Read from `m_bPlayerSelectable` on older builds; since build 6711 it is derived as `development_state == release`."""
    popular_items: NotRequired[HeroPopularItems | None]
    prerelease_only: NotRequired[bool | None]
    """Read from `m_bPrereleaseOnly` on older builds; since build 6711 it is derived as `development_state == pre_release`."""
    purchase_bonuses: HashMap_ItemSlotType_Vec_PurchaseBonus
    """Deprecated: `m_mapPurchaseBonuses` was removed in build 6711, so this is always empty for newer builds."""
    scaling_stats: HashMap_String_ScalingStat
    search_name: NotRequired[str | None]
    """Localized search name (`m_strHeroSearchName`, build 6711+)."""
    shop_stat_display: ShopStatDisplay
    skin: int
    standard_level_up_upgrades: HashMap_String_f64
    starting_stats: StartingStats
    stats_display: StatsDisplay
    tags: list[str]
    """Always emitted (empty if the hero declares no `m_vecHeroTags`)."""


class HeroBanStats(TypedDict):
    bans: int
    """The number of matches in which this hero was banned."""
    bucket: int
    """The bucket value (depends on the bucket query parameter)."""
    hero_id: int
    """The ID of the banned hero. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    matches: int
    """The number of matches with ban data in this bucket. A hero's ban rate is `bans / matches`; a ranked match has 3 bans and an unranked match 2, so the bans of all heroes do not divide into matches by a fixed count."""


class HeroBuildStats(TypedDict):
    avg_average_badge: NotRequired[float | None]
    """Average badge (tier = first digits, subtier = last digit) of the matches with this build that have one; 0 without any. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    bucket: int
    """The bucket value (depends on the bucket query parameter, 0 without one)."""
    hero_build_id: int
    """The ID of the hero build. The `hero_build_id` is the first build the player had selected when the game started."""
    hero_id: int
    """The ID of the hero. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    losses: int
    """The number of losses with this build."""
    matches: int
    """The total number of matches played with this build (`wins + losses`)."""
    players: int
    """The number of unique players who used this build."""
    total_assists: NotRequired[int | None]
    total_boss_damage: NotRequired[int | None]
    total_creep_damage: NotRequired[int | None]
    total_creep_kills: NotRequired[int | None]
    total_damage_mitigated: NotRequired[int | None]
    total_deaths: NotRequired[int | None]
    total_denies: NotRequired[int | None]
    total_duration_s: NotRequired[int | None]
    """Sum of the match durations (seconds), for per-minute rates."""
    total_hero_bullets_hit: NotRequired[int | None]
    """Bullets that hit an enemy hero."""
    total_hero_bullets_hit_crit: NotRequired[int | None]
    """Hero hits that were crits (headshots)."""
    total_kills: NotRequired[int | None]
    """Sum of the kills of every match with this build. Average per match: `total_kills / matches`. This and the other totals are only present with `include_performance=true`."""
    total_last_hits: NotRequired[int | None]
    total_level: NotRequired[int | None]
    """Sum of the final hero levels."""
    total_max_health: NotRequired[int | None]
    total_net_worth: NotRequired[int | None]
    """Sum of the final net worth (souls)."""
    total_neutral_damage: NotRequired[int | None]
    total_neutral_kills: NotRequired[int | None]
    total_player_damage: NotRequired[int | None]
    total_player_damage_taken: NotRequired[int | None]
    total_player_healing: NotRequired[int | None]
    total_self_healing: NotRequired[int | None]
    total_shots_hit: NotRequired[int | None]
    total_shots_missed: NotRequired[int | None]
    total_teammate_healing: NotRequired[int | None]
    wins: int
    """The number of wins with this build."""


class HeroColors(TypedDict):
    style: NotRequired[list[int] | None]
    style_hex: NotRequired[str | None]
    ui: list[int]


class HeroCombStats(TypedDict):
    hero_ids: list[int]
    """See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    losses: int
    matches: int
    wins: int


class HeroCounterStats(TypedDict):
    assists: int
    """The number of assists by `hero_id` when facing `enemy_hero_id`."""
    creeps: int
    """The number of creeps killed by `hero_id` when facing `enemy_hero_id`."""
    deaths: int
    """The number of deaths by `hero_id` when facing `enemy_hero_id`."""
    denies: int
    """The number of denies by `hero_id` when facing `enemy_hero_id`."""
    enemy_assists: int
    """The number of assists by `enemy_hero_id` when facing `hero_id`."""
    enemy_creeps: int
    """The number of creeps killed by `enemy_hero_id` when facing `hero_id`."""
    enemy_deaths: int
    """The number of deaths by `enemy_hero_id` when facing `hero_id`."""
    enemy_denies: int
    """The number of denies by `enemy_hero_id` when facing `hero_id`."""
    enemy_hero_id: int
    """The ID of the opposing hero. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    enemy_kills: int
    """The number of kills by `enemy_hero_id` when facing `hero_id`."""
    enemy_last_hits: int
    """The number of last hits by `enemy_hero_id` when facing `hero_id`."""
    enemy_networth: int
    """The net worth of `enemy_hero_id` when facing `hero_id`."""
    enemy_obj_damage: int
    """The amount of objective damage dealt by `enemy_hero_id` when facing `hero_id`."""
    hero_id: int
    """The ID of the hero. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    kills: int
    """The number of kills by `hero_id` when facing `enemy_hero_id`."""
    last_hits: int
    """The number of last hits by `hero_id` when facing `enemy_hero_id`."""
    matches_played: int
    """The total number of matches played between `hero_id` and `enemy_hero_id` that meet the filter criteria."""
    networth: int
    """The net worth of `hero_id` when facing `enemy_hero_id`."""
    obj_damage: int
    """The amount of objective damage dealt by `hero_id` when facing `enemy_hero_id`."""
    wins: int
    """The number of times `hero_id` won the match when facing `enemy_hero_id`."""


class HeroDescription(TypedDict):
    lore: NotRequired[str | None]
    playstyle: NotRequired[str | None]
    role: NotRequired[str | None]


HeroDevelopmentState: TypeAlias = "Literal[\"release\", \"pre_release\", \"debug_only\"]"


class HeroEntry(TypedDict):
    hero_id: int
    """See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    matches: int
    rank: int
    value: float


class HeroImages(TypedDict):
    background_image: NotRequired[str | None]
    background_image_webp: NotRequired[str | None]
    hero_card_critical: NotRequired[str | None]
    hero_card_critical_webp: NotRequired[str | None]
    hero_card_gloat: NotRequired[str | None]
    hero_card_gloat_webp: NotRequired[str | None]
    icon_hero_card: NotRequired[str | None]
    icon_hero_card_webp: NotRequired[str | None]
    icon_image_small: NotRequired[str | None]
    icon_image_small_webp: NotRequired[str | None]
    minimap_image: NotRequired[str | None]
    minimap_image_webp: NotRequired[str | None]
    name_image: NotRequired[str | None]
    top_bar_vertical_image: NotRequired[str | None]
    top_bar_vertical_image_webp: NotRequired[str | None]
    vote_sticker: NotRequired[str | None]
    """Hero release vote sticker (`m_strVoteSticker`, build 6711+)."""
    vote_sticker_webp: NotRequired[str | None]
    weapon_image: NotRequired[str | None]
    weapon_image_webp: NotRequired[str | None]


class HeroPhysics(TypedDict):
    collision_height: NotRequired[float | None]
    collision_radius: NotRequired[float | None]
    footstep_sound_travel_distance_meters: NotRequired[float | None]
    stealth_speed_meters_per_second: float
    step_height: NotRequired[float | None]
    step_sound_time: NotRequired[float | None]
    step_sound_time_sprinting: NotRequired[float | None]


class HeroPopularItem(TypedDict):
    class_name: str
    item_id: int
    """Item id, derived from `class_name` like `/v2/items` ids."""
    pick_pct: float
    """Pick rate in percent (0-100)."""
    winrate_pct: float
    """Win rate in percent (0-100)."""


class HeroPopularItems(TypedDict):
    early_game: list[HeroPopularItem]
    late_game: list[HeroPopularItem]
    mid_game: list[HeroPopularItem]
    timestamp: NotRequired[int | None]
    """Unix timestamp (seconds) at which Valve generated the data."""


class HeroStats(TypedDict):
    account_id: int
    accuracy: float
    assists: int
    assists_per_min: float
    avg_first_permanent_buff_time_s: NotRequired[float | None]
    """Average game time (seconds) of the first permanent buff pickup, over matches with pickup timings (build 6712+, at least one permanent pickup), `null` without any."""
    creeps_per_min: float
    crit_shot_rate: float
    damage_mitigated_per_min: float
    damage_per_min: float
    damage_per_soul: float
    damage_taken_per_min: float
    damage_taken_per_soul: float
    deaths: int
    deaths_per_min: float
    denies_per_match: float
    denies_per_min: float
    ending_level: float
    hero_id: int
    """See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    kills: int
    kills_per_min: float
    last_hits_per_min: float
    last_played: int
    matches: list[int]
    matches_played: int
    mvp_rank_counts: list[int]
    """Matches by the MVP rank Valve awarded the player: index 0 is rank 1 (MVP), index 1 is rank 2, index 2 is rank 3. Only the top three players of a match get a rank."""
    mvp_rated_matches: int
    """Matches played since Valve started reporting MVP ranks (2026-01-06). Divide `mvp_rank_counts` by this, not by `matches_played`, when the time range reaches further back."""
    networth_per_min: float
    obj_damage_per_min: float
    obj_damage_per_soul: float
    permanent_buff_matches: int
    """Matches that carry buff pickup counts. Only matches ingested since build 6712 (late September 2026) have them here, so divide by this rather than `matches_played`."""
    permanent_buffs: int
    """Permanent buff (power-up) pickups over the `permanent_buff_matches` matches. Buff types: <https://api.deadlock-api.com/v1/assets/misc-entities>"""
    permanent_buffs_per_min: NotRequired[float | None]
    """Permanent buff pickups per minute over the `permanent_buff_matches` matches, `null` without any."""
    time_played: int
    total_boss_damage: int
    total_creep_damage: int
    total_neutral_damage: int
    total_player_damage: int
    total_player_damage_taken: int
    wins: int


class HeroStatsUI(TypedDict):
    display_stats: list[HeroStatsUIDisplay]
    weapon_stat_display: str


class HeroStatsUIDisplay(TypedDict):
    category: str
    stat_type: str


class HeroSwapStats(TypedDict):
    bucket: int
    """The bucket value (depends on the bucket query parameter)."""
    hero_id: int
    """The ID of the hero. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    matches: int
    """The number of players who played this hero, counting only players whose pre-game hero is known."""
    pregame_picks: int
    """The number of players who had this hero locked before the pre-game swap window."""
    swapped_away: int
    """The number of `pregame_picks` players who swapped away from this hero."""
    swapped_in: int
    """The number of players who played this hero after swapping to it from another pre-game hero."""
    swapped_in_wins: int
    """The number of `swapped_in` players who won the match."""


class HeroSynergyStats(TypedDict):
    assists1: int
    """The number of assists by `hero_id1` when playing with `hero_id2`."""
    assists2: int
    """The number of assists by `hero_id2` when playing with `hero_id1`."""
    creeps1: int
    """The number of creeps killed by `hero_id1` when playing with `hero_id2`."""
    creeps2: int
    """The number of creeps killed by `hero_id2` when playing with `hero_id1`."""
    deaths1: int
    """The number of deaths by `hero_id1` when playing with `hero_id2`."""
    deaths2: int
    """The number of deaths by `hero_id2` when playing with `hero_id1`."""
    denies1: int
    """The number of denies by `hero_id1` when playing with `hero_id2`."""
    denies2: int
    """The number of denies by `hero_id2` when playing with `hero_id1`."""
    hero_id1: int
    """The ID of the first hero in the pair."""
    hero_id2: int
    """The ID of the second hero in the pair."""
    kills1: int
    """The number of kills by `hero_id1` when playing with `hero_id2`."""
    kills2: int
    """The number of kills by `hero_id2` when playing with `hero_id1`."""
    last_hits1: int
    """The number of last hits by `hero_id1` when playing with `hero_id2`."""
    last_hits2: int
    """The number of last hits by `hero_id2` when playing with `hero_id1`."""
    matches_played: int
    """The total number of matches played where `hero_id1` and `hero_id2` were on the same team, meeting the filter criteria."""
    networth1: int
    """The net worth of `hero_id1` when playing with `hero_id2`."""
    networth2: int
    """The net worth of `hero_id2` when playing with `hero_id1`."""
    obj_damage1: int
    """The amount of objective damage dealt by `hero_id1` when playing with `hero_id2`."""
    obj_damage2: int
    """The amount of objective damage dealt by `hero_id2` when playing with `hero_id1`."""
    wins: int
    """The number of times the team won when both `hero_id1` and `hero_id2` were on the same team."""


HeroType: TypeAlias = "Literal[\"assassin\", \"brawler\", \"marksman\", \"mystic\"]"


class HorizontalRecoil(TypedDict):
    burst_exponent: NotRequired[float | None]
    range: NotRequired[RecoilRange | None]


class ImagePair(TypedDict):
    """A png image and its webp variant."""
    png: str
    webp: str


class IngestLiveUrl(TypedDict):
    broadcast_url: str
    lobby_id: NotRequired[int | None]
    match_id: int
    started_at: NotRequired[int | None]


class IngestStatusResponse(TypedDict):
    account_id: int
    active: bool
    """Whether the ingest tool uploaded a salt for this account within the window that was then verified."""
    last_upload_at: NotRequired[int | None]
    """Unix timestamp of the most recent verified upload within the window."""
    window_days: int
    """The window, in days, an upload must fall in to count."""


Item: TypeAlias = "Ability | Weapon | Upgrade"


class ItemDraftRound(TypedDict):
    normal_mod_tier: int
    rare_mod_tier: int


class ItemDraftRoundPerGameRound(TypedDict):
    chance_enhanced: OutcomeToWeights
    chance_rare: OutcomeToWeights
    item_draft_rounds: list[ItemDraftRound]


class ItemFlowEdge(TypedDict):
    """A transition between an item in one column and an item in the next column, counted across players who purchased both."""
    from_column: int
    """The column of the source item."""
    from_item_id: int
    losses: int
    matches: int
    to_item_id: int
    wins: int


class ItemFlowLeaveOneOut(TypedDict):
    """The locked build path without one of its locked items: how the population changes when that item's constraint is dropped and every other one kept."""
    column: int
    """Its locked stage column."""
    item_id: int
    """The locked item left out. See more: <https://api.deadlock-api.com/v1/assets/items>"""
    matches: int
    wins: int


class ItemFlowNode(TypedDict):
    """A single item, aggregated within one column of the flow graph."""
    adjusted_win_rate: float
    """Win rate standardized to the stage's net-worth-at-buy distribution, removing the "richer buyers win more" confound. See the endpoint description."""
    avg_net_worth_at_buy: float
    """Average net worth of buyers at the moment they bought this item (confound visibility)."""
    column: int
    """The phase column (0-based) the item was bought in."""
    item_id: int
    """See more: <https://api.deadlock-api.com/v1/assets/items>"""
    losses: int
    matches: int
    players: int
    total_assists: int
    total_deaths: int
    total_kills: int
    wins: int


class ItemFlowStats(TypedDict):
    baseline: ItemFlowSummary
    """Totals ignoring the locked build path (item filters only). Denominator for chained pick rate."""
    edges: list[ItemFlowEdge]
    leave_one_out: list[ItemFlowLeaveOneOut]
    """One entry per locked item, in request order: the totals of the locked build path without that item. `summary` against an entry is what that one item adds to the build. Empty without locks."""
    nodes: list[ItemFlowNode]
    reached_per_column: list[int]
    """Distinct baseline games that bought any upgrade in each stage column (index = column). `reached / baseline.matches` shows how survivorship-selected a (late) stage is."""
    reached_wins_per_column: NotRequired[list[int]]
    """Of `reached_per_column`, the games that were won (index = column). `reached_wins / reached` is the win rate of games that got that far, the fair baseline for a build ending there."""
    summary: ItemFlowSummary
    """Totals for the locked build-path population (all filters applied). Denominator for pick rate."""
    summary_reached_per_column: NotRequired[list[int]]
    """`reached_per_column` for the locked build path's games (`summary`). Late stages hold long games only, so an item bought there is compared with the build's games that got that far."""
    summary_reached_wins_per_column: NotRequired[list[int]]
    """Of `summary_reached_per_column`, the games that were won (index = column)."""


class ItemFlowSummary(TypedDict):
    """Population-level totals for the (optionally locked) build path."""
    avg_duration_s: float
    """Average match duration (seconds) of the population."""
    avg_net_worth: float
    """Average final net worth of the population."""
    losses: int
    matches: int
    players: int
    total_assists: int
    total_deaths: int
    total_kills: int
    wins: int


class ItemGroup(TypedDict):
    shop_group: str
    upgrades: list[str]


class ItemPermutationStats(TypedDict):
    item_ids: list[int]
    """See more: <https://api.deadlock-api.com/v1/assets/items>"""
    losses: int
    matches: int
    wins: int


class ItemProperty(TypedDict):
    can_set_token_override: NotRequired[bool | None]
    conditional: NotRequired[str | None]
    css_class: NotRequired[str | None]
    disable_value: NotRequired[str | None]
    display_units: NotRequired[str | None]
    icon: NotRequired[str | None]
    label: NotRequired[str | None]
    loc_token_override: NotRequired[str | None]
    negative_attribute: NotRequired[bool | None]
    postfix: NotRequired[str | None]
    postvalue_label: NotRequired[str | None]
    prefix: NotRequired[str | None]
    provided_property_type: NotRequired[str | None]
    required_upgrade_bits: NotRequired[list[str] | None]
    """Raw `ABILITY_UPGRADE_BIT_*` flags the ability needs for this property to apply (e.g. `ABILITY_UPGRADE_BIT_TRAINED`, `ABILITY_UPGRADE_BIT_4`)."""
    scale_function: NotRequired[RawItemPropertyScaleFunctionSubclass | None]
    street_brawl_value: NotRequired[str | None]
    usage_flags: NotRequired[list[StatsUsageFlag] | None]
    value: NotRequired[str | None]
    """Raw JSON value preserves the source distinction between numeric and stringly-typed bonuses (`"14.5"` vs `14.5`)."""


ItemSlotType: TypeAlias = "Literal[\"weapon\", \"spirit\", \"vitality\"]"


class ItemStats(TypedDict):
    avg_buy_time_relative: float
    """Average buy time as percentage of match duration"""
    avg_buy_time_s: float
    """Average buy time in seconds (absolute)"""
    avg_sell_time_relative: float
    """Average sell time as percentage of match duration (for items that were sold)"""
    avg_sell_time_s: float
    """Average sell time in seconds (absolute, for items that were sold)"""
    bucket: int
    item_id: int
    """See more: <https://api.deadlock-api.com/v1/assets/items>"""
    losses: int
    matches: int
    players: int
    sold: NotRequired[int]
    """How many of the `matches` purchases were sold again. `sold / matches` is the sell rate."""
    wins: int


class ItemTooltipBacker(TypedDict):
    """Item tooltip background of one slot type: the backer, its alpha mask and the color layer."""
    backer: ImagePair
    color: ImagePair
    mask: ImagePair


class ItemTooltipBackers(TypedDict):
    """Item tooltip backgrounds, one per item slot type."""
    spirit: ItemTooltipBacker
    vitality: ItemTooltipBacker
    weapon: ItemTooltipBacker


ItemType: TypeAlias = "Literal[\"ability\", \"weapon\", \"upgrade\"]"
"""Discriminator for the `type` field on every item variant."""


JobStatus: TypeAlias = "Literal[\"queued\", \"running\", \"done\", \"failed\"]"


class KillDeathStats(TypedDict):
    deaths: int
    killer_team: int
    kills: int
    position_x: int
    position_y: int


class LaneInfo(TypedDict):
    color: NotRequired[Color | None]
    css_class: NotRequired[str | None]
    is_enemy_lane: bool
    lane_name: str
    """Localized lane name. Unused lane slots are named `Unused`."""
    minimap_color: NotRequired[Color | None]
    minimap_zipline_color_override: NotRequired[Color | None]
    objective_color: NotRequired[Color | None]


class LaneMatchupStat(TypedDict):
    """One requested stat, read at `sample_time_s` and averaged over the matchups that reached it."""
    diff: float
    """Mean of the duo's combined value minus the enemy duo's. Negative means behind."""
    diff_std: float
    """Population standard deviation of `diff` across the counted matchups."""
    value: float
    """Mean of the duo's combined value, summed over its two players."""
    value_std: float
    """Population standard deviation of `value` across the counted matchups."""


class LaneMatchupStats(TypedDict):
    """**⚠️ Subject to change:** newly added, fields may change or be removed without notice."""
    assigned_lane: int
    """The lane the matchup was played in, or `0` when `assigned_lane` was grouped away. See the `lane_info` array of <https://api.deadlock-api.com/v1/assets/generic-data>."""
    enemy_hero_ids: list[int]
    """The ascending hero id pair they laned against, or empty when grouped away."""
    hero_ids: list[int]
    """The ascending hero id pair that shared the lane, or empty when grouped away. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    matches_played: int
    """The total number of lane matchups between `hero_ids` and `enemy_hero_ids` in this lane."""
    net_worth_diff: float
    """Mean souls the duo is ahead by at `sample_time_s`, against that duo. Negative means behind. `0` when no counted matchup lasted that long."""
    sample_matches: int
    """How many of `matches_played` lasted to `sample_time_s` with all four players still in. Every reading on this row rests on those matchups only."""
    sample_time_s: int
    """Seconds into the match the stat readings were taken at. Echoes the `sample_time_s` parameter."""
    stats: dict[str, LaneMatchupStat]
    """A reading per stat named in `stats`. Empty unless the parameter was set."""
    wins: int
    """The number of matches `hero_ids` won against `enemy_hero_ids` in this lane."""


class LaneSoulCurve(TypedDict):
    """**⚠️ Subject to change:** newly added, fields may change or be removed without notice."""
    assigned_lane: int
    """The lane the matchup was played in, or `0` when `assigned_lane` was grouped away. See the `lane_info` array of <https://api.deadlock-api.com/v1/assets/generic-data>."""
    enemy_hero_ids: list[int]
    """The ascending hero id pair they laned against, or empty when grouped away."""
    hero_ids: list[int]
    """The ascending hero id pair that shared the lane, or empty when grouped away. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    matches_played: int
    """Lane matchups behind the row, counted at its *first* sample. This is what `min_matches` and `max_matches` filter on, so it does not move when the requested time range changes; read `sample_matches` for what any individual point rests on."""
    net_worth_diff: list[float]
    """Mean souls the duo is ahead by at the matching entry of `sample_times_s`. Negative means behind. Same length as `sample_times_s`."""
    net_worth_diff_std: list[float]
    """Population standard deviation of the lead across the counted matchups, at the matching entry of `sample_times_s`. Same length as `sample_times_s`. Spread between individual games, not uncertainty about the mean: it stays wide however many matchups are counted, because lane outcomes genuinely differ that much."""
    sample_matches: list[int]
    """How many lane matchups were still running at the matching entry of `sample_times_s`. Falls off towards the end of the curve as shorter matches drop out."""
    sample_times_s: list[int]
    """Seconds into the match each entry of the curves was sampled at, ascending."""
    stats: dict[str, LaneStatCurve]
    """A curve per stat named in `stats`. Empty unless the parameter was set."""


class LaneStatCurve(TypedDict):
    """One requested stat's curve. All four arrays line up with `sample_times_s`."""
    diff: list[float]
    """Mean of the duo's combined value minus the enemy duo's. Negative means behind."""
    diff_std: list[float]
    """Population standard deviation of `diff` across the counted matchups."""
    value: list[float]
    """Mean of the duo's combined value, summed over its two players."""
    value_std: list[float]
    """Population standard deviation of `value` across the counted matchups."""


class LastRankedMatch(TypedDict):
    match_id: int
    player_rank_consumed_demotion_protection: NotRequired[bool | None]
    """Whether the match used up one of the player's demotion protection games."""
    player_rank_desired_progress_change: NotRequired[int | None]
    """Progress change the match was supposed to award, before demotion protection is applied."""
    player_rank_final_flat_progress: NotRequired[int | None]
    """Rank progress the player ended the match with."""
    player_rank_initial_calibration_games: NotRequired[int | None]
    """Remaining placement games at the start of the match."""
    player_rank_initial_demotion_protection_games: NotRequired[int | None]
    """Remaining demotion protection games at the start of the match."""
    player_rank_initial_display_rank: int
    """Rank badge the player entered the match with, `tier * 10 + subrank`."""
    player_rank_initial_flat_progress: NotRequired[int | None]
    """Rank progress the player entered the match with."""
    player_rank_initial_win_streak: NotRequired[int | None]
    """Win streak the player entered the match with."""
    start_time: int
    """Match start time as a unix timestamp."""


class Leaderboard(TypedDict):
    entries: list[LeaderboardEntry]
    """The leaderboard entries."""


class LeaderboardEntry(TypedDict):
    account_name: NotRequired[str | None]
    """The account name of the player."""
    possible_account_ids: NotRequired[list[int]]
    """The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.**"""
    rank: NotRequired[int | None]
    """The rank of the player (tier = first digits, subtier = last digit). See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    top_hero_ids: NotRequired[list[int]]
    """The top hero IDs of the player, as the game sends them. Since 2026-07-31 the game leaves them empty for about half of the entries. See more: <https://api.deadlock-api.com/v1/assets/heroes>"""


class ListSteamAccountsResponse(TypedDict):
    """Response for listing Steam accounts"""
    accounts: list[SteamAccountListItem]
    summary: SlotsSummary


class LiveUrl(TypedDict):
    broadcast_url: str
    lobby_id: NotRequired[int | None]
    match_id: int
    started_at: NotRequired[int | None]
    updated_at: NotRequired[int | None]


class LootEntry(TypedDict):
    item: str


class LootTable(TypedDict):
    entries: list[LootEntry]


class MMRHistory(TypedDict):
    account_id: int
    division: int
    """Extracted from the rank the division (rank // 10)"""
    division_tier: int
    """Extracted from the rank the division tier (rank % 10)"""
    match_id: int
    player_score: float
    """Contiguous index of the rank (1-66), derived from `rank`"""
    rank: int
    """The Player Rank (tier = first digits, subtier = last digit). See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    start_time: int
    """Start time of the match"""


class MapData(TypedDict):
    """The `/v1/assets/map` response."""
    entities: NotRequired[MapEntities | None]
    images: MapImages
    neutral_camps: NotRequired[list[NeutralCamp] | None]
    """Neutral camps (build 6711+)."""
    objective_positions: dict[str, ObjectivePosition]
    radius: int
    zipline_paths: list[ZiplanePath]


class MapDistrict(TypedDict):
    """A district / building label pair shown on the map (build 6711+)."""
    building: NotRequired[str | None]
    """Localization token, e.g. `map_district_building_docks`. Absent for districts without buildings."""
    building_name: NotRequired[str | None]
    """Localized building name, e.g. `Docks`."""
    district: str
    """Localization token, e.g. `map_district_theater`."""
    district_name: str
    """Localized district name, e.g. `Theater`."""


class MapEntities(TypedDict):
    """Interactable map entities by category, extracted from the map entity lump."""
    base_sentries: NotRequired[list[MapEntity]]
    """Base defense sentries (`npc_base_defense_sentry`)."""
    bells: NotRequired[list[MapEntity]]
    """Chinatown bells (`citadel_breakable_bell_chinatown`)."""
    bounce_pads: NotRequired[list[MapEntity]]
    """Bounce pads (`trigger_catapult`); `target` is the landing spot."""
    bridge_buffs: NotRequired[list[MapEntity]]
    """Bridge buff spawners (`citadel_item_powerup_spawner`)."""
    climb_ropes: NotRequired[list[MapEntity]]
    """Climbable ropes (`citadel_trigger_climb_rope`)."""
    cosmic_veils: NotRequired[list[MapEntity]]
    """Cosmic veils (`citadel_passthrough_fake_wall`)."""
    crates: NotRequired[list[MapEntity]]
    """Breakable wooden crates (`citadel_breakable_prop_wooden_crate` and variants)."""
    golden_statues: NotRequired[list[MapEntity]]
    """Golden statues (`citadel_breakable_item_container`, `citadel_breakable_lion_statue`)."""
    healing_snacks: NotRequired[list[MapEntity]]
    """Healing snack spawners (`citadel_pickup_spawner`)."""
    shops: NotRequired[list[MapEntity]]
    """Item shops (`trigger_item_shop`); `kind` is `base`, `lane` or `secret`."""
    soul_urn_pads: NotRequired[list[MapEntity]]
    """Soul urn delivery pads (`citadel_trigger_idol_return`)."""
    soul_urn_spawns: NotRequired[list[MapEntity]]
    """Soul urn spawn points (`item_crate_spawn`)."""
    steam_vents: NotRequired[list[MapEntity]]
    """Steam vents (`citadel_invis_volume`, plus `citadel_obscured_volume` with `kind` `obscured`)."""
    teleporters: NotRequired[list[MapEntity]]
    """Teleporters (`citadel_trigger_teleport`); `target` is the exit."""
    tough_crates: NotRequired[list[MapEntity]]
    """Breakable tough crates (`citadel_breakable_prop_tough_crate`)."""
    unstable_rifts: NotRequired[list[MapEntity]]
    """Unstable rift spawn points (`info_koth_spawn_location`)."""


class MapEntity(TypedDict):
    """An interactable map entity (crate, bounce pad, shop, ...). Deserialized from `map/entities.json`, which has no minimap position; that is filled in after."""
    kind: NotRequired[str | None]
    """Variant within the category, e.g. `wooden_crate` or `secret` (shops)."""
    left_relative: NotRequired[float]
    """Position on the minimap, as fractions of its width/height."""
    position: list[float]
    """World position `[x, y, z]`, same space as the zip-line splines. Brush triggers (ropes, pads, veils, ...) are placed at their entity origin."""
    target: NotRequired[list[float] | None]
    """World position `[x, y, z]` the entity sends you to: the teleporter exit or the bounce pad landing spot."""
    team: NotRequired[int | None]
    """Owning team (0 or 1); absent for neutral entities."""
    top_relative: NotRequired[float]


class MapImages(TypedDict):
    """CDN URLs for the minimap image layers."""
    background: NotRequired[str | None]
    """Background layer drawn under `mid`. Only for builds before 6711; the game no longer ships it, so it is omitted from build 6711 on."""
    frame: str
    mid: str
    """Midtown base layer."""
    mid_tunnels: NotRequired[str | None]
    """Mid tunnels overlay, drawn above `mid` (build 6711+)."""
    minimap: str
    """Full minimap. From build 6711 on the game ships no composed minimap, so this is the same image as `mid`: the midtown street layer as a black mask on transparency, meant to be drawn over a base colour rather than shown on its own."""
    plain: str
    """Minimap without overlays. From build 6711 on this is the same street mask as `mid` (see `minimap`)."""
    rat_tunnels: NotRequired[str | None]
    """Rat tunnels overlay, drawn above `mid_tunnels` (build 6711+)."""


class MatchPlayer(TypedDict):
    account_id: int


class MatchSaltsResponse(TypedDict):
    cluster_id: NotRequired[int | None]
    demo_url: NotRequired[str | None]
    match_id: int
    metadata_salt: NotRequired[int | None]
    metadata_url: NotRequired[str | None]
    replay_salt: NotRequired[int | None]


class MatchSpectateResponse(TypedDict):
    broadcast_url: str
    lobby_id: NotRequired[int | None]


class MateStats(TypedDict):
    matches: list[int]
    matches_played: int
    mate_id: int
    wins: int


class MiniMapOffsets(TypedDict):
    entity_class: str
    lane_index: NotRequired[int | None]
    offset_2d: list[float]


class MiscEntity(TypedDict):
    break_on_dodge_touch: NotRequired[bool | None]
    buff_type_graph_color: NotRequired[Color | None]
    buff_type_loc_string: NotRequired[str | None]
    """Permanent pickups: localization token of the stat the buff raises."""
    buff_type_name: NotRequired[str | None]
    """Permanent pickups: `buff_type_loc_string` localized into the requested language (e.g. `Fire Rate`)."""
    buff_type_value_unit: NotRequired[str | None]
    """Permanent pickups: unit of the buff value (e.g. `Percent`, `Meters`). The modifier value itself is in game units (`Meters` values are inches, 39.37 per meter)."""
    class_name: str
    collection_method: NotRequired[str | None]
    """How the pickup is collected, e.g. `Punch` or `VacuumTrigger`."""
    collision_radius: NotRequired[float | None]
    color: NotRequired[Color | None]
    damaged_by_abilities: NotRequired[bool | None]
    damaged_by_bullets: NotRequired[bool | None]
    damaged_by_melee: NotRequired[bool | None]
    damaged_by_slide: NotRequired[bool | None]
    expiration_duration: NotRequired[CurveOrFloat | None]
    gold_amount: NotRequired[float | None]
    gold_per_minute_amount: NotRequired[float | None]
    health: NotRequired[int | None]
    heavy_melee_hit_count: NotRequired[int | None]
    heavy_melee_only: NotRequired[bool | None]
    hits_required: NotRequired[int | None]
    """Punchable pickups: hits needed to collect."""
    id: int
    in_shop_modifier: NotRequired[Subclass_ModifierDefinition | None]
    initial_spawn_delay_in_seconds: NotRequired[int | None]
    initial_spawn_delay_seconds: NotRequired[int | None]
    """Duplicate of `initial_spawn_delay_in_seconds` for shape parity."""
    initial_spawn_time: NotRequired[float | None]
    is_mantleable: NotRequired[bool | None]
    is_permanent_pickup: NotRequired[bool | None]
    lifetime: NotRequired[float | None]
    loot_list_deck_size: NotRequired[int | None]
    m_vecPickups_lv2: NotRequired[list[Pickup] | None]
    m_vecPickups_lv3: NotRequired[list[Pickup] | None]
    match_time_mins_for_level2_pickups: NotRequired[int | None]
    match_time_mins_for_level3_pickups: NotRequired[int | None]
    minimap_class: NotRequired[str | None]
    modifier: NotRequired[Subclass_ModifierDefinition | None]
    name: NotRequired[str | None]
    """`name_loc_string` localized into the requested language (e.g. `+1.5% Fire Rate`). Gold pickups use an ICU plural pattern (`{amount, plural, one{Soul} other{Souls}}`)."""
    name_loc_string: NotRequired[str | None]
    """Localization token of the pickup's world label."""
    orb_spawn_delay_max: NotRequired[float | None]
    orb_spawn_delay_min: NotRequired[float | None]
    pickup: NotRequired[str | None]
    """Pickup spawners: class name of the spawned pickup."""
    pickup_chances: NotRequired[dict[str, float] | None]
    """Pickup name to relative weight (build 6711+); replaces the `primary_pickups` / `m_vecPickups_lv*` lists."""
    pickup_radius: NotRequired[CurveOrFloat | None]
    powerup_drop_chance: NotRequired[float | None]
    """Drop chance (percent) for build 6711+; replaces `primary_drop_chance`."""
    primary_drop_chance: NotRequired[float | None]
    """Pre-6711 builds only; see `powerup_drop_chance`."""
    primary_pickups: NotRequired[list[Pickup] | None]
    regen_duration: NotRequired[float | None]
    """Health pickups: seconds over which the healing is applied to heroes."""
    regen_duration_troopers: NotRequired[float | None]
    """Health pickups: seconds over which the healing is applied to troopers."""
    regen_max_health_percent: NotRequired[CurveOrFloat | None]
    regen_trooper_multi: NotRequired[float | None]
    """Health pickups: healing multiplier for troopers."""
    render_after_death: NotRequired[bool | None]
    respawn_time: NotRequired[float | None]
    roll_type: NotRequired[RollType | None]
    show_on_minimap: NotRequired[bool | None]
    single_pickup_override: NotRequired[str | None]
    """Powerup spawners: class name of the only pickup spawned, overriding `pickup_chances`."""
    solid_after_death: NotRequired[bool | None]
    spawn_delay: NotRequired[float | None]
    """Pickup spawners: delay (seconds) before the first spawn."""
    spawn_interval: NotRequired[float | None]
    spawn_interval_in_seconds: NotRequired[int | None]
    spawn_music_state: NotRequired[str | None]
    """Corrupted item shop (Broker) trigger: music cue played on spawn."""


Modifier = TypedDict("Modifier", {"base": "NotRequired[str | None]", "class": "NotRequired[str | None]", "class_name": "str", "folder": "NotRequired[str | None]", "id": "int", "properties": "dict[str, float]"})


class ModifierValue(TypedDict):
    value: NotRequired[float | None]
    value_max: NotRequired[float | None]
    value_min: NotRequired[float | None]
    value_type: NotRequired[str | None]


class NeutralCamp(TypedDict):
    """A neutral camp ("Haunt") marker (build 6711+)."""
    icon: str
    """Minimap icon URL."""
    kind: NeutralCampKind
    left_relative: float
    """Position on the minimap, as fractions of its width/height."""
    name: str
    """Camp entity name from the map (e.g. `theater_lobby_camp`)."""
    position: list[float]
    """World position `[x, y, z]`, same space as the zip-line splines."""
    top_relative: float


NeutralCampKind: TypeAlias = "Literal[\"weak\", \"medium\", \"strong\", \"vault\"]"
"""Neutral camp strength (`info_neutral_trooper_camp` `subclass_name` `neutral_camp_{weak,medium,strong,vaults}` in `misc.vdata`)."""


class NewPlayerMetrics(TypedDict):
    abilities_upgraded: int
    boss_damage: int
    damage_taken: int
    last_hits: int
    mods_purchased: int
    net_worth: int
    orbs_denied: int
    orbs_secured: int
    player_damage: int
    skill_tier_name: str


class NpcUnit(TypedDict):
    acceleration: NotRequired[float | None]
    attack_t1_boss_max_range: NotRequired[float | None]
    attack_t3_boss_max_range: NotRequired[float | None]
    attack_t3_boss_phase2_max_range: NotRequired[float | None]
    attack_trooper_max_range: NotRequired[float | None]
    backdoor_bullet_resist_modifier: NotRequired[Subclass_BulletResistModifier | None]
    barrack_boss_dps: NotRequired[float | None]
    barrack_guardian_damage_resist_pct: NotRequired[float | None]
    boss_weapon_info: NotRequired[WeaponInfo | None]
    bound_abilities: NotRequired[dict[str, str] | None]
    class_name: str
    core_models: NotRequired[TeamModels | None]
    effigy_models: NotRequired[TeamModels | None]
    empowered_modifier_level1: NotRequired[Subclass_EmpoweredModifierLevel | None]
    empowered_modifier_level2: NotRequired[Subclass_EmpoweredModifierLevel | None]
    enemy_trooper_damage_reduction: NotRequired[Subclass_TrooperDamageReduction | None]
    enemy_trooper_protection_range: NotRequired[float | None]
    generator_boss_dps: NotRequired[float | None]
    gold_reward: NotRequired[float | None]
    gold_reward_bonus_percent_per_minute: NotRequired[float | None]
    health_bar_color_enemy: NotRequired[Color | None]
    health_bar_color_friend: NotRequired[Color | None]
    health_bar_color_team1: NotRequired[Color | None]
    health_bar_color_team2: NotRequired[Color | None]
    health_bar_color_team_neutral: NotRequired[Color | None]
    id: int
    image: NotRequired[str | None]
    """Unit icon (`m_strCustomUnitIcon`) as png."""
    image_webp: NotRequired[str | None]
    """Unit icon (`m_strCustomUnitIcon`) as webp."""
    intrinsic_modifiers: NotRequired[list[Subclass_IntrinsicModifiers] | None]
    laser_dps_max_health: NotRequired[float | None]
    laser_dps_to_players: NotRequired[float | None]
    max_health: NotRequired[int | None]
    max_health_final: NotRequired[int | None]
    max_health_generator: NotRequired[int | None]
    melee_attempt_range: NotRequired[float | None]
    melee_damage: NotRequired[float | None]
    melee_duration: NotRequired[float | None]
    melee_hit_range: NotRequired[float | None]
    models: NotRequired[dict[str, str]]
    """3D model of the unit as a self-contained glTF binary (`.glb`), keyed by pose: `idle` (the model's idle clip baked in) or `default` (no animation, for models without an idle clip). Uses `EXT_meshopt_compression` and `EXT_texture_webp`. Omitted when the unit has no published model."""
    name: NotRequired[str | None]
    """Localized unit name (`m_sLocUnitName`), e.g. `Gutter Ghoul I`."""
    near_death_duration: NotRequired[float | None]
    neutral_abilities: NotRequired[list[str] | None]
    """Neutral ability class names; see `/v1/assets/modifiers` (builds 6711+)."""
    neutral_damage_growth: NotRequired[Subclass_NeutralDamageGrowth | None]
    neutral_melee: NotRequired[str | None]
    """Neutral melee ability class name; see `/v1/assets/modifiers` (builds 6711+)."""
    neutral_type: NotRequired[str | None]
    """Neutral tier, e.g. `NEUTRAL_NPC_WEAK` (builds 6711+)."""
    no_shield_laser_dps_to_players: NotRequired[float | None]
    objective_health_growth_phase1: NotRequired[Subclass_ObjectiveHealthGrowthPhase | None]
    objective_health_growth_phase2: NotRequired[Subclass_ObjectiveHealthGrowthPhase | None]
    objective_regen: NotRequired[Subclass_ObjectiveRegen | None]
    phase2_health: NotRequired[int | None]
    player_damage_resist_pct: NotRequired[float | None]
    player_dps: NotRequired[float | None]
    ranged_armor_modifier: NotRequired[Subclass_RangedArmorModifier | None]
    run_speed: NotRequired[float | None]
    sight_range_npcs: NotRequired[float | None]
    sight_range_players: NotRequired[float | None]
    spawn_breakables_on_death: NotRequired[bool | None]
    stomp_damage: NotRequired[float | None]
    stomp_damage_max_health_percent: NotRequired[float | None]
    stomp_impact_radius: NotRequired[float | None]
    stun_duration: NotRequired[float | None]
    t1_boss_damage_resist_pct: NotRequired[float | None]
    t1_boss_dps: NotRequired[float | None]
    t1_boss_dpsbase_resist: NotRequired[float | None]
    t1_boss_dpsmax_resist: NotRequired[float | None]
    t1_boss_dpsmax_resist_time_in_seconds: NotRequired[float | None]
    t2_boss_damage_resist_pct: NotRequired[float | None]
    t2_boss_dps: NotRequired[float | None]
    t2_boss_dpsbase_resist: NotRequired[float | None]
    t2_boss_dpsmax_resist: NotRequired[float | None]
    t2_boss_dpsmax_resist_time_in_seconds: NotRequired[float | None]
    t3_boss_damage_resist_pct: NotRequired[float | None]
    t3_boss_dps: NotRequired[float | None]
    team_models: NotRequired[TeamModels | None]
    trooper_damage_resist_pct: NotRequired[float | None]
    trooper_dps: NotRequired[float | None]
    viewer_souls_class: NotRequired[dict[str, str] | None]
    """Distance threshold (as string key) → soul orb class shown to the viewer."""
    walk_speed: NotRequired[float | None]
    weapon_info: NotRequired[WeaponInfo | None]


class ObjectiveParams(TypedDict):
    base_guardians_gold_kill: int
    base_guardians_gold_orbs: int
    gold_per_orb: int
    near_player_split_pct: float
    patron_phase1_gold_kill: int
    patron_phase1_gold_orbs: int
    shrines_gold_kill: int
    shrines_gold_orbs: int
    tier1_gold_kill: int
    tier1_gold_orbs: int
    tier2_gold_kill: int
    tier2_gold_orbs: int


class ObjectivePosition(TypedDict):
    """The top-left corner of an objective marker on the minimap, as fractions of its width/height (like a CSS `margin-left`/`margin-top`). The marker is a `Core` (30% x 8%) for the cores and an `Icon` (10% x 10%) otherwise, so its centre is this position plus half that size. Unlike `neutral_camps`, whose `left_relative`/`top_relative` are the point itself. Before build 6711 these are the HUD's schematic layout; from 6711 on they are real map positions."""
    left_relative: float
    top_relative: float


class OutcomeToWeights(TypedDict):
    outcomes_to_weights: dict[str, float]


OutputFormat: TypeAlias = "Literal[\"parquet\", \"ndjson\"]"


class Patch(TypedDict):
    author: str
    category: PatchCategory
    content_encoded: str
    dc_creator: str
    guid: PatchGuid
    link: str
    pub_date: str
    slash_comments: str
    title: str


class PatchCategory(TypedDict):
    domain: str
    text: str


class PatchGuid(TypedDict):
    is_perma_link: bool
    text: str


class Pickup(TypedDict):
    pickup_name: NotRequired[str | None]
    pickup_weight: NotRequired[float | None]


class PlayerEntry(TypedDict):
    account_id: int
    badge: NotRequired[int | None]
    """`rank` and `peak_rank` sorts only: the rank badge the progress in `value` falls in, `0` when the player has no ranked match in range. Omitted for every other sort. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    badge_progress: NotRequired[int | None]
    """`rank` and `peak_rank` sorts only: progress points into `badge`. A subrank spans 1000 points, the sixth of a tier 2000. `null` in Eternus, whose subranks are percentile cuts rather than point spans, and when the player has no ranked match in range."""
    matches: int
    rank: int
    value: float


class PlayerMatchHistoryEntry(TypedDict):
    abandoned_time_s: NotRequired[int | None]
    account_id: int
    brawl_avg_round_time_s: NotRequired[int | None]
    brawl_score_team0: NotRequired[int | None]
    brawl_score_team1: NotRequired[int | None]
    denies: int
    game_mode: int
    hero_id: int
    """See more: <https://api.deadlock-api.com/v1/assets/heroes>"""
    hero_level: int
    last_hits: int
    low_pri_pool: NotRequired[bool | None]
    """Whether the match was played in the low priority pool. `None` for entries stored before this was recorded."""
    match_duration_s: int
    match_id: int
    match_mode: int
    match_result: int
    net_worth: int
    objectives_mask_team0: int
    objectives_mask_team1: int
    player_assists: int
    player_deaths: int
    player_kills: int
    player_match_outcome: int
    """How the match was scored for the player: 0 = invalid, 1 = win, 2 = loss, 3 = penalized, 4 = penalized party, 5 = not scored."""
    player_team: int
    ranked_calibration_match: NotRequired[int | None]
    """Non-zero if this match counted towards the player's ranked calibration."""
    ranked_delta: NotRequired[int | None]
    """The ranked progress change the player got from this match."""
    ranked_display_badge: NotRequired[int | None]
    """The ranked badge shown for the player after the match (tier = first digits, subtier = last digit). Within Eternus, where subranks are percentile cuts the GC misreports, this is the badge the player entered the match with. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    ranked_used_demotion_protection: NotRequired[bool | None]
    """Whether the player's demotion protection absorbed a loss in this match."""
    start_time: int


class PlayerPerformanceCurvePoint(TypedDict):
    assists_avg: float
    """Average assists at this time point"""
    assists_std: float
    """Standard deviation of assists at this time point"""
    boss_damage_avg: float
    """Average damage dealt to objectives at this time point"""
    boss_damage_std: float
    """Standard deviation of `boss_damage_avg` at this time point"""
    boss_kills_avg: float
    """Average objectives killed (last hits) at this time point"""
    boss_kills_std: float
    """Standard deviation of `boss_kills_avg` at this time point"""
    creep_damage_avg: float
    """Average damage dealt to lane creeps at this time point"""
    creep_damage_std: float
    """Standard deviation of `creep_damage_avg` at this time point"""
    creep_kills_avg: float
    """Average lane creeps killed (last hits) at this time point"""
    creep_kills_std: float
    """Standard deviation of `creep_kills_avg` at this time point"""
    deaths_avg: float
    """Average deaths at this time point"""
    deaths_std: float
    """Standard deviation of deaths at this time point"""
    denies_avg: float
    """Average lane creeps denied at this time point"""
    denies_std: float
    """Standard deviation of `denies_avg` at this time point"""
    game_time: int
    """The time point of the data. If `resolution` (default 10) is > 0, this is a percentage (0, 10, ..., 100). If `resolution` is 0, this is the match time in seconds."""
    game_time_avg: float
    """Where in the match the stats snapshots of this point were taken on average, in the unit of `game_time`. Snapshots are taken every few minutes and at the end of the match, so with `resolution` > 0 a point holds the snapshots from `game_time` up to the next point and this is usually about half a bucket later than `game_time`. Percentages are averaged from whole percents, so they can be off by a few tenths."""
    gold_ability_assassinate_avg: float
    """Average souls earned from the Assassinate ability at this time point"""
    gold_ability_assassinate_std: float
    """Standard deviation of `gold_ability_assassinate_avg` at this time point"""
    gold_assists_avg: float
    """Average souls earned from assists at this time point (part of `gold_player_avg`)"""
    gold_assists_std: float
    """Standard deviation of `gold_assists_avg` at this time point"""
    gold_boss_avg: float
    """Average souls earned from objectives at this time point"""
    gold_boss_orb_avg: float
    """Average souls earned from secured objective orbs at this time point"""
    gold_boss_orb_std: float
    """Standard deviation of `gold_boss_orb_avg` at this time point"""
    gold_boss_std: float
    """Standard deviation of `gold_boss_avg` at this time point"""
    gold_breakable_avg: float
    """Average souls earned from breakables (crates, statues) at this time point"""
    gold_breakable_std: float
    """Standard deviation of `gold_breakable_avg` at this time point"""
    gold_death_loss_avg: float
    """Average souls lost on death at this time point"""
    gold_death_loss_std: float
    """Standard deviation of `gold_death_loss_avg` at this time point"""
    gold_denied_avg: float
    """Average souls denied to enemies at this time point"""
    gold_denied_std: float
    """Standard deviation of `gold_denied_avg` at this time point"""
    gold_item_cultist_sacrifice_avg: float
    """Average souls earned from the Cultist Sacrifice item at this time point"""
    gold_item_cultist_sacrifice_std: float
    """Standard deviation of `gold_item_cultist_sacrifice_avg` at this time point"""
    gold_item_goose_egg_avg: float
    """Average souls earned from the Golden Goose Egg item at this time point"""
    gold_item_goose_egg_std: float
    """Standard deviation of `gold_item_goose_egg_avg` at this time point"""
    gold_item_trophy_collector_avg: float
    """Average souls earned from the Trophy Collector item at this time point"""
    gold_item_trophy_collector_std: float
    """Standard deviation of `gold_item_trophy_collector_avg` at this time point"""
    gold_lane_creep_avg: float
    """Average souls earned from lane creeps at this time point"""
    gold_lane_creep_orbs_avg: float
    """Average souls earned from secured lane-creep orbs at this time point"""
    gold_lane_creep_orbs_std: float
    """Standard deviation of `gold_lane_creep_orbs_avg` at this time point"""
    gold_lane_creep_std: float
    """Standard deviation of `gold_lane_creep_avg` at this time point"""
    gold_neutral_creep_avg: float
    """Average souls earned from neutral (jungle) creeps at this time point"""
    gold_neutral_creep_orbs_avg: float
    """Average souls earned from secured neutral-creep orbs at this time point"""
    gold_neutral_creep_orbs_std: float
    """Standard deviation of `gold_neutral_creep_orbs_avg` at this time point"""
    gold_neutral_creep_std: float
    """Standard deviation of `gold_neutral_creep_avg` at this time point"""
    gold_player_avg: float
    """Average souls earned from hero kills at this time point, including assist souls (see `gold_assists_avg`)"""
    gold_player_orbs_avg: float
    """Average souls earned from secured hero-kill orbs at this time point"""
    gold_player_orbs_std: float
    """Standard deviation of `gold_player_orbs_avg` at this time point"""
    gold_player_std: float
    """Standard deviation of `gold_player_avg` at this time point"""
    gold_team_bonus_avg: float
    """Average souls earned from the team bonus at this time point"""
    gold_team_bonus_std: float
    """Standard deviation of `gold_team_bonus_avg` at this time point"""
    gold_treasure_avg: float
    """Average souls earned from the urn at this time point"""
    gold_treasure_std: float
    """Standard deviation of `gold_treasure_avg` at this time point"""
    kills_avg: float
    """Average kills at this time point"""
    kills_std: float
    """Standard deviation of kills at this time point"""
    net_worth_avg: float
    """Average net worth at this time point"""
    net_worth_std: float
    """Standard deviation of net worth at this time point"""
    neutral_damage_avg: float
    """Average damage dealt to neutral (jungle) creeps at this time point"""
    neutral_damage_std: float
    """Standard deviation of `neutral_damage_avg` at this time point"""
    neutral_kills_avg: float
    """Average neutral (jungle) creeps killed at this time point"""
    neutral_kills_std: float
    """Standard deviation of `neutral_kills_avg` at this time point"""
    permanent_buffs_avg: NotRequired[float | None]
    """Average permanent buff (power-up) pickups collected up to this time point. Only matches since build 6712 (2026-09-29) record pickup times, so only players with at least one timed permanent pickup count; `null` when there are none."""
    permanent_buffs_std: NotRequired[float | None]
    """Standard deviation of `permanent_buffs_avg` at this time point; `null` when there are no players with timed permanent pickups."""
    player_barriering_avg: float
    """Average barrier (shield) provided at this time point"""
    player_barriering_std: float
    """Standard deviation of `player_barriering_avg` at this time point"""
    player_damage_avg: float
    """Average damage dealt to enemy heroes at this time point"""
    player_damage_std: float
    """Standard deviation of `player_damage_avg` at this time point"""
    player_healing_avg: float
    """Average healing done at this time point"""
    player_healing_std: float
    """Standard deviation of `player_healing_avg` at this time point"""
    samples: int
    """Number of stats snapshots (one per player per snapshot time) averaged in this point. Each match has a snapshot at 100%, but only some matches have one in any earlier bucket, and longer matches more often."""
    self_damage_avg: float
    """Average self-inflicted damage at this time point"""
    self_damage_std: float
    """Standard deviation of `self_damage_avg` at this time point"""


class Rank(TypedDict):
    color: str
    images: RankImages
    name: str
    tier: int


class RankDistributionEntry(TypedDict):
    badge: int
    """Rank badge, `tier * 10 + subrank`. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    players: int
    """Number of players whose rank at the end of their latest ranked match in the filtered range is this badge."""
    rank: int
    """Rank tier."""
    subrank: int
    """Sub-rank within the tier."""


class RankImages(TypedDict):
    """Image URLs for a single rank tier. Field declaration order is load-bearing: it sets the JSON key order, which is stable across versions of this API."""
    chalk: NotRequired[str | None]
    chalk_webp: NotRequired[str | None]
    large: NotRequired[str | None]
    large_subrank1: NotRequired[str | None]
    large_subrank1_webp: NotRequired[str | None]
    large_subrank2: NotRequired[str | None]
    large_subrank2_webp: NotRequired[str | None]
    large_subrank3: NotRequired[str | None]
    large_subrank3_webp: NotRequired[str | None]
    large_subrank4: NotRequired[str | None]
    large_subrank4_webp: NotRequired[str | None]
    large_subrank5: NotRequired[str | None]
    large_subrank5_webp: NotRequired[str | None]
    large_subrank6: NotRequired[str | None]
    large_subrank6_webp: NotRequired[str | None]
    large_webp: NotRequired[str | None]
    small: NotRequired[str | None]
    small_subrank1: NotRequired[str | None]
    small_subrank1_webp: NotRequired[str | None]
    small_subrank2: NotRequired[str | None]
    small_subrank2_webp: NotRequired[str | None]
    small_subrank3: NotRequired[str | None]
    small_subrank3_webp: NotRequired[str | None]
    small_subrank4: NotRequired[str | None]
    small_subrank4_webp: NotRequired[str | None]
    small_subrank5: NotRequired[str | None]
    small_subrank5_webp: NotRequired[str | None]
    small_subrank6: NotRequired[str | None]
    small_subrank6_webp: NotRequired[str | None]
    small_webp: NotRequired[str | None]
    subrank1: NotRequired[str | None]
    """Tier badge with the division numeral drawn on it, composed on demand by this API."""
    subrank1_webp: NotRequired[str | None]
    subrank2: NotRequired[str | None]
    subrank2_webp: NotRequired[str | None]
    subrank3: NotRequired[str | None]
    subrank3_webp: NotRequired[str | None]
    subrank4: NotRequired[str | None]
    subrank4_webp: NotRequired[str | None]
    subrank5: NotRequired[str | None]
    subrank5_webp: NotRequired[str | None]
    subrank6: NotRequired[str | None]
    subrank6_webp: NotRequired[str | None]


class RankResponse(TypedDict):
    badge: int
    """Rank badge, `tier * 10 + subrank`, including the progress the last ranked match awarded. Eternus subranks are percentile-based and refreshed daily by Valve, so within Eternus this is the badge the player entered their latest ranked match with. `0` when no recent ranked match reports a rank. See more: <https://api.deadlock-api.com/v1/assets/ranks>"""
    last_match: NotRequired[LastRankedMatch | None]
    rank: int
    """Rank tier, `0` when unknown."""
    subrank: int
    """Sub-rank within the tier, `0` when unknown."""


class RankedSeason(TypedDict):
    base_win_loss_point_grant: NotRequired[int | None]
    """Base rank points granted per win / taken per loss (build 6701+)."""
    calibration_matches: int
    class_name: str
    intervals: list[SeasonInterval]
    min_hero_unlocks: int
    min_hero_wins: int
    min_wins: int
    name: str
    ranked_type: str
    valid_party_sizes: list[int]


class RawAbilityUpgrade(TypedDict):
    property_upgrades: NotRequired[list[RawAbilityUpgradePropertyUpgrade]]


class RawAbilityUpgradePropertyUpgrade(TypedDict):
    bonus: str
    fixed_corrupted_bonus: NotRequired[bool | None]
    """Corrupted item bonuses only (build 6711+)."""
    name: str
    round_corrupted_bonus: NotRequired[bool | None]
    """Corrupted item bonuses only (build 6711+)."""
    scale_stat_filter: NotRequired[str | None]
    upgrade_type: NotRequired[str | None]


class RawCustomCrosshairSettings(TypedDict):
    m_DotColor: NotRequired[list[int] | None]
    m_DotOutlineColor: NotRequired[list[int] | None]
    m_PipColor: NotRequired[list[int] | None]
    m_PipOutlineColor: NotRequired[list[int] | None]
    m_SpreadIndicatingElement: NotRequired[str | None]
    m_flBaseSpread: NotRequired[float | None]
    m_flDotOpacity: NotRequired[float | None]
    m_flDotOutlineOpacity: NotRequired[float | None]
    m_flPipOpacity: NotRequired[float | None]
    m_flPipOutlineOpacity: NotRequired[float | None]
    m_nDotOutlineGap: NotRequired[int | None]
    m_nDotOutlineWidth: NotRequired[int | None]
    m_nDotRadius: NotRequired[int | None]
    m_nPipHeight: NotRequired[int | None]
    m_nPipOutlineGap: NotRequired[int | None]
    m_nPipOutlineWidth: NotRequired[int | None]
    m_nPipWidth: NotRequired[int | None]


class RawItemPropertyScaleFunctionSubclass(TypedDict):
    class_name: NotRequired[str | None]
    scaling_stats: NotRequired[list[str] | None]
    specific_stat_scale_type: NotRequired[str | None]
    stat_scale: NotRequired[float | None]
    street_brawl_stat_scale: NotRequired[float | None]
    subclass_name: NotRequired[str | None]


class RawItemWeaponInfoBulletSpeedCurve(TypedDict):
    domain_maxs: list[float]
    domain_mins: list[float]
    spline: NotRequired[list[RawItemWeaponInfoBulletSpeedCurveSpline] | None]


class RawItemWeaponInfoBulletSpeedCurveSpline(TypedDict):
    slope_incoming: float
    slope_outgoing: float
    x: float
    y: float


class RawItemWeaponInfoInner(TypedDict):
    m_BulletSpeedCurve: NotRequired[RawItemWeaponInfoBulletSpeedCurve | None]


class RawWeaponInfoHorizontalRecoil(TypedDict):
    burst_exponent: NotRequired[float | None]
    range: NotRequired[Any]


class RawWeaponInfoVerticalRecoil(TypedDict):
    burst_constant: NotRequired[float | None]
    burst_exponent: NotRequired[float | None]
    burst_slope: NotRequired[float | None]
    range: NotRequired[Any]


RecoilRange: TypeAlias = "list[float] | float"
"""Recoil `m_Range` is either a `[min, max]` array or a single scalar."""


RegionMode: TypeAlias = "Literal[\"row\", \"europe\", \"se_asia\", \"s_america\", \"russia\", \"oceania\"]"


class RejuvParams(TypedDict):
    player_respawn_mult: list[float]
    rejuvinator_buff_duration: float
    rejuvinator_drop_duration: float
    rejuvinator_drop_height: float
    rejuvinator_expiration_warning_timing: float
    rejuvinator_rebirth_duration: list[float]
    trooper_health_mult: list[float]


class ReplaceSteamAccountRequest(TypedDict):
    """Request body for replacing a Steam account"""
    steam_id3: int
    """New Steam ID3 (32-bit unsigned integer format)"""


RollType: TypeAlias = "str"
"""Known values for `m_eRollType`. Unknown values pass through unchanged so a newly-introduced roll type doesn't 500. Known values: `ECitadelRandomRoll_BreakablePowerupPickup`, `ECitadelRandomRoll_BreakableGoldPickup`."""


class ScriptValues(TypedDict):
    modifier_value: NotRequired[str | None]
    value: NotRequired[float | None]


class SeasonInterval(TypedDict):
    end_timestamp: int
    """Unix timestamp (seconds) at which the interval ends."""
    interval: int
    leaderboard_id: NotRequired[int | None]
    """Leaderboard backing this interval (build 6701+)."""
    start_timestamp: int
    """Unix timestamp (seconds) at which the interval starts."""


ServerRegion: TypeAlias = "Literal[\"europe\", \"eu_amsterdam\", \"eu_poland\", \"eu_stockholm\", \"eu_helsinki\", \"eu_falkenstein\", \"eu_spain\", \"eu_east\", \"eu_london\", \"south_africa\", \"us_west\", \"us_east\", \"us_north_central\", \"us_south_central\", \"us_south_east\", \"us_south_west\", \"australia\", \"singapore\", \"japan\", \"hong_kong\", \"mp_hong_kong\", \"seoul\", \"chile\", \"peru\", \"argentina\", \"south_america\"]"


class Settings(TypedDict):
    """Crosshair convars. Anything not given keeps the game's default."""
    color_b: NotRequired[int]
    color_g: NotRequired[int]
    color_r: NotRequired[int]
    dot_opacity: NotRequired[float]
    """0 to 1."""
    dot_outline_border: NotRequired[int]
    dot_outline_gap: NotRequired[int]
    dot_outline_opacity: NotRequired[float]
    """0 to 1."""
    dot_size: NotRequired[int]
    outline_color_b: NotRequired[int]
    outline_color_g: NotRequired[int]
    outline_color_r: NotRequired[int]
    pip_gap: NotRequired[int]
    pip_gap_static: NotRequired[bool]
    """Keep the pips at a fixed distance instead of spreading them with weapon spread."""
    pip_height: NotRequired[int]
    pip_opacity: NotRequired[float]
    """0 to 1."""
    pip_outline_border: NotRequired[int]
    pip_outline_gap: NotRequired[int]
    pip_outline_opacity: NotRequired[float]
    """0 to 1."""
    pip_width: NotRequired[int]
    themed: NotRequired[bool]
    """Use the hero's own crosshair instead of these settings."""


class ShopSpiritStatsDisplay(TypedDict):
    display_stats: list[str]


class ShopStatDisplay(TypedDict):
    spirit_stats_display: ShopSpiritStatsDisplay
    vitality_stats_display: ShopVitalityStatsDisplay
    weapon_stats_display: ShopWeaponStatsDisplay


class ShopVitalityStatsDisplay(TypedDict):
    display_stats: list[str]
    other_display_stats: list[str]


class ShopWeaponStatsDisplay(TypedDict):
    display_stats: list[str]
    other_display_stats: list[str]
    weapon_attributes: NotRequired[list[str] | None]
    weapon_image: NotRequired[str | None]
    weapon_image_webp: NotRequired[str | None]


class SlotsSummary(TypedDict):
    """Summary of the patron's Steam account slots"""
    available_slots: int
    slots_in_cooldown: int
    total_slots: int
    used_slots: int


class SourceLocation(TypedDict):
    chain: NotRequired[list[str]]
    column: int
    component: NotRequired[str | None]
    file: str
    line: int


SpreadPenalty: TypeAlias = "list[float] | str"
"""Source data emits spread penalties as either a list of floats or a string (sometimes a comma-separated list, sometimes a literal label)."""


class StartingStat(TypedDict):
    display_stat_name: str
    value: float


class StartingStats(TypedDict):
    ability_resource_max: StartingStat
    ability_resource_regen_per_second: StartingStat
    air_dash_distance_in_meters: NotRequired[StartingStat | None]
    air_dash_duration: NotRequired[StartingStat | None]
    base_health_regen: StartingStat
    bullet_armor_damage_reduction: NotRequired[StartingStat | None]
    crit_damage_received_scale: StartingStat
    crouch_speed: StartingStat
    ground_dash_distance_in_meters: NotRequired[StartingStat | None]
    ground_dash_duration: NotRequired[StartingStat | None]
    heavy_melee_damage: StartingStat
    light_melee_damage: StartingStat
    max_health: StartingStat
    max_move_speed: StartingStat
    move_acceleration: StartingStat
    ooc_health_regen: NotRequired[StartingStat | None]
    proc_build_up_rate_scale: StartingStat
    reload_speed: StartingStat
    sprint_speed: StartingStat
    stamina: StartingStat
    stamina_regen_per_second: StartingStat
    tech_armor_damage_reduction: NotRequired[StartingStat | None]
    tech_duration: StartingStat
    tech_range: StartingStat
    weapon_power: StartingStat
    weapon_power_scale: StartingStat


class StatsDisplay(TypedDict):
    health_header_stats: list[str]
    health_stats: list[str]
    magic_header_stats: list[str]
    magic_stats: list[str]
    weapon_header_stats: list[str]
    weapon_stats: list[str]


StatsUsageFlag: TypeAlias = "Literal[\"ConditionallyApplied\", \"ConditionallyEnemyApplied\", \"IntrinsicallyProvidedInAbility\", \"IntrinsicallyProvidedInModifier\"]"


class Status(TypedDict):
    services: StatusServices
    """Status of the services."""


class StatusServices(TypedDict):
    clickhouse: bool
    """Whether Clickhouse is reachable."""
    postgres: bool
    """Whether Postgres is reachable."""
    redis: bool
    """Whether Redis is reachable."""


class SteamAccountListItem(TypedDict):
    """Response for a Steam account in the list endpoint (includes `is_in_cooldown`)"""
    created_at: str
    deleted_at: NotRequired[str | None]
    id: str
    is_in_cooldown: bool
    steam_id3: int


class SteamAccountResponse(TypedDict):
    """Response for a Steam account"""
    created_at: str
    deleted_at: NotRequired[str | None]
    id: str
    steam_id3: int


class SteamFriend(TypedDict):
    account_id: int
    friend_since: str


class SteamInfo(TypedDict):
    """Per-patch Steam manifest as served by the public assets API. Field order is load-bearing — it sets the JSON key order."""
    app_id: int
    client_version: int
    product_name: str
    server_app_id: int
    server_version: int
    source_revision: int
    tools_app_id: int
    version_date: str
    version_datetime: str
    """`version_date` + `version_time` combined into a naive ISO-8601 string (`YYYY-MM-DDTHH:MM:SS`, no timezone)."""
    version_time: str


class SteamNews(TypedDict):
    content: str
    guid: PatchGuid
    link: str
    pub_date: str
    title: str


class SteamProfile(TypedDict):
    account_id: int
    avatar: str
    avatarfull: str
    avatarmedium: str
    countrycode: NotRequired[str | None]
    friends: list[SteamFriend]
    last_team_avg_badge: NotRequired[int | None]
    last_updated: str
    matches_played_last_30d: int
    personaname: str
    profileurl: str
    realname: NotRequired[str | None]


class StreetBrawl(TypedDict):
    apper_round: list[int]
    buy_time: list[int]
    buy_time_grace_period: float
    comeback_bonus_health: int
    comeback_bonus_health_critical: int
    corrupt_item_round: NotRequired[int | None]
    """Round in which players may corrupt an item (build 6711+)."""
    gold_per_round: list[int]
    item_draft_rerolls_per_round: list[int]
    item_draft_rounds_per_game_round: list[ItemDraftRoundPerGameRound]
    item_drafts: dict[str, DraftBuckets]
    lane_number: int
    objective_max_health: list[int]
    overtime_respawn_time_increase: list[float]
    overtime_respawn_time_increase_urgent: list[float]
    overtime_trooper_damage_scale: list[float]
    overtime_trooper_health_scale: list[float]
    pre_buy_time: list[float]
    respawn_times: list[int]
    round_length_minutes: list[int]
    round_length_minutes_urgent: list[float]
    score_to_win: int
    scoring_time: float
    tier1_max_resist_time: float
    tier2_bonus_health: int
    tier2_max_resist_time: float
    trooper_spawn_before_round_start_timer: float
    trooper_spawn_timer: list[float]
    ultimate_unlock_round: int
    zip_boost_cooldown_on_start: float


class Subclass_BulletResistModifierSubclass(TypedDict):
    bullet_resist: NotRequired[int | None]
    bullet_resist_reduction_per_hero: NotRequired[int | None]


class Subclass_BulletResistModifier(TypedDict):
    """Serializes back as `{"subclass": ...}` to preserve the KV3 wrapper shape in JSON output."""
    subclass: Subclass_BulletResistModifierSubclass


class Subclass_EmpoweredModifierLevelSubclass(TypedDict):
    max_health: NotRequired[int | None]
    model_scale: NotRequired[float | None]
    transition_duration: NotRequired[float | None]


class Subclass_EmpoweredModifierLevel(TypedDict):
    """Serializes back as `{"subclass": ...}` to preserve the KV3 wrapper shape in JSON output."""
    subclass: Subclass_EmpoweredModifierLevelSubclass


class Subclass_IntrinsicModifiersSubclass(TypedDict):
    script_values: NotRequired[list[ScriptValues] | None]


class Subclass_IntrinsicModifiers(TypedDict):
    """Serializes back as `{"subclass": ...}` to preserve the KV3 wrapper shape in JSON output."""
    subclass: Subclass_IntrinsicModifiersSubclass


class Subclass_ModifierDefinitionSubclass(TypedDict):
    always_show_in_ui: NotRequired[list[str] | None]
    class_name: NotRequired[str | None]
    duration: NotRequired[float | None]
    enabled_state_mask: NotRequired[str | None]
    """Modifier states the modifier enables, e.g. `MODIFIER_STATE_IN_CORRUPTED_ITEM_SHOP`."""
    modifier_values: NotRequired[list[ModifierValue] | None]
    script_values: NotRequired[list[ModifierValue] | None]
    subclass_name: NotRequired[str | None]
    time_max: NotRequired[float | None]
    time_min: NotRequired[float | None]


class Subclass_ModifierDefinition(TypedDict):
    """Serializes back as `{"subclass": ...}` to preserve the KV3 wrapper shape in JSON output."""
    subclass: Subclass_ModifierDefinitionSubclass


class Subclass_NeutralDamageGrowthSubclass(TypedDict):
    damage_growth_pct_per_min: NotRequired[float | None]


class Subclass_NeutralDamageGrowth(TypedDict):
    """Serializes back as `{"subclass": ...}` to preserve the KV3 wrapper shape in JSON output."""
    subclass: Subclass_NeutralDamageGrowthSubclass


class Subclass_ObjectiveHealthGrowthPhaseSubclass(TypedDict):
    growth_per_minute: NotRequired[int | None]
    growth_start_time_in_minutes: NotRequired[int | None]
    tick_rate: NotRequired[float | None]


class Subclass_ObjectiveHealthGrowthPhase(TypedDict):
    """Serializes back as `{"subclass": ...}` to preserve the KV3 wrapper shape in JSON output."""
    subclass: Subclass_ObjectiveHealthGrowthPhaseSubclass


class Subclass_ObjectiveRegenSubclass(TypedDict):
    out_of_combat_health_regen: NotRequired[float | None]
    out_of_combat_regen_delay: NotRequired[float | None]


class Subclass_ObjectiveRegen(TypedDict):
    """Serializes back as `{"subclass": ...}` to preserve the KV3 wrapper shape in JSON output."""
    subclass: Subclass_ObjectiveRegenSubclass


class Subclass_RangedArmorModifierSubclass(TypedDict):
    invuln_range: NotRequired[float | None]
    range_max: NotRequired[float | None]
    range_min: NotRequired[float | None]


class Subclass_RangedArmorModifier(TypedDict):
    """Serializes back as `{"subclass": ...}` to preserve the KV3 wrapper shape in JSON output."""
    subclass: Subclass_RangedArmorModifierSubclass


class Subclass_TrooperDamageReductionSubclass(TypedDict):
    damage_reduction_for_troopers: NotRequired[float | None]


class Subclass_TrooperDamageReduction(TypedDict):
    """Serializes back as `{"subclass": ...}` to preserve the KV3 wrapper shape in JSON output."""
    subclass: Subclass_TrooperDamageReductionSubclass


class TableSchemaResponse(TypedDict):
    columns: list[ColumnSchema]
    kind: str
    """`entity` for tables discovered from the demo's send-tables, `event` for the event tables common to every demo."""
    name: str


class TableSize(TypedDict):
    data_compressed_bytes: NotRequired[int | None]
    """Compressed size of the table in bytes."""
    data_uncompressed_bytes: NotRequired[int | None]
    """Uncompressed size of the table in bytes."""
    is_view: bool
    """Whether the table is a view."""
    rows: NotRequired[int | None]
    """Number of rows in the table."""


class TeamModels(TypedDict):
    """Published pose GLBs (see `NpcUnit::models`) of a per-team model pair."""
    amber: NotRequired[dict[str, str]]
    sapphire: NotRequired[dict[str, str]]


class TooltipDetailsBlock(TypedDict):
    loc_string: NotRequired[str | None]
    properties: NotRequired[list[TooltipDetailsBlockProperty] | None]


class TooltipDetailsBlockProperty(TypedDict):
    important_property: NotRequired[str | None]
    important_property_icon: NotRequired[str | None]
    requires_ability_upgrade: NotRequired[bool | None]
    show_property_value: NotRequired[bool | None]
    status_effect_name: NotRequired[str | None]
    status_effect_value: NotRequired[str | None]


class TooltipDetailsInfoSection(TypedDict):
    basic_properties: NotRequired[list[str] | None]
    loc_string: NotRequired[str | None]
    properties_block: NotRequired[list[TooltipDetailsBlock] | None]
    property_upgrade_required: NotRequired[str | None]


class Upgrade(TypedDict):
    activation: AbilityActivation
    class_name: str
    component_items: NotRequired[list[str] | None]
    corrupted_info: NotRequired[CorruptedItemInfo | None]
    cost: NotRequired[int | None]
    description: NotRequired[UpgradeDescription | None]
    disable_item_target: NotRequired[str | None]
    disabled: NotRequired[bool | None]
    disabled_shop_filters: NotRequired[list[str] | None]
    """Shop filters (`snake_case` `EShopFilter*` names) this item is hidden from even though its stats would match them."""
    hero: NotRequired[int | None]
    heroes: NotRequired[list[int] | None]
    id: int
    image: NotRequired[str | None]
    image_webp: NotRequired[str | None]
    imbue: NotRequired[AbilityImbue | None]
    is_active_item: bool
    item_slot_type: ItemSlotType
    item_tier: int
    name: str
    properties: NotRequired[dict[str, UpgradeProperty] | None]
    shop_filters: NotRequired[list[str] | None]
    """Extra shop filters (`snake_case` `EShopFilter*` names, e.g. `status_grounded`) this item shows up under, beyond those derived from its stats."""
    shop_image: NotRequired[str | None]
    shop_image_small: NotRequired[str | None]
    shop_image_small_webp: NotRequired[str | None]
    shop_image_webp: NotRequired[str | None]
    shop_version: NotRequired[int | None]
    shopable: bool
    start_trained: NotRequired[bool | None]
    tooltip_sections: NotRequired[list[UpgradeTooltipSection] | None]
    type: ItemType
    update_time: NotRequired[int | None]
    upgrades: NotRequired[list[RawAbilityUpgrade] | None]
    weapon_info: NotRequired[RawItemWeaponInfoInner | None]


class UpgradeDescription(TypedDict):
    active: NotRequired[str | None]
    desc: NotRequired[str | None]
    desc2: NotRequired[str | None]
    passive: NotRequired[str | None]


UpgradeProperty: TypeAlias = "dict[str, Any]"


class UpgradeTooltipImportantPropertyWithIcon(TypedDict):
    icon: NotRequired[str | None]
    localized_name: NotRequired[str | None]
    name: NotRequired[str | None]


class UpgradeTooltipSection(TypedDict):
    section_attributes: NotRequired[list[UpgradeTooltipSectionAttribute] | None]
    section_type: NotRequired[AbilitySectionType | None]


class UpgradeTooltipSectionAttribute(TypedDict):
    elevated_properties: NotRequired[list[str] | None]
    important_properties: NotRequired[list[str] | None]
    important_properties_with_icon: NotRequired[list[UpgradeTooltipImportantPropertyWithIcon] | None]
    loc_string: NotRequired[str | None]
    properties: NotRequired[list[str] | None]


VariableCategory: TypeAlias = "Literal[\"General\", \"Daily\", \"Hero\", \"Item\", \"Leaderboard\", \"Season\", \"Overall\"]"


class VariableDescription(TypedDict):
    category: VariableCategory
    """The category of the variable."""
    default_label: NotRequired[str | None]
    """The default label for the variable."""
    description: str
    """The description of the variable."""
    extra_args: list[str]
    """Extra arguments that can be passed to the variable."""
    name: str
    """The name of the variable."""


class VerticalRecoil(TypedDict):
    burst_constant: NotRequired[float | None]
    burst_exponent: NotRequired[float | None]
    burst_slope: NotRequired[float | None]
    range: NotRequired[RecoilRange | None]


class Viewport(TypedDict):
    device_pixel_ratio: float
    height: int
    width: int


class Weapon(TypedDict):
    class_name: str
    crosshair_css_class: NotRequired[str | None]
    custom_crosshair_settings: NotRequired[RawCustomCrosshairSettings | None]
    hero: NotRequired[int | None]
    heroes: NotRequired[list[int] | None]
    id: int
    image: NotRequired[str | None]
    image_webp: NotRequired[str | None]
    name: str
    properties: NotRequired[dict[str, ItemProperty] | None]
    start_trained: NotRequired[bool | None]
    type: ItemType
    update_time: NotRequired[int | None]
    use_custom_crosshair_settings: NotRequired[bool | None]
    weapon_info: NotRequired[WeaponInfo | None]


class WeaponInfo(TypedDict):
    aiming_shot_spread_penalty: NotRequired[Any]
    build_up_rate: NotRequired[float | None]
    bullet_damage: NotRequired[float | None]
    bullet_gravity_scale: NotRequired[float | None]
    bullet_handler_type: NotRequired[str | None]
    bullet_inherit_shooter_velocity_scale: NotRequired[float | None]
    bullet_lifetime: NotRequired[float | None]
    bullet_radius: NotRequired[float | None]
    bullet_radius_vs_world: NotRequired[float | None]
    bullet_reflect_amount: NotRequired[float | None]
    bullet_reflect_scale: NotRequired[float | None]
    bullet_speed: NotRequired[float | None]
    bullet_speed_curve: NotRequired[RawItemWeaponInfoBulletSpeedCurve | None]
    bullet_whiz_distance: NotRequired[float | None]
    bullets: NotRequired[int | None]
    bullets_per_second: NotRequired[float | None]
    bullets_per_second_with_reload: NotRequired[float | None]
    burst_shot_cooldown: NotRequired[float | None]
    burst_shot_count: NotRequired[int | None]
    can_zoom: NotRequired[bool | None]
    clip_size: NotRequired[int | None]
    crit_bonus_against_npcs: NotRequired[float | None]
    crit_bonus_end: NotRequired[float | None]
    crit_bonus_end_range: NotRequired[float | None]
    crit_bonus_start: NotRequired[float | None]
    crit_bonus_start_range: NotRequired[float | None]
    cycle_time: NotRequired[float | None]
    damage_falloff_bias: NotRequired[float | None]
    damage_falloff_end_range: NotRequired[float | None]
    damage_falloff_end_scale: NotRequired[float | None]
    damage_falloff_start_range: NotRequired[float | None]
    damage_falloff_start_scale: NotRequired[float | None]
    damage_per_magazine: NotRequired[float | None]
    damage_per_second: NotRequired[float | None]
    damage_per_second_with_reload: NotRequired[float | None]
    damage_per_shot: NotRequired[float | None]
    horizontal_punch: NotRequired[float | None]
    horizontal_recoil: NotRequired[RawWeaponInfoHorizontalRecoil | None]
    intra_burst_cycle_time: NotRequired[float | None]
    is_semi_auto: NotRequired[bool | None]
    low_ammo_indicator_threshold: NotRequired[float | None]
    max_spin_cycle_time: NotRequired[float | None]
    range: NotRequired[float | None]
    recoil_recovery_delay_factor: NotRequired[float | None]
    recoil_recovery_speed: NotRequired[float | None]
    recoil_seed: NotRequired[float | None]
    recoil_shot_index_recovery_time_factor: NotRequired[float | None]
    recoil_speed: NotRequired[float | None]
    recycle_time: NotRequired[float | None]
    reload_duration: NotRequired[float | None]
    reload_move_speed: NotRequired[float | None]
    reload_single_bullets: NotRequired[bool | None]
    reload_single_bullets_allow_cancel: NotRequired[bool | None]
    reload_single_bullets_initial_delay: NotRequired[float | None]
    scatter_yaw_scale: NotRequired[float | None]
    semi_auto_cycle_rate: NotRequired[float | None]
    shoot_move_speed_percent: NotRequired[float | None]
    shoot_spread_penalty_decay: NotRequired[float | None]
    shoot_spread_penalty_decay_delay: NotRequired[float | None]
    shoot_spread_penalty_per_shot: NotRequired[float | None]
    shooting_up_spread_penalty: NotRequired[float | None]
    shots_per_second: NotRequired[float | None]
    shots_per_second_with_reload: NotRequired[float | None]
    spin_decay_rate: NotRequired[float | None]
    spin_increase_rate: NotRequired[float | None]
    spins_up: NotRequired[bool | None]
    spread: NotRequired[float | None]
    standing_shot_spread_penalty: NotRequired[Any]
    standing_spread: NotRequired[float | None]
    vertical_punch: NotRequired[float | None]
    vertical_recoil: NotRequired[RawWeaponInfoVerticalRecoil | None]
    zoom_fov: NotRequired[float | None]
    zoom_move_speed_percent: NotRequired[float | None]


class ZiplanePath(TypedDict):
    """A single lane's zip-line cubic spline."""
    P0_points: list[list[float]]
    P1_points: list[list[float]]
    P2_points: list[list[float]]
    color: str
    color_parsed: Color
    origin: list[float]
