"""
Endpoints for retrieving player data, statistics, and squad information.

This module wraps the `/players`, `/players/seasons`, `/fixtures/players`,
`/players/squads`, `/players/profiles`, and `/players/teams`
endpoints of the API Football.

Usage example:
--------------
    from api_football.endpoints.players import get_players_by_team

    players = await get_players_by_team(team_id=33, season=2020)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client


async def get_player_by_id(player_id: int, season: int) -> dict[str, Any]:
    """
    Get detailed information and stats for a specific player by ID and season.

    Parameters
    ----------
    player_id : int
        Player ID.
    season : int
        Season year.

    Returns
    -------
    dict
        Player metadata and statistics.
    """
    client = get_client()
    response = await client.get("/players", params={"id": player_id, "season": season})
    return response.json()["response"][0]


async def get_players_by_team(team_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get all players of a team for a given season.

    Parameters
    ----------
    team_id : int
        Team ID.
    season : int
        Season year.

    Returns
    -------
    list of dict
        List of players with metadata and statistics.
    """
    client = get_client()
    response = await client.get(
        "/players", params={"team": team_id, "season": season}
    )
    return response.json()["response"]


async def get_players_by_league(league_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get all players that played in a given league during a season.

    Parameters
    ----------
    league_id : int
        League ID.
    season : int
        Season year.

    Returns
    -------
    list of dict
        List of players with metadata and statistics.
    """
    client = get_client()
    response = await client.get(
        "/players", params={"league": league_id, "season": season}
    )
    return response.json()["response"]


async def get_players_in_fixture(fixture_id: int) -> list[dict[str, Any]]:
    """
    Get all players that participated in a specific fixture.

    Parameters
    ----------
    fixture_id : int
        Fixture ID.

    Returns
    -------
    list of dict
        List of players and their roles in the match.
    """
    client = get_client()
    response = await client.get("/fixtures/players", params={"fixture": fixture_id})
    return response.json()["response"]


async def get_players_seasons() -> list[int]:
    """
    Get a list of all seasons available for players' statistics.

    Returns
    -------
    list of int
        Season years.
    """
    client = get_client()
    response = await client.get("/players/seasons")
    return response.json()["response"]


async def get_seasons_by_player(player_id: int) -> list[int]:
    """
    Get all seasons in which a specific player has participated.

    Parameters
    ----------
    player_id : int
        Player ID.

    Returns
    -------
    list of int
        List of seasons played by the player.
    """
    client = get_client()
    response = await client.get("/players/seasons", params={"player": player_id})
    return response.json()["response"]


async def get_player_teams(player_id: int) -> list[dict[str, Any]]:
    """
    Get all teams a specific player has played for.

    Parameters
    ----------
    player_id : int
        Player ID.

    Returns
    -------
    list of dict
        List of teams the player has been associated with.
    """
    client = get_client()
    response = await client.get("/players/teams", params={"player": player_id})
    return response.json()["response"]


async def get_team_squad(team_id: int) -> list[dict[str, Any]]:
    """
    Get the full squad list of a given team.

    Parameters
    ----------
    team_id : int
        Team ID.

    Returns
    -------
    list of dict
        Squad members with their metadata.
    """
    client = get_client()
    response = await client.get("/players/squads", params={"team": team_id})
    return response.json()["response"]


async def get_players_profiles() -> list[dict[str, Any]]:
    """
    Get all player profiles available in the database.

    Returns
    -------
    list of dict
        List of players with static profile information.
    """
    client = get_client()
    response = await client.get("/players/profiles")
    return response.json()["response"]
