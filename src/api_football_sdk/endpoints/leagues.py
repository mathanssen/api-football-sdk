"""
Endpoints for retrieving league metadata and filters.

This module wraps the `/leagues` endpoint of the API Football,
supporting filters by ID, country, season, type, team, and more.

Usage example:
--------------
    from api_football.endpoints.leagues import get_all_leagues

    leagues = await get_all_leagues()
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client


async def get_all_leagues() -> list[dict[str, Any]]:
    """
    Get a list of all leagues supported by the API.

    Returns
    -------
    list of dict
        List of leagues with associated metadata and coverage.
    """
    client = get_client()
    response = await client.get("/leagues")
    return response.json()["response"]


async def get_league_by_id(league_id: int) -> dict[str, Any]:
    """
    Get details for a specific league by its ID.

    Parameters
    ----------
    league_id : int
        The unique ID of the league.

    Returns
    -------
    dict
        Metadata and coverage for the league.
    """
    client = get_client()
    response = await client.get("/leagues", params={"id": league_id})
    return response.json()["response"][0]


async def get_leagues_by_country(country_name: str) -> list[dict[str, Any]]:
    """
    Get all leagues played in a given country by name.

    Parameters
    ----------
    country_name : str
        Country name (e.g., "England").

    Returns
    -------
    list of dict
        List of leagues in the given country.
    """
    client = get_client()
    response = await client.get("/leagues", params={"country": country_name})
    return response.json()["response"]


async def get_leagues_by_country_code(country_code: str) -> list[dict[str, Any]]:
    """
    Get all leagues for a country using its ISO code (e.g., "IT", "BR").

    Parameters
    ----------
    country_code : str
        ISO 3166-1 alpha-2 country code.

    Returns
    -------
    list of dict
        List of leagues in the given country code.
    """
    client = get_client()
    response = await client.get("/leagues", params={"code": country_code})
    return response.json()["response"]


async def get_leagues_by_season(season: int) -> list[dict[str, Any]]:
    """
    Get all leagues that were active in a specific season.

    Parameters
    ----------
    season : int
        Season year (e.g., 2020).

    Returns
    -------
    list of dict
        Leagues active during the given season.
    """
    client = get_client()
    response = await client.get("/leagues", params={"season": season})
    return response.json()["response"]


async def get_leagues_by_team(team_id: int) -> list[dict[str, Any]]:
    """
    Get all leagues in which a specific team is participating.

    Parameters
    ----------
    team_id : int
        Team ID.

    Returns
    -------
    list of dict
        Leagues where the team has played.
    """
    client = get_client()
    response = await client.get("/leagues", params={"team": team_id})
    return response.json()["response"]


async def get_leagues_by_type(competition_type: str) -> list[dict[str, Any]]:
    """
    Get leagues filtered by type: "league" or "cup".

    Parameters
    ----------
    competition_type : str
        Type of competition ("league" or "cup").

    Returns
    -------
    list of dict
        Leagues matching the given type.
    """
    client = get_client()
    response = await client.get("/leagues", params={"type": competition_type})
    return response.json()["response"]


async def get_current_leagues() -> list[dict[str, Any]]:
    """
    Get all leagues that are currently active.

    Returns
    -------
    list of dict
        Leagues currently in progress.
    """
    client = get_client()
    response = await client.get("/leagues", params={"current": "true"})
    return response.json()["response"]
