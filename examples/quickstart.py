"""python examples/quickstart.py [steam id or profile URL]"""

import sys
import time

from deadlock_sdk import Deadlock

with Deadlock() as dl:
    player = sys.argv[1] if len(sys.argv) > 1 else dl.leaderboard.get("eu", limit=1)[0].account_ids[0]

    me = dl.players.summary(player)
    name = me.profile["personaname"] if me.profile else me.account_id
    print(f"{name}: {me.rank.label if me.rank else 'unranked'}")
    print(
        f"last {me.recent.matches}: {me.recent.win_rate:.1%} win rate, KDA {me.recent.kda}, {me.recent.streak.count} {me.recent.streak.kind} streak"
    )
    for h in me.top_heroes:
        print(f"  {h.name:<14} {h.matches} games, {h.win_rate:.0%}")

    # The meta above Oracle over the last two weeks.
    since = int(time.time()) - 14 * 86400
    tiers = dl.heroes.tier_list(min_average_badge=81, min_unix_timestamp=since)
    print("\nS tier above Oracle:", ", ".join(t.name for t in tiers if t.tier == "S"))

    # Anything else is still one typed call away.
    mates = dl.api.get("/v1/players/{account_id}/mate-stats", path_params={"account_id": me.account_id})
    print(f"{len(mates)} different teammates on record")
