"""
Endpoints for retrieving trophies won by players or coaches.

This module provides typed access to the `/trophies` endpoint
of the API Football.

Usage example:
--------------
    from api_football_sdk.endpoints.trophies import get_trophies_by_player

    trophies = await get_trophies_by_player(player_id=276)
    print(trophies)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client

__all__: list[str] = [
    "get_trophies_by_player",
    "get_trophies_by_coach",
    "get_trophies_by_players",
    "get_trophies_by_coaches",
]


async def get_trophies_by_player(player_id: int) -> list[dict[str, Any]]:
    """
    Get all trophies won by a specific player.

    :param player_id: The ID of the player.
    :return: List of trophies the player has won.
    """
    client = get_client()
    response = await client.get("/trophies", params={"player": player_id})
    return response.json().get("response", [])


async def get_trophies_by_coach(coach_id: int) -> list[dict[str, Any]]:
    """
    Get all trophies won by a specific coach.

    :param coach_id: The ID of the coach.
    :return: List of trophies the coach has won.
    """
    client = get_client()
    response = await client.get("/trophies", params={"coach": coach_id})
    return response.json().get("response", [])


async def get_trophies_by_players(player_ids: list[int]) -> list[dict[str, Any]]:
    """
    Get all trophies won by multiple players at once.

    :param player_ids: A list of player IDs.
    :return: Trophies won by the specified players.
    """
    ids = "-".join(str(player_id) for player_id in player_ids)
    client = get_client()
    response = await client.get("/trophies", params={"players": ids})
    return response.json().get("response", [])


async def get_trophies_by_coaches(coach_ids: list[int]) -> list[dict[str, Any]]:
    """
    Get all trophies won by multiple coaches at once.

    :param coach_ids: A list of coach IDs.
    :return: Trophies won by the specified coaches.
    """
    ids = "-".join(str(coach_id) for coach_id in coach_ids)
    client = get_client()
    response = await client.get("/trophies", params={"coachs": ids})
    return response.json().get("response", [])
