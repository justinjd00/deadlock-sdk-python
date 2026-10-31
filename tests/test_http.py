from __future__ import annotations

import time
from typing import Any

import httpx
import pytest
import respx

from deadlock_sdk import AsyncDeadlock, Deadlock, DeadlockError, RetryEvent, RetryPolicy, parse_retry_after
from deadlock_sdk._http import encode_query

URL = "https://api.deadlock-api.com/v1/info"
FAST = RetryPolicy(retries=2, min_delay=0.001, max_delay=0.05)


def client(**kwargs: Any) -> Deadlock:
    return Deadlock(cache=False, user_agent=None, **{"retry": FAST, **kwargs})


def test_encodes_queries_like_the_api_expects() -> None:
    q = encode_query({"account_ids": [1, 2, 3], "only_active": True, "x": None, "y": "", "z": 0, "e": []})
    assert q == {"account_ids": "1,2,3", "only_active": "true", "z": "0"}


@respx.mock
def test_sends_api_key_and_user_agent() -> None:
    route = respx.get(URL).respond(json={})
    with Deadlock(api_key="secret", user_agent="tests/1", cache=False) as dl:
        dl.info()
    headers = route.calls.last.request.headers
    assert headers["X-API-KEY"] == "secret"
    assert headers["User-Agent"] == "tests/1"


@respx.mock
def test_retries_a_busy_server_and_honors_retry_after() -> None:
    events: list[RetryEvent] = []
    respx.get(URL).mock(
        side_effect=[
            httpx.Response(503, text="busy", headers={"retry-after": "0"}),
            httpx.Response(200, json={"ok": 1}),
        ]
    )
    with client(on_retry=events.append) as dl:
        assert dl.info() == {"ok": 1}
    assert len(events) == 1
    assert events[0].delay == 0
    assert events[0].error.code == "SERVICE_BUSY"


@respx.mock
def test_never_retries_a_504_query_timeout() -> None:
    route = respx.get(URL).respond(504, text="Query timed out", headers={"retry-after": "1"})
    with client() as dl, pytest.raises(DeadlockError) as info:
        dl.info()
    assert info.value.code == "QUERY_TIMEOUT"
    assert info.value.retryable is False
    assert route.call_count == 1


@pytest.mark.parametrize(("status", "code"), [(400, "BAD_REQUEST"), (403, "FORBIDDEN"), (404, "NOT_FOUND")])
@respx.mock
def test_maps_status_codes_with_the_server_message(status: int, code: str) -> None:
    respx.get(URL).respond(status, json={"error": "nope"})
    with client() as dl, pytest.raises(DeadlockError) as info:
        dl.info()
    assert info.value.code == code
    assert info.value.status == status
    assert "nope" in info.value.message
    assert info.value.attempts == 1


@respx.mock
def test_gives_up_after_the_configured_retries() -> None:
    route = respx.get(URL).respond(502)
    with client() as dl, pytest.raises(DeadlockError) as info:
        dl.info()
    assert info.value.attempts == 3
    assert route.call_count == 3


@respx.mock
def test_does_not_retry_writes() -> None:
    route = respx.post("https://api.deadlock-api.com/v1/x").respond(503)
    with client() as dl, pytest.raises(DeadlockError):
        dl.api.request("post", "/v1/x", json={"a": 1})
    assert route.call_count == 1
    assert route.calls.last.request.content == b'{"a":1}'


@respx.mock
def test_wraps_network_errors_and_retries_them() -> None:
    respx.get(URL).mock(side_effect=[httpx.ConnectError("boom"), httpx.Response(200, json=[1])])
    with client() as dl:
        assert dl.api.request("get", "/v1/info") == [1]


@respx.mock
def test_times_out() -> None:
    respx.get(URL).mock(side_effect=httpx.ReadTimeout("slow"))
    with client(retry=None) as dl, pytest.raises(DeadlockError) as info:
        dl.info()
    assert info.value.code == "TIMEOUT"


@respx.mock
def test_rejects_non_json_bodies() -> None:
    respx.get(URL).respond(200, text="<html>oops</html>")
    with client() as dl, pytest.raises(DeadlockError) as info:
        dl.info()
    assert info.value.code == "INVALID_RESPONSE"


@respx.mock
def test_waits_for_the_rate_limit_window_instead_of_running_into_429(monkeypatch: pytest.MonkeyPatch) -> None:
    slept: list[float] = []
    monkeypatch.setattr(time, "sleep", slept.append)
    headers = {"ratelimit-limit": "200", "ratelimit-remaining": "0", "ratelimit-reset": "2"}
    route = respx.get(URL).mock(
        side_effect=[httpx.Response(200, json={}, headers=headers), httpx.Response(200, json={"second": 1})]
    )
    with client(retry=RetryPolicy(max_delay=5)) as dl:
        dl.info()
        state = dl.rate_limit("/v1/info")
        assert state is not None
        assert (state.limit, state.remaining) == (200, 0)
        assert dl.info(options=None) == {"second": 1}
    assert route.call_count == 2
    assert len(slept) == 1
    assert 1.5 < slept[0] <= 2


def test_parses_retry_after() -> None:
    assert parse_retry_after("3") == 3
    assert parse_retry_after(None) is None
    assert parse_retry_after("garbage") is None
    future = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(time.time() + 30))
    assert 20 < (parse_retry_after(future) or 0) <= 30


@respx.mock
async def test_async_shares_identical_concurrent_requests() -> None:
    import asyncio

    route = respx.get(URL).respond(json={"n": 1})
    async with AsyncDeadlock(cache=False, retry=None) as dl:
        a, b = await asyncio.gather(dl.info(), dl.info())
    assert a == b == {"n": 1}
    assert route.call_count == 1


@respx.mock
async def test_async_retries_like_sync() -> None:
    respx.get(URL).mock(
        side_effect=[httpx.Response(503, headers={"retry-after": "0"}), httpx.Response(200, json=[2])]
    )
    async with AsyncDeadlock(cache=False, retry=FAST) as dl:
        assert await dl.api.request("get", "/v1/info") == [2]
