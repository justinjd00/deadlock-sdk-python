"""Steam ids, ranks, modes and stats. Pure functions, no client needed."""

from __future__ import annotations

import math
import re
import unicodedata
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Literal, TypeVar

from .errors import DeadlockError, invalid_input

T = TypeVar("T")

# --- Steam ids ---------------------------------------------------------------

#: Offset between a 32-bit account id and a SteamID64 for individual accounts.
STEAM_ID64_BASE = 76561197960265728
_MAX_ACCOUNT_ID = 0xFFFFFFFF

#: Account id, SteamID64, ``[U:1:x]``, ``STEAM_1:Y:Z`` or a ``/profiles/`` URL.
PlayerInput = int | str


def _not_an_id(raw: object) -> DeadlockError:
    return invalid_input(f"{raw!r} is not a Steam account id, SteamID64, SteamID3 or profile URL.")


def _from_int(value: int, raw: object) -> int:
    if 0 <= value <= _MAX_ACCOUNT_ID:
        return value
    account = value - STEAM_ID64_BASE
    if 0 <= account <= _MAX_ACCOUNT_ID:
        return account
    raise _not_an_id(raw)


def to_account_id(player: PlayerInput) -> int:
    """Converts any supported Steam identifier to the 32-bit account id the API uses."""
    if isinstance(player, bool):
        raise _not_an_id(player)
    if isinstance(player, int):
        return _from_int(player, player)
    if not isinstance(player, str):
        raise _not_an_id(player)
    raw = player.strip()
    if m := re.fullmatch(r"\[?U:1:(\d+)\]?", raw, re.IGNORECASE):
        return _from_int(int(m[1]), raw) if int(m[1]) <= _MAX_ACCOUNT_ID else _raise(raw)
    if m := re.fullmatch(r"STEAM_[0-5]:([01]):(\d+)", raw, re.IGNORECASE):
        account = int(m[2]) * 2 + int(m[1])
        return account if account <= _MAX_ACCOUNT_ID else _raise(raw)
    if m := re.search(r"steamcommunity\.com/profiles/(\d{17})", raw, re.IGNORECASE):
        return _from_int(int(m[1]), raw)
    if re.search(r"steamcommunity\.com/id/", raw, re.IGNORECASE):
        raise invalid_input(
            f"{raw!r} is a custom (vanity) Steam URL and cannot be converted offline. "
            "Use players.search(name) or Steam's ResolveVanityURL to get the id."
        )
    if raw.isdigit():
        return _from_int(int(raw), raw)
    raise _not_an_id(raw)


def _raise(raw: str) -> int:
    raise _not_an_id(raw)


def to_steam_id64(player: PlayerInput) -> str:
    return str(to_account_id(player) + STEAM_ID64_BASE)


def to_steam_id3(player: PlayerInput) -> str:
    return f"[U:1:{to_account_id(player)}]"


def to_steam_id2(player: PlayerInput) -> str:
    account = to_account_id(player)
    return f"STEAM_1:{account % 2}:{account // 2}"


def steam_profile_url(player: PlayerInput) -> str:
    return f"https://steamcommunity.com/profiles/{to_steam_id64(player)}"


def is_player_input(value: object) -> bool:
    try:
        to_account_id(value)  # type: ignore[arg-type]
    except DeadlockError:
        return False
    return True


# --- Ranks -------------------------------------------------------------------

#: Rank names by tier. The client prefers live names from the API when it has them.
RANK_NAMES: tuple[str, ...] = (
    "Obscurus",
    "Initiate",
    "Seeker",
    "Acolyte",
    "Sentinel",
    "Mystic",
    "Ritualist",
    "Emissary",
    "Oracle",
    "Phantom",
    "Ascendant",
    "Eternus",
)


@dataclass(frozen=True)
class Badge:
    """A decoded rank badge: ``badge = tier * 10 + subrank``."""

    badge: int
    tier: int
    subrank: int
    name: str
    #: ``"Eternus 5"`` or ``"Obscurus"``.
    label: str
    image: str | None = None
    color: str | None = None


def decode_badge(badge: int, ranks: Sequence[Mapping[str, Any]] | None = None) -> Badge:
    """Decodes a badge like ``115`` to Eternus 5. Pass ``client.ranks.list()`` for live names and icons."""
    safe = max(0, int(badge))
    tier, subrank = divmod(safe, 10)
    asset = next((r for r in ranks or () if r.get("tier") == tier), None)
    name = (
        str(asset.get("name"))
        if asset and asset.get("name")
        else (RANK_NAMES[tier] if tier < len(RANK_NAMES) else f"Tier {tier}")
    )
    images: Mapping[str, Any] = (asset or {}).get("images") or {}
    image = None
    if subrank:
        image = images.get(f"large_subrank{subrank}_webp") or images.get(f"large_subrank{subrank}")
    image = image or images.get("large_webp") or images.get("large")
    label = name if tier == 0 or subrank == 0 else f"{name} {subrank}"
    return Badge(safe, tier, subrank, name, label, image, (asset or {}).get("color"))


def encode_badge(tier: int, subrank: int) -> int:
    return tier * 10 + subrank


def parse_badge(value: str | int) -> int:
    """Parses what people type: ``"oracle"``, ``"Oracle 3"``, ``"eternus6"`` or ``"81"``."""
    if isinstance(value, int):
        return value
    raw = value.strip().lower()
    if raw.isdigit():
        return int(raw)
    m = re.fullmatch(r"([a-z]+)\s*([1-6])?", raw)
    names = [n.lower() for n in RANK_NAMES]
    if not m or m[1] not in names:
        raise invalid_input(f'Unknown rank {value!r}. Use a name like "oracle 3" or a badge number.')
    tier = names.index(m[1])
    return encode_badge(tier, 0 if tier == 0 else int(m[2] or 1))


# --- Modes and regions -------------------------------------------------------

GAME_MODES: dict[int, str] = {0: "Invalid", 1: "Normal", 2: "1v1 Test", 3: "Sandbox", 4: "Street Brawl"}
MATCH_MODES: dict[int, str] = {
    0: "Invalid",
    1: "Unranked",
    2: "Private Lobby",
    3: "Co-op Bot",
    4: "Ranked",
    5: "Server Test",
    6: "Tutorial",
    7: "Hero Labs",
    8: "New Player Placement",
}
LeaderboardRegion = Literal["Europe", "Asia", "NAmerica", "SAmerica", "Oceania"]
LEADERBOARD_REGIONS: tuple[LeaderboardRegion, ...] = ("Europe", "Asia", "NAmerica", "SAmerica", "Oceania")
_REGION_ALIASES: dict[str, LeaderboardRegion] = {
    "eu": "Europe",
    "europe": "Europe",
    "asia": "Asia",
    "sea": "Asia",
    "na": "NAmerica",
    "nam": "NAmerica",
    "namerica": "NAmerica",
    "north america": "NAmerica",
    "sa": "SAmerica",
    "sam": "SAmerica",
    "samerica": "SAmerica",
    "south america": "SAmerica",
    "oce": "Oceania",
    "oceania": "Oceania",
}


def game_mode_name(mode: int | None) -> str:
    return GAME_MODES.get(mode or 0, f"Mode {mode}")


def match_mode_name(mode: int | None) -> str:
    return MATCH_MODES.get(mode or 0, f"Mode {mode}")


def normalize_region(region: str) -> LeaderboardRegion:
    """Accepts ``"eu"``, ``"na"``, ``"North America"`` and returns the API's region name."""
    key = re.sub(r"[_-]+", " ", region.strip().lower())
    if key in _REGION_ALIASES:
        return _REGION_ALIASES[key]
    raise invalid_input(f"Unknown region {region!r}. Use one of: eu, na, sa, asia, oce.")


# --- Stats -------------------------------------------------------------------


def win_rate(wins: int, matches: int) -> float:
    return wins / matches if matches > 0 else 0.0


def kda(kills: int, deaths: int, assists: int) -> float:
    """(kills + assists) / deaths, with deaths floored at 1."""
    return (kills + assists) / max(1, deaths)


def wilson_lower_bound(wins: int, matches: int, z: float = 1.96) -> float:
    """Lower bound of the Wilson score interval (95% by default).

    Ranks win rates by how sure we can be about them, so 12 games at 75% do not
    beat 40,000 games at 55%.
    """
    if matches <= 0:
        return 0.0
    p = wins / matches
    z2 = z * z
    centre = p + z2 / (2 * matches)
    margin = z * math.sqrt((p * (1 - p) + z2 / (4 * matches)) / matches)
    return (centre - margin) / (1 + z2 / matches)


def chunk(items: Sequence[T], size: int) -> list[list[T]]:
    return [list(items[i : i + size]) for i in range(0, len(items), size)]


def normalize_text(text: str) -> str:
    """Lowercase, no accents, only letters and digits: ``"Lady Geist"`` matches ``"ladygeist"``."""
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", folded.lower())


def unique(items: Iterable[T]) -> list[T]:
    return list(dict.fromkeys(items))
