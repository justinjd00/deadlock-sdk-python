# Contributing

Thanks for helping out. Bug reports, API drift reports and pull requests are all welcome.

## Setup

Development uses [uv](https://docs.astral.sh/uv/). The package supports Python 3.10 and newer.

```bash
git clone https://github.com/justinjd00/deadlock-sdk-python.git
cd deadlock-sdk-python
uv sync
```

## Commands

| Command                                     | What it does                                                    |
| ------------------------------------------- | --------------------------------------------------------------- |
| `uv run pytest`                             | Offline tests against anonymized fixtures                       |
| `uv run pytest -m contract -o addopts=""`   | Runs the SDK against the live Deadlock API                      |
| `uv run mypy`                               | Strict type check, includes the typing contract in the tests    |
| `uv run ruff check . && uv run ruff format .` | Lint and format                                               |
| `uv run python scripts/generate.py`         | Rebuilds `src/deadlock_sdk/_generated` from the live spec       |
| `uv run python scripts/unasync.py`          | Rebuilds the sync client from `_async_client.py`                |
| `uv build`                                  | Builds the wheel and sdist                                      |

Before opening a PR, run `uv run ruff check . && uv run mypy && uv run pytest`.

## Guidelines

- The only runtime dependencies are httpx and typing-extensions. Keep it that way, pandas stays an extra.
- Edit `_async_client.py`, never `_sync_client.py`. Run `scripts/unasync.py` afterwards, CI fails when they drift.
- Logic that turns responses into results goes into `_logic.py` as pure functions, so sync and async share it.
- Never edit `src/deadlock_sdk/_generated` by hand. Run `scripts/generate.py` and commit the diff.
- The match metadata response is untyped in the spec, its types live in `models.py`. Keep new fields optional.
- Every bug fix gets a test. Fixtures in `tests/fixtures` are trimmed, anonymized real responses. Regenerate them with `uv run python scripts/capture_fixtures.py <match_id>`. Never commit real account ids or Steam names.
- Be gentle with the API: it is free and community run. Only the contract tests may hit it.

## When the API changes

The weekly `API contract` workflow opens an issue labeled `api-drift` when the live API or its spec no longer matches:

```bash
uv run python scripts/generate.py --check   # do the generated types still match the spec?
uv run python scripts/generate.py           # if not, regenerate and review the diff
uv run pytest -m contract -o addopts=""     # does the SDK still behave against the live API?
```

## Releasing

1. Bump `__version__` in `src/deadlock_sdk/_version.py`.
2. Add a `## [x.y.z] - YYYY-MM-DD` section to `CHANGELOG.md`.
3. Merge to `main`, then tag: `git tag -a vX.Y.Z -m vX.Y.Z && git push origin vX.Y.Z`.

The `Release` workflow checks the tag against the version, runs the tests, builds, publishes to PyPI with trusted publishing (no token) and creates the GitHub release from the changelog.

## Reporting issues

Include the package version, Python version, a minimal code sample and the `code` of the `DeadlockError` if one was thrown.
