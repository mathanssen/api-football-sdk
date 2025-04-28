"""
Endpoints for retrieving and filtering match fixtures.

This module wraps the `/fixtures`, `/fixtures/headtohead`, and `/fixtures/rounds`
endpoints of the API Football.

Usage example:
--------------
    from api_football_sdk.endpoints.fixtures import get_fixtures_by_league

    fixtures = await get_fixtures_by_league(league_id=39, season=2020)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client

__all__: list[str] = [
    "get_fixture_by_id",
    "get_fixtures_by_ids",
    "get_fixtures_by_date",
    "get_fixtures_by_status",
    "get_fixtures_in_progress",
    "get_last_fixtures",
    "get_next_fixtures",
    "get_fixtures_by_league",
    "get_fixtures_by_team",
    "get_fixtures_by_dates",
    "get_fixtures_by_round",
    "get_fixtures_rounds",
    "get_fixtures_rounds_with_dates",
    "get_fixtures_head_to_head",
]


async def get_fixture_by_id(fixture_id: int) -> dict[str, Any]:
    """
    Retrieve a fixture by its ID.

    :param fixture_id: The ID of the fixture.
    :return: Metadata about the fixture.
    """
    client = get_client()
    response = await client.get("/fixtures", params={"id": fixture_id})
    results = response.json().get("response", [])
    return results[0] if results else {}


async def get_fixtures_by_ids(ids: list[int]) -> list[dict[str, Any]]:
    """
    Retrieve multiple fixtures by their IDs.

    :param ids: List of fixture IDs.
    :return: List of fixture metadata.
    """
    fixture_ids = "-".join(str(fixture_id) for fixture_id in ids)
    client = get_client()
    response = await client.get("/fixtures", params={"ids": fixture_ids})
    return response.json().get("response", [])


async def get_fixtures_by_date(date: str) -> list[dict[str, Any]]:
    """
    Retrieve fixtures by a specific date.

    :param date: Date in YYYY-MM-DD format.
    :return: List of fixtures on that date.
    """
    client = get_client()
    response = await client.get("/fixtures", params={"date": date})
    return response.json().get("response", [])


async def get_fixtures_by_status(status: str) -> list[dict[str, Any]]:
    """
    Retrieve fixtures by their status.

    :param status: Status of the fixture (e.g., "NS", "FT").
    :return: List of fixtures matching the status.
    """
    client = get_client()
    response = await client.get("/fixtures", params={"status": status})
    return response.json().get("response", [])


async def get_fixtures_in_progress() -> list[dict[str, Any]]:
    """
    Retrieve fixtures that are currently live.

    :return: List of live fixtures.
    """
    client = get_client()
    response = await client.get("/fixtures", params={"live": "all"})
    return response.json().get("response", [])


async def get_last_fixtures(count: int) -> list[dict[str, Any]]:
    """
    Retrieve the last played fixtures.

    :param count: Number of fixtures to retrieve.
    :return: List of recent fixtures.
    """
    client = get_client()
    response = await client.get("/fixtures", params={"last": count})
    return response.json().get("response", [])


async def get_next_fixtures(count: int) -> list[dict[str, Any]]:
    """
    Retrieve the next upcoming fixtures.

    :param count: Number of fixtures to retrieve.
    :return: List of upcoming fixtures.
    """
    client = get_client()
    response = await client.get("/fixtures", params={"next": count})
    return response.json().get("response", [])


async def get_fixtures_by_league(league_id: int, season: int) -> list[dict[str, Any]]:
    """
    Retrieve fixtures by league and season.

    :param league_id: ID of the league.
    :param season: Season year.
    :return: List of fixtures.
    """
    client = get_client()
    response = await client.get(
        "/fixtures", params={"league": league_id, "season": season}
    )
    return response.json().get("response", [])


async def get_fixtures_by_team(team_id: int, season: int) -> list[dict[str, Any]]:
    """
    Retrieve fixtures for a specific team and season.

    :param team_id: ID of the team.
    :param season: Season year.
    :return: List of fixtures.
    """
    client = get_client()
    response = await client.get("/fixtures", params={"team": team_id, "season": season})
    return response.json().get("response", [])


async def get_fixtures_by_dates(
    league_id: int,
    season: int,
    from_date: str,
    to_date: str,
) -> list[dict[str, Any]]:
    """
    Retrieve fixtures within a date range for a league and season.

    :param league_id: ID of the league.
    :param season: Season year.
    :param from_date: Start date (YYYY-MM-DD).
    :param to_date: End date (YYYY-MM-DD).
    :return: List of fixtures in the range.
    """
    client = get_client()
    response = await client.get(
        "/fixtures",
        params={
            "league": league_id,
            "season": season,
            "from": from_date,
            "to": to_date,
        },
    )
    return response.json().get("response", [])


async def get_fixtures_by_round(
    league_id: int,
    season: int,
    round_name: str,
) -> list[dict[str, Any]]:
    """
    Retrieve fixtures for a specific round.

    :param league_id: ID of the league.
    :param season: Season year.
    :param round_name: Name of the round.
    :return: List of fixtures.
    """
    client = get_client()
    response = await client.get(
        "/fixtures",
        params={
            "league": league_id,
            "season": season,
            "round": round_name,
        },
    )
    return response.json().get("response", [])


async def get_fixtures_rounds(league_id: int, season: int) -> list[str]:
    """
    Retrieve all available rounds for a league and season.

    :param league_id: ID of the league.
    :param season: Season year.
    :return: List of rounds.
    """
    client = get_client()
    response = await client.get(
        "/fixtures/rounds", params={"league": league_id, "season": season}
    )
    return response.json().get("response", [])


async def get_fixtures_rounds_with_dates(league_id: int, season: int) -> list[str]:
    """
    Retrieve all available rounds with their dates.

    :param league_id: ID of the league.
    :param season: Season year.
    :return: List of rounds with dates.
    """
    client = get_client()
    response = await client.get(
        "/fixtures/rounds",
        params={"league": league_id, "season": season, "dates": "true"},
    )
    return response.json().get("response", [])


async def get_fixtures_head_to_head(
    team1_id: int, team2_id: int
) -> list[dict[str, Any]]:
    """
    Retrieve head-to-head fixtures between two teams.

    :param team1_id: ID of the first team.
    :param team2_id: ID of the second team.
    :return: List of head-to-head fixtures.
    """
    h2h = f"{team1_id}-{team2_id}"
    client = get_client()
    response = await client.get("/fixtures/headtohead", params={"h2h": h2h})
    return response.json().get("response", [])
