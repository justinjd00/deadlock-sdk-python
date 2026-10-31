"""Pure transformations from raw responses to SDK results.

Kept free of I/O so the sync and async clients share every line of logic.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any, cast

from ._generated.schemas import (
    AnalyticsHeroStats,
    Hero,
    HeroCounterStats,
    HeroSynergyStats,
    Item,
    ItemStats,
    LeaderboardEntry,
    Patch,
    PlayerMatchHistoryEntry,
    RankResponse,
    SteamProfile,
)
from .errors import DeadlockError
from .helpers import decode_badge, kda, normalize_text, to_steam_id64, wilson_lower_bound, win_rate
from .models import (
    HeroStat,
    HeroSummary,
    HistorySummary,
    ItemStat,
    LeaderboardRow,
    MatchMetadata,
    MatchPlayer,
    Matchup,
    PatchNote,
    PlayerRank,
    PlayerSummary,
    Scoreboard,
    ScoreboardPlayer,
    Streak,
    Tier,
    TierEntry,
)


def _utc(ts: int | float) -> datetime:
    return datetime.fromtimestamp(ts, tz=timezone.utc)


def did_win(entry: Mapping[str, Any]) -> bool:
    """``True`` when the player's team won the match."""
    return bool(entry.get("match_result") == entry.get("player_team"))


def summarize_history(entries: Sequence[PlayerMatchHistoryEntry]) -> HistorySummary:
    """Win rate, KDA, streak, ranked progress and per hero numbers for a match history."""
    rows = sorted(entries, key=lambda e: e["start_time"], reverse=True)
    n = len(rows)
    wins = sum(1 for e in rows if did_win(e))
    kills = sum(e["player_kills"] for e in rows)
    deaths = sum(e["player_deaths"] for e in rows)
    assists = sum(e["player_assists"] for e in rows)

    per_hero: dict[int, list[PlayerMatchHistoryEntry]] = {}
    for e in rows:
        per_hero.setdefault(e["hero_id"], []).append(e)
    heroes = [
        HeroSummary(
            hero_id=hero_id,
            matches=len(games),
            wins=(w := sum(1 for g in games if did_win(g))),
            win_rate=round(win_rate(w, len(games)), 4),
            kda=round(
                kda(
                    sum(g["player_kills"] for g in games),
                    sum(g["player_deaths"] for g in games),
                    sum(g["player_assists"] for g in games),
                ),
                2,
            ),
            avg_net_worth=round(sum(g["net_worth"] for g in games) / len(games)),
        )
        for hero_id, games in per_hero.items()
    ]
    heroes.sort(key=lambda h: (-h.matches, -h.win_rate))

    streak = Streak("none", 0)
    if rows:
        first = did_win(rows[0])
        count = 0
        for e in rows:
            if did_win(e) != first:
                break
            count += 1
        streak = Streak("win" if first else "loss", count)

    return HistorySummary(
        matches=n,
        wins=wins,
        losses=n - wins,
        win_rate=round(win_rate(wins, n), 4),
        kills=kills,
        deaths=deaths,
        assists=assists,
        kda=round(kda(kills, deaths, assists), 2),
        avg_net_worth=round(sum(e["net_worth"] for e in rows) / n) if n else 0,
        avg_last_hits=round(sum(e["last_hits"] for e in rows) / n, 1) if n else 0.0,
        avg_duration_s=round(sum(e["match_duration_s"] for e in rows) / n) if n else 0,
        streak=streak,
        ranked_delta=sum(e.get("ranked_delta") or 0 for e in rows),
        heroes=heroes,
        first_match_at=_utc(rows[-1]["start_time"]) if rows else None,
        last_match_at=_utc(rows[0]["start_time"]) if rows else None,
    )


def filter_history(
    rows: Sequence[PlayerMatchHistoryEntry],
    *,
    limit: int | None = None,
    since: int | None = None,
    match_modes: Sequence[int] | None = None,
    hero_id: int | None = None,
) -> list[PlayerMatchHistoryEntry]:
    out = [
        r
        for r in rows
        if (since is None or r["start_time"] >= since)
        and (match_modes is None or r["match_mode"] in match_modes)
        and (hero_id is None or r["hero_id"] == hero_id)
    ]
    out.sort(key=lambda r: r["start_time"], reverse=True)
    return out[:limit] if limit is not None else out


def player_rank(account_id: int, raw: RankResponse, ranks: Sequence[Mapping[str, Any]] | None) -> PlayerRank:
    b = decode_badge(raw.get("badge") or 0, ranks)
    return PlayerRank(
        badge=b.badge,
        tier=b.tier,
        subrank=b.subrank,
        name=b.name,
        label=b.label,
        image=b.image,
        color=b.color,
        account_id=account_id,
        raw=raw,
    )


def player_summary(
    account_id: int,
    history: Sequence[PlayerMatchHistoryEntry],
    rank: PlayerRank | None,
    profile: SteamProfile | None,
    heroes: Sequence[Hero],
) -> PlayerSummary:
    recent = summarize_history(history)
    names = hero_names(heroes)
    top = [
        HeroSummary(**{**h.to_dict(), "name": names.get(h.hero_id, f"Hero {h.hero_id}")})
        for h in recent.heroes[:5]
    ]
    return PlayerSummary(
        account_id=account_id,
        steam_id64=to_steam_id64(account_id),
        profile=profile,
        rank=rank if rank and rank.badge > 0 else None,
        recent=recent,
        top_heroes=top,
    )


def hero_names(heroes: Sequence[Hero]) -> dict[int, str]:
    return {h["id"]: h["name"] for h in heroes}


def find_hero(heroes: Sequence[Hero], hero: int | str) -> Hero | None:
    if isinstance(hero, int) or str(hero).isdigit():
        return next((h for h in heroes if h["id"] == int(hero)), None)
    want = normalize_text(str(hero))
    return next(
        (
            h
            for h in heroes
            if normalize_text(h["name"]) == want
            or h["class_name"] == hero
            or normalize_text(h["class_name"].removeprefix("hero_")) == want
        ),
        None,
    )


def require_hero(heroes: Sequence[Hero], hero: int | str) -> Hero:
    found = find_hero(heroes, hero)
    if found is None:
        raise DeadlockError(f"No hero {hero!r}", code="NOT_FOUND")
    return found


def hero_stats(rows: Sequence[AnalyticsHeroStats], heroes: Sequence[Hero]) -> list[HeroStat]:
    names = hero_names(heroes)
    # Every match has 12 heroes, so total matches = sum of hero matches / 12.
    total = sum(r["matches"] for r in rows) / 12
    out = [
        HeroStat(
            hero_id=r["hero_id"],
            name=names.get(r["hero_id"], f"Hero {r['hero_id']}"),
            matches=r["matches"],
            wins=r["wins"],
            win_rate=round(win_rate(r["wins"], r["matches"]), 4),
            pick_rate=round(r["matches"] / total, 4) if total else 0.0,
            kda=round(kda(r["total_kills"], r["total_deaths"], r["total_assists"]), 2),
            avg_net_worth=round(r["total_net_worth"] / r["matches"]) if r["matches"] else 0,
            avg_player_damage=round(r["total_player_damage"] / r["matches"]) if r["matches"] else 0,
            confidence=round(wilson_lower_bound(r["wins"], r["matches"]), 4),
            raw=r,
        )
        for r in rows
    ]
    return sorted(out, key=lambda s: -s.matches)


def tier_list(stats: Sequence[HeroStat], min_matches: int = 100) -> list[TierEntry]:
    """S top 10%, A next 20%, B 40%, C 20%, D bottom 10%, ranked by confidence."""
    ranked = sorted(
        (s for s in stats if s.matches >= min_matches), key=lambda s: (-s.confidence, -s.win_rate)
    )
    n = len(ranked)

    def cut(i: int) -> Tier:
        p = (i + 0.5) / n
        return "S" if p <= 0.1 else "A" if p <= 0.3 else "B" if p <= 0.7 else "C" if p <= 0.9 else "D"

    return [
        TierEntry(**{**{k: getattr(s, k) for k in s.__dataclass_fields__}, "tier": cut(i), "position": i + 1})
        for i, s in enumerate(ranked)
    ]


def counters(
    rows: Sequence[HeroCounterStats], target: Hero, heroes: Sequence[Hero], min_matches: int = 50
) -> list[Matchup]:
    names = hero_names(heroes)
    out = [
        Matchup(
            hero_id=r["enemy_hero_id"],
            name=names.get(r["enemy_hero_id"], f"Hero {r['enemy_hero_id']}"),
            matches=r["matches_played"],
            wins=r["wins"],
            win_rate=round(win_rate(r["wins"], r["matches_played"]), 4),
            confidence=round(wilson_lower_bound(r["wins"], r["matches_played"]), 4),
        )
        for r in rows
        if r["hero_id"] == target["id"] and r["matches_played"] >= min_matches
    ]
    return sorted(out, key=lambda m: -m.confidence)


def worst_matchups(matchups: Sequence[Matchup]) -> list[Matchup]:
    """Matchups the hero loses most, also confidence ranked so tiny samples do not top the list."""
    return sorted(matchups, key=lambda m: -wilson_lower_bound(m.matches - m.wins, m.matches))


def synergies(
    rows: Sequence[HeroSynergyStats], target: Hero, heroes: Sequence[Hero], min_matches: int = 50
) -> list[Matchup]:
    names = hero_names(heroes)
    out = []
    for r in rows:
        if target["id"] not in (r["hero_id1"], r["hero_id2"]) or r["matches_played"] < min_matches:
            continue
        mate = r["hero_id2"] if r["hero_id1"] == target["id"] else r["hero_id1"]
        out.append(
            Matchup(
                hero_id=mate,
                name=names.get(mate, f"Hero {mate}"),
                matches=r["matches_played"],
                wins=r["wins"],
                win_rate=round(win_rate(r["wins"], r["matches_played"]), 4),
                confidence=round(wilson_lower_bound(r["wins"], r["matches_played"]), 4),
            )
        )
    return sorted(out, key=lambda m: -m.confidence)


def filter_items(
    items: Sequence[Item],
    *,
    type: str | None = None,
    slot: str | None = None,
    tier: int | None = None,
    shopable: bool | None = None,
) -> list[Item]:
    out = []
    for item in items:
        i = cast(Mapping[str, Any], item)
        if type is not None and i.get("type") != type:
            continue
        if i.get("type") != "upgrade":
            if slot is None and tier is None and not shopable:
                out.append(item)
            continue
        if slot is not None and i.get("item_slot_type") != slot:
            continue
        if tier is not None and i.get("item_tier") != tier:
            continue
        if shopable is not None and bool(i.get("shopable")) != shopable:
            continue
        out.append(item)
    return out


def item_stats(rows: Sequence[ItemStats], items: Sequence[Item], min_matches: int = 100) -> list[ItemStat]:
    by_id = {cast(Mapping[str, Any], i)["id"]: cast(Mapping[str, Any], i) for i in items}
    out = []
    for r in rows:
        if r["matches"] < min_matches:
            continue
        item = by_id.get(r["item_id"], {})
        out.append(
            ItemStat(
                item_id=r["item_id"],
                name=str(item.get("name") or r["item_id"]),
                slot=item.get("item_slot_type"),
                tier=item.get("item_tier"),
                matches=r["matches"],
                wins=r["wins"],
                win_rate=round(win_rate(r["wins"], r["matches"]), 4),
                confidence=round(wilson_lower_bound(r["wins"], r["matches"]), 4),
                avg_buy_time_s=round(r["avg_buy_time_s"]),
                raw=r,
            )
        )
    return sorted(out, key=lambda s: -s.confidence)


def scoreboard(meta: MatchMetadata, heroes: Sequence[Hero], items: Sequence[Item]) -> Scoreboard:
    info = meta["match_info"]
    names = hero_names(heroes)
    raw_items = [cast(Mapping[str, Any], i) for i in items]
    item_names = {i["id"]: str(i.get("name") or i.get("class_name")) for i in raw_items}
    upgrades = {i["id"] for i in raw_items if i.get("type") == "upgrade"}

    def row(p: MatchPlayer) -> ScoreboardPlayer:
        stats = p.get("stats") or []
        damage = stats[-1].get("player_damage") if stats else None
        return ScoreboardPlayer(
            account_id=p["account_id"],
            hero_id=p["hero_id"],
            hero_name=names.get(p["hero_id"], f"Hero {p['hero_id']}"),
            team=p["team"],
            won=p["team"] == info["winning_team"],
            kills=p["kills"],
            deaths=p["deaths"],
            assists=p["assists"],
            kda=round(kda(p["kills"], p["deaths"], p["assists"]), 2),
            net_worth=p["net_worth"],
            last_hits=p["last_hits"],
            denies=p["denies"],
            level=p["level"],
            player_damage=damage if isinstance(damage, int) else None,
            final_items=[
                item_names.get(it["item_id"], str(it["item_id"]))
                for it in p.get("items") or []
                if it["item_id"] in upgrades and not it.get("sold_time_s")
            ],
            abandoned=(p.get("abandon_match_time_s") or 0) > 0,
        )

    rows = sorted((row(p) for p in info["players"]), key=lambda r: -r.net_worth)
    return Scoreboard(
        match_id=info["match_id"],
        started_at=_utc(info["start_time"]),
        duration_s=info["duration_s"],
        winning_team=info["winning_team"],
        game_mode=info["game_mode"],
        match_mode=info["match_mode"],
        teams=([r for r in rows if r.team == 0], [r for r in rows if r.team == 1]),
    )


def leaderboard(entries: Sequence[LeaderboardEntry], heroes: Sequence[Hero]) -> list[LeaderboardRow]:
    names = hero_names(heroes)
    return [
        LeaderboardRow(
            rank=e.get("rank") or 0,
            name=e.get("account_name") or "",
            account_ids=list(e.get("possible_account_ids") or []),
            top_hero_ids=list(e.get("top_hero_ids") or []),
            top_heroes=[names.get(h, f"Hero {h}") for h in e.get("top_hero_ids") or []],
            raw=e,
        )
        for e in entries
    ]


def patch_notes(patches: Sequence[Patch]) -> list[PatchNote]:
    def when(raw: str) -> datetime:
        try:
            return parsedate_to_datetime(raw)
        except (TypeError, ValueError):
            return datetime.fromisoformat(raw.replace("Z", "+00:00"))

    notes = [
        PatchNote(
            title=p["title"],
            url=p["link"],
            published_at=when(p["pub_date"]),
            html=p.get("content_encoded") or "",
            raw=p,
        )
        for p in patches
    ]
    return sorted(notes, key=lambda n: n.published_at, reverse=True)
