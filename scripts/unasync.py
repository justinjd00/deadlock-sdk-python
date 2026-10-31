#!/usr/bin/env python3
"""Generates the sync client from the async one, so both always behave the same.

python scripts/unasync.py          # write src/deadlock_sdk/_sync_client.py
python scripts/unasync.py --check  # fail if it is out of date (CI)
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src" / "deadlock_sdk"
ASYNC, SYNC = SRC / "_async_client.py", SRC / "_sync_client.py"

HEADER = '"""The sync client. Generated from _async_client.py by scripts/unasync.py, do not edit."""\n'

REPLACEMENTS = [
    (r"from \._aio import", "from ._sio import"),
    (r"\bhttpx\.AsyncClient\b", "httpx.Client"),
    (r"\bAsyncTransport\b", "SyncTransport"),
    (r"\bAsyncTypedGetMixin\b", "TypedGetMixin"),
    (r"\bAsync([A-Z]\w*)", r"\1"),
    (r"\basync def ", "def "),
    (r"\basync with ", "with "),
    (r"\bawait ", ""),
    (r"__aenter__", "__enter__"),
    (r"__aexit__", "__exit__"),
    (r"Async client for", "Client for"),
    (r"\basync ", ""),
]


def render() -> str:
    text = ASYNC.read_text()
    # Drop the module docstring, the sync file gets its own.
    text = re.sub(r'\A""".*?"""\n', "", text, count=1, flags=re.DOTALL)
    for pattern, repl in REPLACEMENTS:
        text = re.sub(pattern, repl, text)
    return format_code(HEADER + text)


def format_code(text: str) -> str:
    """Runs ruff's fixes and formatter, since the rewrite changes imports and line lengths."""
    ruff = shutil.which("ruff")
    cmd = [ruff] if ruff else [sys.executable, "-m", "ruff"]
    for step in (["check", "--fix", "--quiet", "--exit-zero"], ["format"]):
        done = subprocess.run(
            [*cmd, *step, "--stdin-filename", str(SYNC), "-"],
            input=text,
            capture_output=True,
            text=True,
            check=True,
        )
        text = done.stdout
    return text


def main() -> int:
    out = render()
    if "--check" in sys.argv:
        if not SYNC.exists() or SYNC.read_text() != out:
            print("_sync_client.py is out of date. Run `python scripts/unasync.py`.")
            return 1
        print("Sync client is up to date.")
        return 0
    SYNC.write_text(out)
    print(f"Wrote {SYNC.relative_to(SRC.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
