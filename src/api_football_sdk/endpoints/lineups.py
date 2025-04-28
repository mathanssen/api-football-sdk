"""
Endpoints for retrieving starting lineups and formations.

This module provides typed access to the `/fixtures/lineups`
endpoint of the API Football.

Usage example:
--------------
    from api_football_sdk.endpoints.lineups import get_lineups_by_fixture

    lineups = await get_lineups_by_fixture(fixture_id=215662)
    print(lineups)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client

__all__: list[str] = ["get_lineups_by_fixture", "get_lineups_by_fixture_and_team"]


async def get_lineups_by_fixture(fixture_id: int) -> list[dict[str, Any]]:
    """
    Get the full lineup (starting XI, substitutes, coach) for both teams
    in a given fixture.

    :param fixture_id: The ID of the fixture.
    :return: Lineups information for both home and away teams.
    """
    client = get_client()
    response = await client.get("/fixtures/lineups", params={"fixture": fixture_id})
    return response.json().get("response", [])


async def get_lineups_by_fixture_and_team(
    fixture_id: int,
    team_id: int,
) -> dict[str, Any]:
    """
    Get the lineup for a specific team in a given fixture.

    :param fixture_id: The ID of the fixture.
    :param team_id: The ID of the team.
    :return: Lineup information for the selected team.
    """
    client = get_client()
    response = await client.get(
        "/fixtures/lineups",
        params={"fixture": fixture_id, "team": team_id},
    )
    results = response.json().get("response", [])
    return results[0] if results else {}
