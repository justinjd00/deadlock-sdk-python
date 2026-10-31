# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-10-31

First release.

### Added

- `Deadlock` (sync) and `AsyncDeadlock` (asyncio) clients. The sync client is generated from the async source, so both behave the same.
- Typed access to every GET endpoint through `dl.api.get(...)`: all 237 schemas generated as `TypedDict`, one `@overload` per endpoint, checked by mypy and pyright.
- Resources: `players` (summary, rank, batched ranks, match history with filters, hero, enemy and mate stats, search, profiles), `matches` (metadata, bulk metadata in chunks of 1000, live matches, scoreboards), `heroes` (lookup by name, stats, confidence ranked tier list, counters, synergies), `items` (shop filters, lookup, item stats), `ranks`, `leaderboard`, `builds`, `patches`, `analytics` and `sql`.
- Steam id helpers for account ids, SteamID64, SteamID3, SteamID2 and profile URLs, accepted by every method.
- Rank helpers `decode_badge`, `encode_badge` and `parse_badge` (`"oracle 3"` to `83`), stats helpers `summarize_history`, `wilson_lower_bound`, `win_rate`, `kda`.
- HTTP layer on httpx with retries, `Retry-After`, proactive throttling on `RateLimit-*` headers, no retries for 504 query timeouts, typed `DeadlockError` codes and request de-duplication in async code.
- Per resource cache lifetimes and pluggable cache stores.
- `deadlock_sdk.pandas.to_dataframe` with the optional `pandas` extra.
- `deadlock-py` CLI (also `python -m deadlock_sdk`).
- Weekly contract tests against the live API plus a schema drift check.

[1.0.0]: https://github.com/justinjd00/deadlock-sdk-python/releases/tag/v1.0.0
