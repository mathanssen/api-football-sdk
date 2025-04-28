"""
Custom exception hierarchy for api-football-sdk.

These exceptions provide clear and structured error handling
for both HTTP-level issues (e.g., 4xx, 5xx) and SDK misuse.

Typical usage:
--------------
    from api_football.exceptions import APIFootballError

    try:
        await client.get("/fixtures")
    except APIFootballError as exc:
        logger.error("Something went wrong: %s", exc)
"""

from __future__ import annotations

from typing import Final

import httpx


class APIFootballError(Exception):
    """
    Base exception for all errors raised by this SDK.

    All domain-specific exceptions should inherit from this.
    """

    def __init__(self, message: str = "") -> None:
        super().__init__(message)


class APIFootballRequestError(APIFootballError):
    """
    Raised when a network-level issue occurs (e.g., DNS failure,
    timeouts, connection errors).

    Wraps `httpx.RequestError`.
    """

    def __init__(self, original: httpx.RequestError) -> None:
        self.original: Final[httpx.RequestError] = original
        super().__init__(f"Request error: {original}")


class APIFootballHTTPError(APIFootballError):
    """
    Raised when the API returns a non-success status code (e.g., 401, 404, 500).

    Wraps `httpx.HTTPStatusError`.
    """

    def __init__(self, original: httpx.HTTPStatusError) -> None:
        self.status_code: Final[int] = original.response.status_code
        self.original: Final[httpx.HTTPStatusError] = original
        super().__init__(f"HTTP error {self.status_code}: {original.response.text[:200]}")

    @classmethod
    def from_response(cls, response: httpx.Response) -> APIFootballHTTPError:
        """
        Builds the error from a raw `httpx.Response`.

        :param response: The HTTP response to wrap in an exception.
        :return: An instance of `APIFootballHTTPError`.
        """
        request = getattr(response, "request", None)

        exc = httpx.HTTPStatusError(
            message=f"Error response {response.status_code}",
            request=request,
            response=response,
        )
        return cls(exc)


class APIFootballRateLimitError(APIFootballHTTPError):
    """
    Raised when the API responds with HTTP 429 (too many requests).
    """


class ConfigurationError(APIFootballError):
    """
    Raised when the SDK is misconfigured (e.g., missing API key).
    """


class UnsupportedOperation(APIFootballError):
    """
    Raised when a requested feature is not supported by the current API plan or version.
    """


class ParsingError(APIFootballError):
    """
    Raised when the response could not be parsed into a valid model.
    """


NetworkError = APIFootballRequestError
ServerError = APIFootballHTTPError
ClientError = APIFootballHTTPError
