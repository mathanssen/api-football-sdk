"""
Endpoints for retrieving league metadata and filters.

This module wraps the `/leagues` endpoint of the API Football,
supporting filters by ID, country, season, type, team, and more.

Usage example:
--------------
    from api_football_sdk.endpoints.leagues import get_all_leagues

    leagues = await get_all_leagues()
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client

__all__: list[str] = [
    "get_all_leagues",
    "get_league_by_id",
    "get_leagues_by_country",
    "get_leagues_by_country_code",
    "get_leagues_by_season",
    "get_leagues_by_team",
    "get_leagues_by_type",
    "get_current_leagues",
]


async def get_all_leagues() -> list[dict[str, Any]]:
    """
    Get a list of all leagues supported by the API.

    :return: List of leagues with associated metadata and coverage.
    """
    client = get_client()
    response = await client.get("/leagues")
    return response.json().get("response", [])


async def get_league_by_id(league_id: int) -> dict[str, Any]:
    """
    Get details for a specific league by its ID.

    :param league_id: The unique ID of the league.
    :return: Metadata and coverage for the league.
    """
    client = get_client()
    response = await client.get("/leagues", params={"id": league_id})
    results = response.json().get("response", [])
    return results[0] if results else {}


async def get_leagues_by_country(country_name: str) -> list[dict[str, Any]]:
    """
    Get all leagues played in a given country by name.

    :param country_name: Country name (e.g., "England").
    :return: List of leagues in the given country.
    """
    client = get_client()
    response = await client.get("/leagues", params={"country": country_name})
    return response.json().get("response", [])


async def get_leagues_by_country_code(country_code: str) -> list[dict[str, Any]]:
    """
    Get all leagues for a country using its ISO code (e.g., "IT", "BR").

    :param country_code: ISO 3166-1 alpha-2 country code.
    :return: List of leagues in the given country code.
    """
    client = get_client()
    response = await client.get("/leagues", params={"code": country_code})
    return response.json().get("response", [])


async def get_leagues_by_season(season: int) -> list[dict[str, Any]]:
    """
    Get all leagues that were active in a specific season.

    :param season: Season year (e.g., 2020).
    :return: Leagues active during the given season.
    """
    client = get_client()
    response = await client.get("/leagues", params={"season": season})
    return response.json().get("response", [])


async def get_leagues_by_team(team_id: int) -> list[dict[str, Any]]:
    """
    Get all leagues in which a specific team is participating.

    :param team_id: Team ID.
    :return: Leagues where the team has played.
    """
    client = get_client()
    response = await client.get("/leagues", params={"team": team_id})
    return response.json().get("response", [])


async def get_leagues_by_type(competition_type: str) -> list[dict[str, Any]]:
    """
    Get leagues filtered by type: "league" or "cup".

    :param competition_type: Type of competition ("league" or "cup").
    :return: Leagues matching the given type.
    """
    client = get_client()
    response = await client.get("/leagues", params={"type": competition_type})
    return response.json().get("response", [])


async def get_current_leagues() -> list[dict[str, Any]]:
    """
    Get all leagues that are currently active.

    :return: Leagues currently in progress.
    """
    client = get_client()
    response = await client.get("/leagues", params={"current": "true"})
    return response.json().get("response", [])
