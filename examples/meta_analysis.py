"""How the meta changes with rank, as a pandas table. Needs: pip install "deadlock-sdk[pandas]"

python examples/meta_analysis.py
"""

import time

import pandas as pd

from deadlock_sdk import Deadlock, parse_badge
from deadlock_sdk.pandas import to_dataframe

BANDS = {"Initiate+": "initiate", "Ritualist+": "ritualist", "Oracle+": "oracle", "Ascendant+": "ascendant"}
since = int(time.time()) - 30 * 86400

with Deadlock() as dl:
    frames = []
    for band, rank in BANDS.items():
        df = to_dataframe(dl.heroes.stats(min_average_badge=parse_badge(rank), min_unix_timestamp=since))
        frames.append(df.assign(band=band)[["name", "band", "win_rate", "matches"]])

table = pd.concat(frames).pivot_table(index="name", columns="band", values="win_rate")[list(BANDS)]
table["climb"] = table["Ascendant+"] - table["Initiate+"]
print("Heroes that get better the higher you go:\n")
print((table.sort_values("climb", ascending=False).head(8) * 100).round(1).to_string())
