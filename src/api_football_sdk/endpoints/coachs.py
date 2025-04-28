"""
Endpoints for retrieving coaches' metadata.

This module wraps the `/coachs` endpoint of the API Football,
allowing queries by team or by coach ID.

Usage example:
--------------
    from api_football.endpoints.coaches import get_coach_by_team

    coach = await get_coach_by_team(team_id=33)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client


async def get_coach_by_team(team_id: int) -> dict[str, Any]:
    """
    Get the coach currently associated with a given team.

    Parameters
    ----------
    team_id : int
        The ID of the team.

    Returns
    -------
    dict
        Metadata about the coach (name, nationality, photo, etc.).
    """
    client = get_client()
    response = await client.get("/coachs", params={"team": team_id})
    results = response.json()["response"]

    if not results:
        return {}

    return results[0]


async def get_coach_by_id(coach_id: int) -> dict[str, Any]:
    """
    Get detailed information about a specific coach by ID.

    Parameters
    ----------
    coach_id : int
        The ID of the coach.

    Returns
    -------
    dict
        Metadata about the coach.
    """
    client = get_client()
    response = await client.get("/coachs", params={"id": coach_id})
    results = response.json()["response"]

    if not results:
        return {}

    return results[0]
