"""``deadlock-py`` command line tool. Run ``deadlock-py --help``."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from collections.abc import Callable, Sequence
from dataclasses import asdict, is_dataclass
from datetime import datetime
from typing import Any

from . import _logic as logic
from ._sync_client import ATTRIBUTION, Deadlock
from ._version import __version__
from .errors import DeadlockError
from .helpers import (
    game_mode_name,
    match_mode_name,
    parse_badge,
    steam_profile_url,
    to_account_id,
    to_steam_id2,
    to_steam_id3,
    to_steam_id64,
)

TEAM_NAMES = ("Hidden King", "Archmother")
_ANSI = re.compile(r"\x1b\[[0-9;]*m")


class Style:
    def __init__(self, enabled: bool) -> None:
        self.enabled = enabled

    def _wrap(self, code: str, text: str) -> str:
        return f"\x1b[{code}m{text}\x1b[0m" if self.enabled else text

    def bold(self, t: str) -> str:
        return self._wrap("1", t)

    def dim(self, t: str) -> str:
        return self._wrap("2", t)

    def green(self, t: str) -> str:
        return self._wrap("32", t)

    def red(self, t: str) -> str:
        return self._wrap("31", t)

    def cyan(self, t: str) -> str:
        return self._wrap("36", t)


def pct(v: float) -> str:
    return f"{v * 100:.1f}%"


def num(v: int | float) -> str:
    return f"{v:,}"


def mins(s: int) -> str:
    return f"{s // 60}:{s % 60:02d}"


def ago(unix: int) -> str:
    d = max(0, time.time() - unix)
    if d < 3600:
        return f"{round(d / 60)}m ago"
    if d < 86400:
        return f"{round(d / 3600)}h ago"
    return f"{round(d / 86400)}d ago"


def table(rows: Sequence[dict[str, Any]], style: Style, limit: int | None = None) -> None:
    shown = list(rows[:limit] if limit else rows)
    if not shown:
        print(style.dim("No results."))
        return
    cols = [c for c in shown[0] if any(r.get(c) not in (None, "") for r in shown)]

    def text(v: Any) -> str:
        s = "" if v is None else str(v)
        plain = _ANSI.sub("", s)
        return s if len(plain) <= 48 or plain.startswith("http") else plain[:45] + "..."

    cells = [[text(r.get(c)) for c in cols] for r in shown]
    widths = [max(len(c), *(len(_ANSI.sub("", row[i])) for row in cells)) for i, c in enumerate(cols)]
    numeric = [
        all(re.fullmatch(r"[+-]?[\d,.:]+%?", _ANSI.sub("", row[i])) or not row[i] for row in cells)
        for i in range(len(cols))
    ]

    def line(values: Sequence[str]) -> str:
        out = []
        for i, v in enumerate(values):
            pad = " " * (widths[i] - len(_ANSI.sub("", v)))
            out.append(pad + v if numeric[i] else v + pad)
        return "  ".join(out).rstrip()

    print(style.bold(line(cols)))
    for row in cells:
        print(line(row))
    if limit and len(rows) > limit:
        print(style.dim(f"... {len(rows) - limit} more, use --limit"))


def to_json(data: Any) -> str:
    def default(o: Any) -> Any:
        if is_dataclass(o) and not isinstance(o, type):
            return asdict(o)
        if isinstance(o, datetime):
            return o.isoformat()
        raise TypeError(type(o).__name__)

    return json.dumps(data, default=default, indent=2, ensure_ascii=False)


def time_query(args: argparse.Namespace) -> dict[str, Any]:
    """Meta commands cover the last 30 days by default, all-time numbers hide the current balance."""
    q: dict[str, Any] = {"min_unix_timestamp": int(time.time() - args.days * 86400)}
    if args.min_rank:
        q["min_average_badge"] = parse_badge(args.min_rank)
    return q


def resolve(dl: Deadlock, who: str, style: Style) -> int:
    try:
        return to_account_id(who)
    except DeadlockError:
        hits = dl.players.search(who, limit=1)
        if not hits:
            raise DeadlockError(f"No player found for {who!r}", code="INVALID_INPUT") from None
        print(
            style.dim(f"Using {hits[0]['personaname']} ({hits[0]['account_id']}). Pass an id to be exact."),
            file=sys.stderr,
        )
        return hits[0]["account_id"]


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="deadlock-py",
        description="Deadlock stats from the terminal, powered by the Deadlock API.",
        epilog=f"{ATTRIBUTION['text']}: {ATTRIBUTION['url']}. Not affiliated with Valve.",
    )
    p.add_argument("-V", "--version", action="version", version=__version__)
    p.add_argument("--json", action="store_true", help="raw JSON output")
    p.add_argument("--api-key", default=os.environ.get("DEADLOCK_API_KEY"), help="or set DEADLOCK_API_KEY")
    sub = p.add_subparsers(dest="command", required=True, metavar="command")

    def cmd(name: str, help: str) -> argparse.ArgumentParser:
        c = sub.add_parser(name, help=help, description=help)
        c.add_argument("--json", action="store_true", default=argparse.SUPPRESS, help="raw JSON output")
        return c

    def meta(c: argparse.ArgumentParser) -> None:
        c.add_argument("--days", type=float, default=30, help="look back this many days (default 30)")
        c.add_argument("--min-rank", help='e.g. "oracle", "eternus 3" or a badge like 81')

    c = cmd("player", "rank, recent form, streak and top heroes")
    c.add_argument("who", help="account id, SteamID64, [U:1:x], profile URL or Steam name")
    c.add_argument("--matches", type=int, default=50)
    c = cmd("matches", "recent matches of a player")
    c.add_argument("who")
    c.add_argument("--limit", type=int, default=15)
    c.add_argument("--ranked", action="store_true")
    c.add_argument("--hero")
    c = cmd("rank", "current rank of a player")
    c.add_argument("who")
    c = cmd("search", "find players by Steam name")
    c.add_argument("name", nargs="+")
    c.add_argument("--limit", type=int, default=10)
    c = cmd("steamid", "convert between Steam id formats")
    c.add_argument("who")
    c = cmd("match", "scoreboard of a match")
    c.add_argument("match_id", type=int)
    c = cmd("live", "top matches being played right now")
    c.add_argument("--limit", type=int, default=15)
    c = cmd("tiers", "tier list ranked by confidence")
    meta(c)
    c.add_argument("--limit", type=int)
    c = cmd("hero", "hero stats, matchups and best teammates")
    c.add_argument("name", nargs="+")
    meta(c)
    c = cmd("items", "item win rates and buy timings")
    meta(c)
    c.add_argument("--slot", choices=["weapon", "vitality", "spirit"])
    c.add_argument("--hero")
    c.add_argument("--limit", type=int, default=25)
    c = cmd("leaderboard", "regional leaderboard")
    c.add_argument("region", nargs="?", default="eu")
    c.add_argument("--hero")
    c.add_argument("--limit", type=int, default=25)
    c = cmd("patches", "latest patch notes")
    c.add_argument("--limit", type=int, default=10)
    c = cmd("sql", 'SQL over the public dataset (DuckDB). "tables" lists tables')
    c.add_argument("query", nargs="+")
    c.add_argument("--limit", type=int, default=50)
    return p


def run(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    style = Style(sys.stdout.isatty() and not os.environ.get("NO_COLOR"))
    dl = Deadlock(api_key=args.api_key)
    out: Callable[[Any, Callable[[], None]], None] = lambda data, render: (  # noqa: E731
        print(to_json(data)) if args.json else render()
    )
    try:
        handler = COMMANDS[args.command]
        handler(dl, args, style, out)
        return 0
    except DeadlockError as error:
        status = f" {error.status}" if error.status else ""
        print(f"Error ({error.code}{status}): {error.message}", file=sys.stderr)
        return 2 if error.code == "INVALID_INPUT" else 1
    finally:
        dl.close()


Out = Callable[[Any, Callable[[], None]], None]


def _player(dl: Deadlock, args: argparse.Namespace, st: Style, out: Out) -> None:
    s = dl.players.summary(resolve(dl, args.who, st), matches=args.matches)

    def render() -> None:
        r = s.recent
        name = (s.profile.get("personaname") if s.profile else None) or str(s.account_id)
        print(f"{st.bold(name)}  {st.dim(f'{s.account_id} · {s.steam_id64}')}")
        print(f"Rank      {st.cyan(s.rank.label) if s.rank else st.dim('unranked or private')}")
        streak = r.streak.kind
        mark = (
            st.green(f"{r.streak.count}W")
            if streak == "win"
            else st.red(f"{r.streak.count}L")
            if streak == "loss"
            else "-"
        )
        print(
            f"Last {r.matches}   {r.wins}W {r.losses}L  {st.bold(pct(r.win_rate))}  KDA {r.kda:.2f}  streak {mark}"
        )
        if r.ranked_delta:
            delta = f"+{r.ranked_delta}" if r.ranked_delta > 0 else str(r.ranked_delta)
            print(f"Ranked    {st.green(delta) if r.ranked_delta > 0 else st.red(delta)} rank points")
        print(f"\n{st.bold('Top heroes')}")
        table(
            [
                {
                    "hero": h.name,
                    "matches": num(h.matches),
                    "winrate": pct(h.win_rate),
                    "kda": f"{h.kda:.2f}",
                    "avg souls": num(h.avg_net_worth),
                }
                for h in s.top_heroes
            ],
            st,
        )

    out(s, render)


def _matches(dl: Deadlock, args: argparse.Namespace, st: Style, out: Out) -> None:
    hero = dl.heroes.require(args.hero) if args.hero else None
    rows = dl.players.match_history(
        resolve(dl, args.who, st),
        limit=args.limit,
        match_modes=[4] if args.ranked else None,
        hero_id=hero["id"] if hero else None,
    )
    names = logic.hero_names(dl.heroes.list(only_active=False))

    def render() -> None:
        table(
            [
                {
                    "when": ago(m["start_time"]),
                    "match": m["match_id"],
                    "hero": names.get(m["hero_id"], m["hero_id"]),
                    "result": st.green("WIN") if logic.did_win(m) else st.red("LOSS"),
                    "kda": f"{m['player_kills']}/{m['player_deaths']}/{m['player_assists']}",
                    "souls": num(m["net_worth"]),
                    "length": mins(m["match_duration_s"]),
                    "mode": match_mode_name(m["match_mode"]),
                    "rank": (f"+{d}" if d > 0 else str(d)) if (d := m.get("ranked_delta") or 0) else "",
                }
                for m in rows
            ],
            st,
        )

    out(rows, render)


def _rank(dl: Deadlock, args: argparse.Namespace, st: Style, out: Out) -> None:
    r = dl.players.rank(resolve(dl, args.who, st))
    out(
        r,
        lambda: print(
            f"{st.cyan(r.label)}  {st.dim(f'badge {r.badge}')}" if r.badge else st.dim("No ranked data.")
        ),
    )


def _search(dl: Deadlock, args: argparse.Namespace, st: Style, out: Out) -> None:
    hits = dl.players.search(" ".join(args.name), limit=args.limit)
    out(hits, lambda: table([{"name": h["personaname"], "id": h["account_id"]} for h in hits], st))


def _steamid(dl: Deadlock, args: argparse.Namespace, st: Style, out: Out) -> None:
    a = to_account_id(args.who)
    ids = {
        "account_id": a,
        "steam_id64": to_steam_id64(a),
        "steam_id3": to_steam_id3(a),
        "steam_id2": to_steam_id2(a),
        "profile": steam_profile_url(a),
    }
    out(ids, lambda: table([{"format": k, "value": v} for k, v in ids.items()], st))


def _match(dl: Deadlock, args: argparse.Namespace, st: Style, out: Out) -> None:
    s = dl.matches.scoreboard(args.match_id)

    def render() -> None:
        when = s.started_at.strftime("%Y-%m-%d %H:%M")
        print(
            f"{st.bold(f'Match {s.match_id}')}  {st.dim(f'{when} UTC · {mins(s.duration_s)} · {game_mode_name(s.game_mode)} {match_mode_name(s.match_mode)}')}"
        )
        for i, team in enumerate(s.teams):
            print(f"\n{st.bold(TEAM_NAMES[i])}  {st.green('WIN') if s.winning_team == i else st.red('LOSS')}")
            table(
                [
                    {
                        "hero": p.hero_name,
                        "k": p.kills,
                        "d": p.deaths,
                        "a": p.assists,
                        "souls": num(p.net_worth),
                        "dmg": num(p.player_damage) if p.player_damage is not None else "",
                        "items": ", ".join(p.final_items[-4:]),
                        "player": p.account_id,
                    }
                    for p in team
                ],
                st,
            )

    out(s, render)


def _live(dl: Deadlock, args: argparse.Namespace, st: Style, out: Out) -> None:
    active = dl.matches.active()
    names = logic.hero_names(dl.heroes.list(only_active=False))
    rows = [
        {
            "match": m.get("match_id"),
            "mode": m.get("match_mode_parsed"),
            "region": m.get("region_mode_parsed"),
            "watching": m.get("spectators"),
            "heroes": ", ".join(names.get(p.get("hero_id") or -1, "?") for p in m["players"]),
        }
        for m in active
    ]
    out(active, lambda: table(rows, st, args.limit))


def _tiers(dl: Deadlock, args: argparse.Namespace, st: Style, out: Out) -> None:
    tiers = dl.heroes.tier_list(min_matches=200, **time_query(args))
    out(
        tiers,
        lambda: table(
            [
                {
                    "tier": st.bold(t.tier),
                    "hero": t.name,
                    "winrate": pct(t.win_rate),
                    "pick rate": pct(t.pick_rate),
                    "matches": num(t.matches),
                    "kda": f"{t.kda:.2f}",
                }
                for t in tiers
            ],
            st,
            args.limit,
        ),
    )


def _hero(dl: Deadlock, args: argparse.Namespace, st: Style, out: Out) -> None:
    hero = dl.heroes.require(" ".join(args.name))
    q = time_query(args)
    stats = next((s for s in dl.heroes.stats(**q) if s.hero_id == hero["id"]), None)
    counters = dl.heroes.counters(hero["id"], **q)
    mates = dl.heroes.synergies(hero["id"], **q)

    def render() -> None:
        print(f"{st.bold(hero['name'])}  {st.dim(str(hero.get('hero_type') or ''))}")
        if stats:
            print(
                f"Win rate {st.bold(pct(stats.win_rate))}  pick rate {pct(stats.pick_rate)}  KDA {stats.kda:.2f}  {st.dim(num(stats.matches) + ' matches')}"
            )
        for title, rows, color in (
            ("Strong against", counters[:5], st.green),
            ("Weak against", logic.worst_matchups(counters)[:5], st.red),
            ("Best teammates", mates[:5], str),
        ):
            print(f"\n{st.bold(title)}")
            table(
                [
                    {"hero": m.name, "winrate": color(pct(m.win_rate)), "matches": num(m.matches)}
                    for m in rows
                ],
                st,
            )

    out(
        {
            "hero": {"id": hero["id"], "name": hero["name"]},
            "stats": stats,
            "counters": counters,
            "synergies": mates,
        },
        render,
    )


def _items(dl: Deadlock, args: argparse.Namespace, st: Style, out: Out) -> None:
    q = time_query(args)
    if args.hero:
        q["hero_id"] = dl.heroes.require(args.hero)["id"]
    rows = [s for s in dl.items.stats(min_matches=500, **q) if not args.slot or s.slot == args.slot]
    out(
        rows,
        lambda: table(
            [
                {
                    "item": s.name,
                    "slot": s.slot,
                    "tier": s.tier,
                    "winrate": pct(s.win_rate),
                    "matches": num(s.matches),
                    "avg buy": mins(s.avg_buy_time_s),
                }
                for s in rows
            ],
            st,
            args.limit,
        ),
    )


def _leaderboard(dl: Deadlock, args: argparse.Namespace, st: Style, out: Out) -> None:
    rows = dl.leaderboard.get(args.region, hero=args.hero, limit=args.limit)
    out(
        rows,
        lambda: table([{"#": r.rank, "name": r.name, "heroes": ", ".join(r.top_heroes)} for r in rows], st),
    )


def _patches(dl: Deadlock, args: argparse.Namespace, st: Style, out: Out) -> None:
    notes = dl.patches.list()
    out(
        notes,
        lambda: table(
            [{"date": n.published_at.date().isoformat(), "title": n.title, "url": n.url} for n in notes],
            st,
            args.limit,
        ),
    )


def _sql(dl: Deadlock, args: argparse.Namespace, st: Style, out: Out) -> None:
    text = " ".join(args.query)
    if text.strip() == "tables":
        tables = dl.sql.tables()
        out(tables, lambda: print("\n".join(tables)))
        return
    rows = dl.sql.query(text)
    out(rows, lambda: table(rows, st, args.limit))


COMMANDS: dict[str, Callable[[Deadlock, argparse.Namespace, Style, Out], None]] = {
    "player": _player,
    "matches": _matches,
    "rank": _rank,
    "search": _search,
    "steamid": _steamid,
    "match": _match,
    "live": _live,
    "tiers": _tiers,
    "hero": _hero,
    "items": _items,
    "leaderboard": _leaderboard,
    "patches": _patches,
    "sql": _sql,
}


def main() -> None:
    try:
        code = run()
        sys.stdout.flush()
    except BrokenPipeError:
        # Output piped into `head` and friends, which closed early. Not an error.
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        code = 0
    except KeyboardInterrupt:
        code = 130
    sys.exit(code)


if __name__ == "__main__":
    main()
