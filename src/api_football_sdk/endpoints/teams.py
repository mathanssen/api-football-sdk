"""
Endpoints for retrieving team metadata and statistics.

This module wraps the `/teams`, `/teams/statistics`, `/teams/seasons`,
and `/teams/countries` endpoints from the API Football.

Usage example:
--------------
    from api_football_sdk.endpoints.teams import get_team_by_id

    team = await get_team_by_id(team_id=33)
    print(team)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client

__all__: list[str] = [
    "get_team_statistics",
    "get_team_by_id",
    "get_team_seasons",
    "get_teams_countries",
]


async def get_team_statistics(
    team_id: int,
    league_id: int,
    season: int,
) -> dict[str, Any]:
    """
    Get full team performance statistics in a specific league and season.

    :param team_id: Unique ID of the team.
    :param league_id: ID of the league the team played in.
    :param season: Year of the season (e.g., 2020).
    :return: Detailed performance metrics for the team.
    """
    client = get_client()
    response = await client.get(
        "/teams/statistics",
        params={"team": team_id, "league": league_id, "season": season},
    )
    return response.json().get("response", {})


async def get_team_by_id(team_id: int) -> dict[str, Any]:
    """
    Get metadata for a single team by its ID.

    :param team_id: Unique ID of the team.
    :return: Metadata for the given team (name, logo, founded year, etc.).
    """
    client = get_client()
    response = await client.get("/teams", params={"id": team_id})
    results = response.json().get("response", [])
    return results[0] if results else {}


async def get_team_seasons(team_id: int) -> list[int]:
    """
    Get a list of seasons in which the team has played.

    :param team_id: Unique ID of the team.
    :return: List of season years the team participated in.
    """
    client = get_client()
    response = await client.get("/teams/seasons", params={"team": team_id})
    return response.json().get("response", [])


async def get_teams_countries() -> list[dict[str, Any]]:
    """
    Get a list of all countries that have teams in the API.

    :return: Each entry contains the country name and its code.
    """
    client = get_client()
    response = await client.get("/teams/countries")
    return response.json().get("response", [])
