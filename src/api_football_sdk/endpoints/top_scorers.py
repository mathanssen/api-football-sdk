"""
Endpoints for retrieving top players statistics in a league and season.

This module wraps the `/players/topscorers`, `/players/topassists`,
`/players/topredcards`, and `/players/topyellowcards` endpoints of the API Football.

Usage example:
--------------
    from api_football.endpoints.top_scorers import get_top_scorers

    top_scorers = await get_top_scorers(league_id=39, season=2020)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client


async def get_top_scorers(league_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get the top scorers in a specific league and season.

    Parameters
    ----------
    league_id : int
        ID of the league.
    season : int
        Year of the season.

    Returns
    -------
    list of dict
        List of top scorers with goals count and player metadata.
    """
    client = get_client()
    response = await client.get(
        "/players/topscorers", params={"league": league_id, "season": season}
    )
    return response.json()["response"]


async def get_top_assists(league_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get the players with most assists in a specific league and season.

    Parameters
    ----------
    league_id : int
        ID of the league.
    season : int
        Year of the season.

    Returns
    -------
    list of dict
        List of players with highest number of assists.
    """
    client = get_client()
    response = await client.get(
        "/players/topassists", params={"league": league_id, "season": season}
    )
    return response.json()["response"]


async def get_top_red_cards(league_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get the players with the most red cards in a league and season.

    Parameters
    ----------
    league_id : int
        ID of the league.
    season : int
        Year of the season.

    Returns
    -------
    list of dict
        List of players with most red cards.
    """
    client = get_client()
    response = await client.get(
        "/players/topredcards", params={"league": league_id, "season": season}
    )
    return response.json()["response"]


async def get_top_yellow_cards(league_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get the players with the most yellow cards in a league and season.

    Parameters
    ----------
    league_id : int
        ID of the league.
    season : int
        Year of the season.

    Returns
    -------
    list of dict
        List of players with most yellow cards.
    """
    client = get_client()
    response = await client.get(
        "/players/topyellowcards", params={"league": league_id, "season": season}
    )
    return response.json()["response"]
