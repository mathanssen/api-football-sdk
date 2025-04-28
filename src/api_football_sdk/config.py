"""
Runtime configuration for api-football-sdk.

This module defines the Settings class, which loads environment variables,
validates them, and exposes them globally through a single frozen instance.

All settings are strongly typed and validated at import time.
"""

from __future__ import annotations

import functools
from typing import Final, Mapping

from pydantic import AnyHttpUrl, Field, field_validator
from pydantic_settings import BaseSettings

__all__: Final[list[str]] = ["Settings", "settings"]


class Settings(BaseSettings):
    """
    Strongly-typed application settings.

    All attributes are validated at import time to ensure correct
    configuration before the application runs.
    """

    api_key: str = Field(..., alias="API_FOOTBALL_KEY")
    api_host: str = Field(
        default="api-football-v1.p.rapidapi.com",
        alias="API_FOOTBALL_HOST",
    )
    api_base_url: AnyHttpUrl = Field(
        default="https://api-football-v1.p.rapidapi.com/v3",
        alias="API_FOOTBALL_BASE_URL",
    )
    http_timeout: float = Field(10.0, alias="API_FOOTBALL_HTTP_TIMEOUT")
    http_max_retries: int = Field(3, alias="API_FOOTBALL_HTTP_MAX_RETRIES")
    http_backoff_factor: float = Field(0.5, alias="API_FOOTBALL_HTTP_BACKOFF_FACTOR")
    user_agent: str = Field(default="api-football-sdk/1.0", alias="USER_AGENT")

    model_config: Final[dict[str, object]] = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
        "populate_by_name": True,
    }

    @functools.cached_property
    def default_headers(self) -> Mapping[str, str]:
        """
        HTTP headers that must accompany every request.

        :return: A mapping of default HTTP headers.
        """
        return {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.api_host,
            "User-Agent": self.user_agent,
            "Accept": "application/json",
        }

    @field_validator("http_timeout", "http_backoff_factor", mode="before")
    @classmethod
    def _validate_positive_float(cls, value: float) -> float:
        """
        Ensure positive floats for timeout and backoff factor.

        :param value: The value to validate.
        :return: The validated positive float.
        :raises ValueError: If the value is not positive.
        """
        if isinstance(value, str):
            value = float(value)
        if value <= 0:
            raise ValueError("must be greater than 0")
        return value

    @field_validator("http_max_retries", mode="before")
    @classmethod
    def _validate_non_negative(cls, value: int) -> int:
        """
        Ensure a non-negative retry count.

        :param value: The value to validate.
        :return: The validated non-negative integer.
        :raises ValueError: If the value is negative.
        """
        if isinstance(value, str):
            value = int(value)
        if value < 0:
            raise ValueError("must be greater than or equal to 0")
        return value


settings: Final[Settings] = Settings()
