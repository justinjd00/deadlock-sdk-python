"""HTTP layer: retries, Retry-After, rate limit throttling, error mapping.

The policy lives in ``_Policy`` and is shared by the sync and async transports,
so both behave exactly the same.
"""

from __future__ import annotations

import asyncio
import email.utils
import json
import random
import threading
import time
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any, Literal
from urllib.parse import urlsplit

import httpx

from ._version import __version__
from .errors import DeadlockError, ErrorCode

DEFAULT_BASE_URL = "https://api.deadlock-api.com"
DEFAULT_USER_AGENT = f"deadlock-sdk-python/{__version__} (+https://github.com/justinjd00/deadlock-sdk-python)"

ResponseKind = Literal["json", "text", "bytes"]
QueryValue = str | int | float | bool | None | list[Any] | tuple[Any, ...]
Query = Mapping[str, QueryValue]

# 504 is missing on purpose: the API answers 504 when a query is too heavy, and
# the same query would time out again.
RETRYABLE_STATUS = frozenset({408, 425, 429, 500, 502, 503})


@dataclass(frozen=True)
class RetryPolicy:
    """Retries for GET requests. Delays are in seconds."""

    retries: int = 2
    min_delay: float = 0.4
    max_delay: float = 15.0


@dataclass(frozen=True)
class RateLimit:
    limit: int | None
    remaining: int | None
    #: ``time.monotonic()`` value when the window resets.
    reset_at: float | None


@dataclass(frozen=True)
class RetryEvent:
    url: str
    attempt: int
    delay: float
    error: DeadlockError


def encode_query(query: Query | None) -> dict[str, str]:
    """Lists become comma separated, booleans lowercase, empty values are dropped."""
    out: dict[str, str] = {}
    for key, value in (query or {}).items():
        if value is None or value == "":
            continue
        if isinstance(value, (list, tuple)):
            if value:
                out[key] = ",".join(str(v).lower() if isinstance(v, bool) else str(v) for v in value)
        elif isinstance(value, bool):
            out[key] = "true" if value else "false"
        else:
            out[key] = str(value)
    return out


def parse_retry_after(value: str | None) -> float | None:
    """Seconds to wait from a ``Retry-After`` header (delta seconds or HTTP date)."""
    if not value:
        return None
    value = value.strip()
    try:
        return max(0.0, float(value))
    except ValueError:
        pass
    try:
        when = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    return max(0.0, when.timestamp() - time.time())


def _int(value: str | None) -> int | None:
    try:
        return int(float(value)) if value is not None else None
    except ValueError:
        return None


def _message(body: Any, text: str) -> str | None:
    if isinstance(body, dict):
        for key in ("error", "message", "detail"):
            if isinstance(body.get(key), str):
                return str(body[key])
    if text and len(text) < 300 and "<html" not in text.lower():
        return text.strip()
    return None


class _Policy:
    def __init__(
        self,
        *,
        base_url: str,
        api_key: str | None,
        timeout: float,
        retry: RetryPolicy | None,
        throttle: bool,
        headers: Mapping[str, str] | None,
        user_agent: str | None,
        on_retry: Callable[[RetryEvent], None] | None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.retry = retry
        self.throttle = throttle
        self.on_retry = on_retry
        self.headers: dict[str, str] = {"Accept": "application/json"}
        if user_agent:
            self.headers["User-Agent"] = user_agent
        if api_key:
            self.headers["X-API-KEY"] = api_key
        self.headers.update(headers or {})
        self._limits: dict[str, RateLimit] = {}
        self._lock = threading.Lock()

    def url(self, path: str) -> str:
        return path if path.startswith(("http://", "https://")) else f"{self.base_url}/{path.lstrip('/')}"

    @staticmethod
    def _limit_key(url: str) -> str:
        parts = urlsplit(url)
        return f"{parts.netloc}{parts.path}"

    def rate_limit(self, path: str) -> RateLimit | None:
        return self._limits.get(self._limit_key(self.url(path)))

    def record(self, url: str, headers: httpx.Headers) -> None:
        limit = _int(headers.get("ratelimit-limit") or headers.get("x-ratelimit-limit"))
        remaining = _int(headers.get("ratelimit-remaining") or headers.get("x-ratelimit-remaining"))
        reset = _int(headers.get("ratelimit-reset") or headers.get("x-ratelimit-reset"))
        if limit is None and remaining is None:
            return
        reset_at = time.monotonic() + reset if reset is not None else None
        with self._lock:
            self._limits[self._limit_key(url)] = RateLimit(limit, remaining, reset_at)

    def throttle_delay(self, url: str) -> float:
        """How long to wait before sending, so we do not run into a 429."""
        if not self.throttle:
            return 0.0
        state = self._limits.get(self._limit_key(url))
        if not state or state.remaining is None or state.remaining > 0 or state.reset_at is None:
            return 0.0
        delay = state.reset_at - time.monotonic()
        max_delay = self.retry.max_delay if self.retry else 15.0
        # Waiting longer than a retry would makes no sense, fail with a clear 429 instead.
        if delay <= 0 or delay > max_delay:
            return 0.0
        with self._lock:
            self._limits[self._limit_key(url)] = RateLimit(state.limit, None, None)
        return delay

    def error(self, url: str, response: httpx.Response) -> DeadlockError:
        text = response.text
        try:
            body: Any = json.loads(text) if text else None
        except ValueError:
            body = text
        status = response.status_code
        detail = _message(body, text)
        retry_after = parse_retry_after(response.headers.get("retry-after"))
        message = f"Deadlock API responded with {status}" + (f": {detail}" if detail else "")
        retryable = status in RETRYABLE_STATUS
        code: ErrorCode = "HTTP_ERROR"
        if status == 400:
            code = "BAD_REQUEST"
        elif status == 403:
            code = "FORBIDDEN"
            message += ". The player may have opted out of data collection."
        elif status == 404:
            code = "NOT_FOUND"
        elif status == 429:
            code = "RATE_LIMITED"
        elif status == 503:
            code = "SERVICE_BUSY"
        elif status == 504:
            code = "QUERY_TIMEOUT"
            message += ". The query is too heavy, narrow it down (time range, filters)."
        return DeadlockError(
            message,
            code=code,
            url=url,
            status=status,
            body=body,
            retryable=retryable,
            retry_after=retry_after,
        )

    def retry_delay(self, error: DeadlockError, attempt: int) -> float | None:
        if not self.retry or not error.retryable or attempt > self.retry.retries:
            return None
        if error.retry_after is not None:
            wait: float = error.retry_after
            return wait if wait <= self.retry.max_delay else None
        exp = min(self.retry.max_delay, self.retry.min_delay * 2.0 ** (attempt - 1))
        return exp / 2 + random.random() * exp / 2

    def parse(self, url: str, response: httpx.Response, kind: ResponseKind) -> Any:
        if kind == "bytes":
            return response.content
        if kind == "text":
            return response.text
        if response.status_code == 204 or not response.content:
            return None
        try:
            return response.json()
        except ValueError as exc:
            raise DeadlockError(
                "Expected a JSON response",
                code="INVALID_RESPONSE",
                url=url,
                status=response.status_code,
                body=response.text[:500],
            ) from exc

    def network_error(self, url: str, exc: Exception) -> DeadlockError:
        if isinstance(exc, httpx.TimeoutException):
            return DeadlockError(f"Request timed out: {url}", code="TIMEOUT", url=url, retryable=True)
        return DeadlockError(
            f"Network error while requesting {url}: {exc}", code="NETWORK_ERROR", url=url, retryable=True
        )


class SyncTransport(_Policy):
    def __init__(self, *, client: httpx.Client | None = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._owns_client = client is None
        self.client = client or httpx.Client(follow_redirects=True)

    def close(self) -> None:
        if self._owns_client:
            self.client.close()

    def request(
        self,
        method: str,
        path: str,
        *,
        query: Query | None = None,
        body: Any = None,
        kind: ResponseKind = "json",
        timeout: float | None = None,
    ) -> Any:
        url = self.url(path)
        attempts = (self.retry.retries + 1) if self.retry and method == "GET" else 1
        attempt = 0
        while True:
            attempt += 1
            wait = self.throttle_delay(url)
            if wait:
                time.sleep(wait)
            try:
                try:
                    response = self.client.request(
                        method,
                        url,
                        params=encode_query(query),
                        json=body,
                        headers=self.headers,
                        timeout=timeout or self.timeout,
                    )
                except httpx.HTTPError as exc:
                    raise self.network_error(url, exc) from exc
                self.record(url, response.headers)
                if response.is_error:
                    raise self.error(url, response)
                return self.parse(url, response, kind)
            except DeadlockError as error:
                delay = self.retry_delay(error, attempt) if attempt < attempts else None
                if delay is None:
                    error.attempts = attempt
                    raise
                if self.on_retry:
                    self.on_retry(RetryEvent(url, attempt, delay, error))
                time.sleep(delay)


class AsyncTransport(_Policy):
    def __init__(self, *, client: httpx.AsyncClient | None = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._owns_client = client is None
        self.client = client or httpx.AsyncClient(follow_redirects=True)
        self._inflight: dict[str, asyncio.Future[Any]] = {}

    async def close(self) -> None:
        if self._owns_client:
            await self.client.aclose()

    async def request(
        self,
        method: str,
        path: str,
        *,
        query: Query | None = None,
        body: Any = None,
        kind: ResponseKind = "json",
        timeout: float | None = None,
    ) -> Any:
        if method != "GET":
            return await self._execute(method, path, query, body, kind, timeout)
        # Identical concurrent GETs (think asyncio.gather) share one request.
        key = f"{kind} {self.url(path)}?{sorted(encode_query(query).items())}"
        existing = self._inflight.get(key)
        if existing is not None:
            return await asyncio.shield(existing)
        task = asyncio.ensure_future(self._execute(method, path, query, body, kind, timeout))
        self._inflight[key] = task
        try:
            return await asyncio.shield(task)
        finally:
            if task.done():
                self._inflight.pop(key, None)
            else:
                task.add_done_callback(lambda _: self._inflight.pop(key, None))

    async def _execute(
        self,
        method: str,
        path: str,
        query: Query | None,
        body: Any,
        kind: ResponseKind,
        timeout: float | None,
    ) -> Any:
        url = self.url(path)
        attempts = (self.retry.retries + 1) if self.retry and method == "GET" else 1
        attempt = 0
        while True:
            attempt += 1
            wait = self.throttle_delay(url)
            if wait:
                await asyncio.sleep(wait)
            try:
                try:
                    response = await self.client.request(
                        method,
                        url,
                        params=encode_query(query),
                        json=body,
                        headers=self.headers,
                        timeout=timeout or self.timeout,
                    )
                except httpx.HTTPError as exc:
                    raise self.network_error(url, exc) from exc
                self.record(url, response.headers)
                if response.is_error:
                    raise self.error(url, response)
                return self.parse(url, response, kind)
            except DeadlockError as error:
                delay = self.retry_delay(error, attempt) if attempt < attempts else None
                if delay is None:
                    error.attempts = attempt
                    raise
                if self.on_retry:
                    self.on_retry(RetryEvent(url, attempt, delay, error))
                await asyncio.sleep(delay)
