"""Errors raised by the SDK. Every failure is a ``DeadlockError`` with a ``code``."""

from __future__ import annotations

from typing import Any, Literal

ErrorCode = Literal[
    "BAD_REQUEST",
    "FORBIDDEN",
    "NOT_FOUND",
    "RATE_LIMITED",
    "SERVICE_BUSY",
    "QUERY_TIMEOUT",
    "HTTP_ERROR",
    "NETWORK_ERROR",
    "TIMEOUT",
    "INVALID_RESPONSE",
    "INVALID_INPUT",
]


class DeadlockError(Exception):
    """Raised for every failed call.

    ``code`` is stable and meant for branching, the message is for humans.
    ``retry_after`` (seconds) is set when the API asked to wait.
    """

    def __init__(
        self,
        message: str,
        *,
        code: ErrorCode,
        url: str = "",
        status: int | None = None,
        body: Any = None,
        retryable: bool = False,
        retry_after: float | None = None,
        attempts: int = 1,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code: ErrorCode = code
        self.url = url
        self.status = status
        self.body = body
        self.retryable = retryable
        self.retry_after = retry_after
        self.attempts = attempts

    def __repr__(self) -> str:
        status = f", status={self.status}" if self.status else ""
        return f"DeadlockError(code={self.code!r}{status}, message={self.message!r})"


def invalid_input(message: str) -> DeadlockError:
    return DeadlockError(message, code="INVALID_INPUT")
