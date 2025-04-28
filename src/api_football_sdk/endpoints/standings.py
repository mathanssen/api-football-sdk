"""
Endpoints related to league standings and team positions.

This module provides typed wrappers around the /standings
endpoint of the API Football.

Usage example:
--------------
    from api_football_sdk.endpoints.standings import get_standings_by_league

    standings = await get_standings_by_league(league_id=39, season=2020)
    print(standings)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client

__all__: list[str] = ["get_standings_by_league", "get_standings_by_team"]


async def get_standings_by_league(league_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get the full standings table for a given league and season.

    :param league_id: The unique ID of the league (e.g., 39 for Premier League).
    :param season: The year of the season (e.g., 2020).
    :return: List where each element represents a team in the standings.
    """
    client = get_client()
    response = await client.get(
        "/standings",
        params={"league": league_id, "season": season},
    )
    return response.json().get("response", [])


async def get_standings_by_team(team_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get the standings group(s) that include a specific team in a given season.

    Useful when you don't know the league ID but have the team ID.

    :param team_id: The unique ID of the team.
    :param season: The season year (e.g., 2020).
    :return: List of standings groups containing the specified team.
    """
    client = get_client()
    response = await client.get(
        "/standings",
        params={"team": team_id, "season": season},
    )
    return response.json().get("response", [])
