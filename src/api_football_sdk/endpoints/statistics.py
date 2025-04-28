"""
Endpoints for retrieving match statistics.

This module provides typed access to the `/fixtures/statistics`
endpoint of the API Football.

Usage example:
--------------
    from api_football.endpoints.statistics import get_statistics_by_fixture

    stats = await get_statistics_by_fixture(fixture_id=215662)
    print(stats)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client


async def get_statistics_by_fixture(fixture_id: int) -> list[dict[str, Any]]:
    """
    Get all statistics available for a given fixture.

    Parameters
    ----------
    fixture_id : int
        The ID of the fixture.

    Returns
    -------
    list of dict
        List of statistics per team.
    """
    client = get_client()
    response = await client.get("/fixtures/statistics", params={"fixture": fixture_id})
    return response.json()["response"]


async def get_statistics_by_fixture_and_type(
    fixture_id: int, stat_type: str
) -> list[dict[str, Any]]:
    """
    Get statistics filtered by a specific type (e.g., "Shots on Goal") for a fixture.

    Parameters
    ----------
    fixture_id : int
        The ID of the fixture.
    stat_type : str
        The type of statistic to filter (e.g., "Shots on Goal", "Yellow Cards").

    Returns
    -------
    list of dict
        List of filtered statistics matching the requested type.
    """
    client = get_client()
    response = await client.get(
        "/fixtures/statistics", params={"fixture": fixture_id, "type": stat_type}
    )
    return response.json()["response"]


async def get_statistics_by_fixture_and_team(
    fixture_id: int, team_id: int
) -> list[dict[str, Any]]:
    """
    Get statistics for a specific team in a given fixture.

    Parameters
    ----------
    fixture_id : int
        The ID of the fixture.
    team_id : int
        The ID of the team.

    Returns
    -------
    list of dict
        List of statistics for the selected team.
    """
    client = get_client()
    response = await client.get(
        "/fixtures/statistics", params={"fixture": fixture_id, "team": team_id}
    )
    return response.json()["response"]
