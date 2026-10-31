"""Small shared types: per call options, languages and path filling."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Literal
from urllib.parse import quote

from .errors import invalid_input

#: Asset languages the API supports.
Language = Literal[
    "brazilian", "bulgarian", "czech", "danish", "dutch", "english", "finnish", "french", "german",
    "greek", "hungarian", "indonesian", "italian", "japanese", "koreana", "latam", "norwegian", "polish",
    "portuguese", "romanian", "russian", "schinese", "spanish", "swedish", "tchinese", "thai", "turkish",
    "ukrainian", "vietnamese",
]  # fmt: skip


@dataclass(frozen=True)
class CallOptions:
    """Per call settings, the last argument of every method.

    ``fresh`` skips the cache (the result is still stored), ``timeout`` in seconds
    overrides the client default.
    """

    fresh: bool = False
    timeout: float | None = None


DEFAULT_OPTIONS = CallOptions()


def fill_path(template: str, params: Mapping[str, Any] | None) -> str:
    out = template
    while "{" in out:
        start = out.index("{")
        end = out.index("}", start)
        name = out[start + 1 : end]
        value = (params or {}).get(name)
        if value is None:
            raise invalid_input(f"Missing path parameter {name!r} for {template}")
        out = out[:start] + quote(str(value), safe="") + out[end + 1 :]
    return out
