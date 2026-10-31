#!/usr/bin/env python3
"""Captures small, anonymized samples of real API responses into tests/fixtures.

Account ids and Steam names are replaced, so no real player data lands in the
repository. Run: python scripts/capture_fixtures.py <match_id>
"""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path
from typing import Any

BASE = "https://api.deadlock-api.com"
OUT = Path(__file__).resolve().parent.parent / "tests" / "fixtures"
DROP = {"death_details", "book_rewards", "pings", "ability_stats", "hero_data", "power_up_buffs",
        "player_tracked_stats", "hero_xp_rewards"}  # fmt: skip
INFO_KEYS = ["match_id", "start_time", "duration_s", "match_outcome", "winning_team", "game_mode",
             "match_mode", "average_badge_team0", "average_badge_team1"]  # fmt: skip


def get(path: str) -> Any:
    req = urllib.request.Request(BASE + path, headers={"User-Agent": "deadlock-sdk-python fixture capture"})
    with urllib.request.urlopen(req, timeout=120) as res:
        return json.loads(res.read())


ids: dict[int, int] = {}


def fake(account_id: int) -> int:
    """Stable fake ids: the first account seen becomes 1001, the next 1002, ..."""
    return ids.setdefault(account_id, 1001 + len(ids))


def pick(obj: dict[str, Any], keys: list[str]) -> dict[str, Any]:
    return {k: obj[k] for k in keys if k in obj}


def main(match_id: int) -> None:
    info = get(f"/v1/matches/{match_id}/metadata")["match_info"]
    players = [
        {
            **{k: v for k, v in p.items() if k not in DROP},
            "account_id": fake(p["account_id"]),
            "stats": p.get("stats", [])[-1:],
        }
        for p in info["players"]
    ]
    subject = info["players"][0]["account_id"]
    history = [
        {**m, "account_id": fake(m["account_id"])} for m in get(f"/v1/players/{subject}/match-history")[:30]
    ]
    hero_id = info["players"][0]["hero_id"]
    used_items = {i["item_id"] for p in info["players"] for i in p.get("items", [])}
    all_items = get("/v1/assets/items")
    items = [
        pick(i, ["id", "class_name", "name", "type", "item_slot_type", "item_tier", "shopable", "cost", "hero"])
        for i in [*(i for i in all_items if i["type"] == "upgrade" and (i["id"] in used_items or i.get("item_tier") == 1)),
                  *[i for i in all_items if i["type"] == "ability"][:3]]
    ]  # fmt: skip
    board = get("/v1/leaderboard/Europe")["entries"][:10]
    files: dict[str, Any] = {
        "match-metadata": {"match_info": {**pick(info, INFO_KEYS), "players": players}},
        "match-history": history,
        "rank": {**get(f"/v1/players/{subject}/rank"), "account_id": fake(subject)},
        "heroes": [
            {
                **pick(
                    h,
                    [
                        "id",
                        "class_name",
                        "name",
                        "hero_type",
                        "player_selectable",
                        "disabled",
                        "in_development",
                    ],
                ),
                "images": pick(h.get("images") or {}, ["icon_hero_card"]),
            }
            for h in get("/v1/assets/heroes?only_active=false")
        ],
        "items": items,
        "ranks": [
            {
                **pick(r, ["tier", "name", "color"]),
                "images": pick(
                    r.get("images") or {}, ["large", "large_webp", "large_subrank1", "large_subrank5"]
                ),
            }
            for r in get("/v1/assets/ranks")
        ],
        "hero-stats": get("/v1/analytics/hero-stats"),
        "hero-counter-stats": [r for r in get("/v1/analytics/hero-counter-stats") if r["hero_id"] == hero_id],
        "hero-synergy-stats": [
            r for r in get("/v1/analytics/hero-synergy-stats") if hero_id in (r["hero_id1"], r["hero_id2"])
        ],
        "item-stats": [
            r for r in get("/v1/analytics/item-stats") if any(i["id"] == r["item_id"] for i in items)
        ],
        "leaderboard": {
            "entries": [
                {
                    **e,
                    "account_name": f"Player {n + 1}",
                    "possible_account_ids": [fake(a) for a in e.get("possible_account_ids") or []],
                }
                for n, e in enumerate(board)
            ]
        },
        "patches": get("/v1/patches")[:3],
        "active": [
            {
                **m,
                "players": [
                    {**p, "account_id": fake(p["account_id"]) if p.get("account_id") else None}
                    for p in m["players"]
                ],
            }
            for m in get("/v1/matches/active")[:3]
        ],
        "steam": [
            {
                "account_id": fake(subject),
                "personaname": "Test Player",
                "profileurl": "https://steamcommunity.com/profiles/76561197960266729/",
                "avatar": "",
                "avatarmedium": "",
                "avatarfull": "",
                "countrycode": None,
                "last_updated": history[0]["start_time"] if history else 0,
            }
        ],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    for name, data in files.items():
        (OUT / f"{name}.json").write_text(json.dumps(data, indent=1) + "\n")
    print(f"Wrote {len(files)} fixtures, {len(ids)} accounts anonymized, subject is 1001.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python scripts/capture_fixtures.py <match_id>")
    main(int(sys.argv[1]))
