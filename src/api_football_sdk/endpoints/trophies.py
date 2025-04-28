"""
Endpoints for retrieving trophies won by players or coaches.

This module provides typed access to the `/trophies` endpoint
of the API Football.

Usage example:
--------------
    from api_football.endpoints.trophies import get_trophies_by_player

    trophies = await get_trophies_by_player(player_id=276)
    print(trophies)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client


async def get_trophies_by_player(player_id: int) -> list[dict[str, Any]]:
    """
    Get all trophies won by a specific player.

    Parameters
    ----------
    player_id : int
        The ID of the player.

    Returns
    -------
    list of dict
        List of trophies the player has won.
    """
    client = get_client()
    response = await client.get("/trophies", params={"player": player_id})
    return response.json()["response"]


async def get_trophies_by_coach(coach_id: int) -> list[dict[str, Any]]:
    """
    Get all trophies won by a specific coach.

    Parameters
    ----------
    coach_id : int
        The ID of the coach.

    Returns
    -------
    list of dict
        List of trophies the coach has won.
    """
    client = get_client()
    response = await client.get("/trophies", params={"coach": coach_id})
    return response.json()["response"]


async def get_trophies_by_players(player_ids: list[int]) -> list[dict[str, Any]]:
    """
    Get all trophies won by multiple players at once.

    Parameters
    ----------
    player_ids : list of int
        A list of player IDs.

    Returns
    -------
    list of dict
        Trophies won by the specified players.
    """
    ids = "-".join(str(pid) for pid in player_ids)
    client = get_client()
    response = await client.get("/trophies", params={"players": ids})
    return response.json()["response"]


async def get_trophies_by_coaches(coach_ids: list[int]) -> list[dict[str, Any]]:
    """
    Get all trophies won by multiple coaches at once.

    Parameters
    ----------
    coach_ids : list of int
        A list of coach IDs.

    Returns
    -------
    list of dict
        Trophies won by the specified coaches.
    """
    ids = "-".join(str(cid) for cid in coach_ids)
    client = get_client()
    response = await client.get("/trophies", params={"coachs": ids})
    return response.json()["response"]
