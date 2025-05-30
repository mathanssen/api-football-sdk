"""
Endpoints for retrieving match events (goals, cards, substitutions, etc).

This module wraps the `/fixtures/events` endpoint of the API Football
and allows filtering by fixture, player, or team.

Usage example:
--------------
    from api_football_sdk.endpoints.events import get_events_by_fixture

    events = await get_events_by_fixture(fixture_id=215662)
    print(events)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client

__all__: list[str] = [
    "get_events_by_fixture",
    "get_events_by_fixture_and_player",
    "get_events_by_fixture_and_team",
]


async def get_events_by_fixture(fixture_id: int) -> list[dict[str, Any]]:
    """
    Get all events (goals, cards, substitutions, etc.) for a given fixture.

    :param fixture_id: The ID of the fixture.
    :return: List of events that occurred during the match.
    """
    client = get_client()
    response = await client.get("/fixtures/events", params={"fixture": fixture_id})
    return response.json().get("response", [])


async def get_events_by_fixture_and_player(
    fixture_id: int,
    player_id: int,
) -> list[dict[str, Any]]:
    """
    Get events related to a specific player in a given fixture.

    :param fixture_id: The ID of the fixture.
    :param player_id: The ID of the player.
    :return: List of events involving the given player.
    """
    client = get_client()
    response = await client.get(
        "/fixtures/events",
        params={"fixture": fixture_id, "player": player_id},
    )
    return response.json().get("response", [])


async def get_events_by_fixture_and_team(
    fixture_id: int,
    team_id: int,
) -> list[dict[str, Any]]:
    """
    Get events associated with a specific team in a given fixture.

    :param fixture_id: The ID of the fixture.
    :param team_id: The ID of the team.
    :return: List of events related to the team in the match.
    """
    client = get_client()
    response = await client.get(
        "/fixtures/events",
        params={"fixture": fixture_id, "team": team_id},
    )
    return response.json().get("response", [])
