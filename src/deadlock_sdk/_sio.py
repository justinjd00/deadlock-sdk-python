"""Sync twins of ``_aio.py``, used by the generated sync client."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any


def gather(*values: Any) -> list[Any]:
    """In sync code every call already ran when it was passed in, so this just collects them."""
    return list(values)


def optional(call: Callable[[], Any], *codes: str) -> Any:
    from .errors import DeadlockError

    try:
        return call()
    except DeadlockError as error:
        if error.code in codes:
            return None
        raise
