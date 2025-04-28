"""
Endpoints for retrieving top players statistics in a league and season.

This module wraps the `/players/topscorers`, `/players/topassists`,
`/players/topredcards`, and `/players/topyellowcards` endpoints of the API Football.

Usage example:
--------------
    from api_football_sdk.endpoints.top_scorers import get_top_scorers

    top_scorers = await get_top_scorers(league_id=39, season=2020)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client

__all__: list[str] = [
    "get_top_scorers",
    "get_top_assists",
    "get_top_red_cards",
    "get_top_yellow_cards",
]


async def get_top_scorers(league_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get the top scorers in a specific league and season.

    :param league_id: ID of the league.
    :param season: Year of the season.
    :return: List of top scorers with goals count and player metadata.
    """
    client = get_client()
    response = await client.get(
        "/players/topscorers",
        params={"league": league_id, "season": season},
    )
    return response.json().get("response", [])


async def get_top_assists(league_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get the players with most assists in a specific league and season.

    :param league_id: ID of the league.
    :param season: Year of the season.
    :return: List of players with highest number of assists.
    """
    client = get_client()
    response = await client.get(
        "/players/topassists",
        params={"league": league_id, "season": season},
    )
    return response.json().get("response", [])


async def get_top_red_cards(league_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get the players with the most red cards in a league and season.

    :param league_id: ID of the league.
    :param season: Year of the season.
    :return: List of players with most red cards.
    """
    client = get_client()
    response = await client.get(
        "/players/topredcards",
        params={"league": league_id, "season": season},
    )
    return response.json().get("response", [])


async def get_top_yellow_cards(league_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get the players with the most yellow cards in a league and season.

    :param league_id: ID of the league.
    :param season: Year of the season.
    :return: List of players with most yellow cards.
    """
    client = get_client()
    response = await client.get(
        "/players/topyellowcards",
        params={"league": league_id, "season": season},
    )
    return response.json().get("response", [])
