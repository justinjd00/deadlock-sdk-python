"""Turn SDK results into pandas DataFrames. Needs ``pip install "deadlock-sdk[pandas]"``.

>>> from deadlock_sdk.pandas import to_dataframe
>>> df = to_dataframe(dl.heroes.stats(min_average_badge=81))
>>> df.sort_values("win_rate", ascending=False).head()
"""

from __future__ import annotations

import dataclasses
from collections.abc import Iterable, Mapping
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import pandas as pd

#: Raw payloads are dropped by default, they are nested and rarely what you want in a table.
_SKIP = frozenset({"raw"})


def _row(item: Any, keep_raw: bool) -> dict[str, Any]:
    if dataclasses.is_dataclass(item) and not isinstance(item, type):
        out = {}
        for f in dataclasses.fields(item):
            if f.name in _SKIP and not keep_raw:
                continue
            value = getattr(item, f.name)
            # Flatten one level of nested dataclasses: rank.label -> rank_label.
            if dataclasses.is_dataclass(value) and not isinstance(value, type):
                out.update({f"{f.name}_{k}": v for k, v in _row(value, keep_raw).items()})
            else:
                out[f.name] = value
        return out
    if isinstance(item, Mapping):
        return dict(item)
    raise TypeError(f"Cannot turn {type(item).__name__} into a row")


def to_dataframe(items: Iterable[Any], *, keep_raw: bool = False) -> pd.DataFrame:
    """A DataFrame from SDK dataclasses (``HeroStat``, ``TierEntry``, ...) or raw response dicts."""
    try:
        import pandas as pd
    except ImportError as exc:  # pragma: no cover - depends on the environment
        raise ImportError('pandas is not installed. Run: pip install "deadlock-sdk[pandas]"') from exc
    frame: pd.DataFrame = pd.DataFrame([_row(i, keep_raw) for i in items])
    return frame
