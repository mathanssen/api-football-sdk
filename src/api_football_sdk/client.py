"""
HTTP client for interacting with the API Football endpoints.

This module wraps `httpx.AsyncClient`, injecting authentication headers
and providing automatic retry with exponential backoff on transient failures.

Usage example:
--------------
    from api_football_sdk.client import get_client

    async with get_client() as client:
        response = await client.get("/timezone")
        print(response.json())
"""

from __future__ import annotations

import asyncio
import logging
from types import TracebackType
from typing import Any, Optional, Type

import httpx

from api_football_sdk.config import settings
from api_football_sdk.exceptions import (
    APIFootballHTTPError,
    APIFootballRateLimitError,
    APIFootballRequestError,
)

__all__: list[str] = ["ApiFootballClient", "get_client"]

logger = logging.getLogger(__name__)


class ApiFootballClient:
    """
    Asynchronous API Football client with automatic retries.

    Should be reused across the entire application lifecycle to take
    advantage of connection pooling and efficient resource usage.
    """

    DEFAULT_TIMEOUT: float = 10.0
    MAX_RETRIES: int = 3
    BACKOFF_FACTOR: float = 0.5

    def __init__(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
    ) -> None:
        self._timeout = timeout or self.DEFAULT_TIMEOUT
        self._max_retries = max_retries or self.MAX_RETRIES
        self._client = httpx.AsyncClient(
            base_url=str(settings.api_base_url),
            headers=settings.default_headers,
            timeout=self._timeout,
            follow_redirects=True,
        )

    async def __aenter__(self) -> ApiFootballClient:
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        """
        Close the underlying AsyncClient connection.

        :return: None
        """
        await self._client.aclose()

    async def request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
    ) -> httpx.Response:
        """
        Perform an HTTP request with retry logic on transient errors.

        :param method: HTTP method (GET, POST, etc.).
        :param url: Endpoint relative path (e.g., "/fixtures").
        :param params: Query string parameters.
        :param json: Request body (for POST/PUT methods).
        :return: The HTTP response object.
        :raises APIFootballHTTPError: On API-related HTTP errors.
        :raises APIFootballRateLimitError: On HTTP 429 Too Many Requests.
        :raises APIFootballRequestError: On network-level request failures.
        """
        attempt = 0

        while True:
            try:
                response = await self._client.request(
                    method=method,
                    url=url,
                    params=params,
                    json=json,
                )

                if response.status_code == 429:
                    raise APIFootballRateLimitError.from_response(response)
                if response.status_code >= 500:
                    raise APIFootballHTTPError.from_response(response)

                response.raise_for_status()
                return response

            except httpx.HTTPStatusError as exc:
                raise APIFootballHTTPError(exc) from exc

            except httpx.RequestError as exc:
                attempt += 1
                if attempt > self._max_retries:
                    logger.error(
                        "Request failed after %d attempts: %s",
                        attempt,
                        exc,
                    )
                    raise APIFootballRequestError(exc) from exc

                backoff_time = self.BACKOFF_FACTOR * (2 ** (attempt - 1))
                logger.warning(
                    "Transient error on attempt %d/%d: %s. Retrying in %.2fs...",
                    attempt,
                    self._max_retries,
                    exc,
                    backoff_time,
                )
                await asyncio.sleep(backoff_time)

    async def get(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
    ) -> httpx.Response:
        """
        Perform a GET request.

        :param url: Endpoint relative path.
        :param params: Query string parameters.
        :return: HTTP response.
        """
        return await self.request("GET", url, params=params)

    async def post(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
    ) -> httpx.Response:
        """
        Perform a POST request.

        :param url: Endpoint relative path.
        :param params: Query string parameters.
        :param json: Request body payload.
        :return: HTTP response.
        """
        return await self.request("POST", url, params=params, json=json)


_client_instance: Optional[ApiFootballClient] = None


def get_client() -> ApiFootballClient:
    """
    Return a singleton instance of the API Football client.

    :return: A singleton instance of `ApiFootballClient`.
    """
    global _client_instance
    if _client_instance is None:
        _client_instance = ApiFootballClient()
    return _client_instance
