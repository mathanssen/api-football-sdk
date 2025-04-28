"""
Endpoints for retrieving player data, statistics, and squad information.

This module wraps the `/players`, `/players/seasons`, `/fixtures/players`,
`/players/squads`, `/players/profiles`, and `/players/teams`
endpoints of the API Football.

Usage example:
--------------
    from api_football_sdk.endpoints.players import get_players_by_team

    players = await get_players_by_team(team_id=33, season=2020)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client

__all__: list[str] = [
    "get_player_by_id",
    "get_players_by_team",
    "get_players_by_league",
    "get_players_in_fixture",
    "get_players_seasons",
    "get_seasons_by_player",
    "get_player_teams",
    "get_team_squad",
    "get_players_profiles",
]


async def get_player_by_id(player_id: int, season: int) -> dict[str, Any]:
    """
    Get detailed information and stats for a specific player by ID and season.

    :param player_id: Player ID.
    :param season: Season year.
    :return: Player metadata and statistics.
    """
    client = get_client()
    response = await client.get("/players", params={"id": player_id, "season": season})
    results = response.json().get("response", [])
    return results[0] if results else {}


async def get_players_by_team(team_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get all players of a team for a given season.

    :param team_id: Team ID.
    :param season: Season year.
    :return: List of players with metadata and statistics.
    """
    client = get_client()
    response = await client.get("/players", params={"team": team_id, "season": season})
    return response.json().get("response", [])


async def get_players_by_league(league_id: int, season: int) -> list[dict[str, Any]]:
    """
    Get all players that played in a given league during a season.

    :param league_id: League ID.
    :param season: Season year.
    :return: List of players with metadata and statistics.
    """
    client = get_client()
    response = await client.get(
        "/players",
        params={"league": league_id, "season": season},
    )
    return response.json().get("response", [])


async def get_players_in_fixture(fixture_id: int) -> list[dict[str, Any]]:
    """
    Get all players that participated in a specific fixture.

    :param fixture_id: Fixture ID.
    :return: List of players and their roles in the match.
    """
    client = get_client()
    response = await client.get("/fixtures/players", params={"fixture": fixture_id})
    return response.json().get("response", [])


async def get_players_seasons() -> list[int]:
    """
    Get a list of all seasons available for players' statistics.

    :return: List of season years.
    """
    client = get_client()
    response = await client.get("/players/seasons")
    return response.json().get("response", [])


async def get_seasons_by_player(player_id: int) -> list[int]:
    """
    Get all seasons in which a specific player has participated.

    :param player_id: Player ID.
    :return: List of seasons played by the player.
    """
    client = get_client()
    response = await client.get("/players/seasons", params={"player": player_id})
    return response.json().get("response", [])


async def get_player_teams(player_id: int) -> list[dict[str, Any]]:
    """
    Get all teams a specific player has played for.

    :param player_id: Player ID.
    :return: List of teams the player has been associated with.
    """
    client = get_client()
    response = await client.get("/players/teams", params={"player": player_id})
    return response.json().get("response", [])


async def get_team_squad(team_id: int) -> list[dict[str, Any]]:
    """
    Get the full squad list of a given team.

    :param team_id: Team ID.
    :return: Squad members with their metadata.
    """
    client = get_client()
    response = await client.get("/players/squads", params={"team": team_id})
    return response.json().get("response", [])


async def get_players_profiles() -> list[dict[str, Any]]:
    """
    Get all player profiles available in the database.

    :return: List of players with static profile information.
    """
    client = get_client()
    response = await client.get("/players/profiles")
    return response.json().get("response", [])
