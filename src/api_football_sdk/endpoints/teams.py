"""
Endpoints for retrieving team metadata and statistics.

This module wraps the `/teams`, `/teams/statistics`, `/teams/seasons`,
and `/teams/countries` endpoints from the API Football.

Usage example:
--------------
    from api_football.endpoints.teams import get_team_by_id

    team = await get_team_by_id(team_id=33)
    print(team)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client


async def get_team_statistics(
    team_id: int, league_id: int, season: int
) -> dict[str, Any]:
    """
    Get full team performance statistics in a specific league and season.

    Parameters
    ----------
    team_id : int
        Unique ID of the team.
    league_id : int
        ID of the league the team played in.
    season : int
        Year of the season (e.g., 2020).

    Returns
    -------
    dict
        Detailed performance metrics for the team.
    """
    client = get_client()
    response = await client.get(
        "/teams/statistics",
        params={"team": team_id, "league": league_id, "season": season},
    )
    return response.json()["response"]


async def get_team_by_id(team_id: int) -> dict[str, Any]:
    """
    Get metadata for a single team by its ID.

    Parameters
    ----------
    team_id : int
        Unique ID of the team.

    Returns
    -------
    dict
        Metadata for the given team (name, logo, founded year, etc.).
    """
    client = get_client()
    response = await client.get("/teams", params={"id": team_id})
    return response.json()["response"][0]


async def get_team_seasons(team_id: int) -> list[int]:
    """
    Get a list of seasons in which the team has played.

    Parameters
    ----------
    team_id : int
        Unique ID of the team.

    Returns
    -------
    list of int
        Season years in which the team participated in competitions.
    """
    client = get_client()
    response = await client.get("/teams/seasons", params={"team": team_id})
    return response.json()["response"]


async def get_teams_countries() -> list[dict[str, Any]]:
    """
    Get a list of all countries that have teams in the API.

    Returns
    -------
    list of dict
        Each entry contains the country name and its code.
    """
    client = get_client()
    response = await client.get("/teams/countries")
    return response.json()["response"]
