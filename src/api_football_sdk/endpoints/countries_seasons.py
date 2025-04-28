"""
Reference endpoints for retrieving seasons and countries.

These are general-purpose endpoints useful for populating dropdowns
or validating available filters in the API.

Usage example:
--------------
    from api_football.endpoints.reference import get_supported_seasons

    seasons = await get_supported_seasons()
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client


async def get_supported_seasons() -> list[int]:
    """
    Get a list of all seasons supported by the API.

    Returns
    -------
    list of int
        Season years (e.g., [2008, 2009, ..., 2024]).
    """
    client = get_client()
    response = await client.get("/leagues/seasons")
    return response.json()["response"]


async def get_supported_countries() -> list[dict[str, Any]]:
    """
    Get a list of all countries that appear in the API.

    Returns
    -------
    list of dict
        Each entry includes the country name and code.
    """
    client = get_client()
    response = await client.get("/countries")
    return response.json()["response"]
