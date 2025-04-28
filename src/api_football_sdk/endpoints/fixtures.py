"""
Endpoints for retrieving and filtering match fixtures.

This module wraps the `/fixtures`, `/fixtures/headtohead`, and `/fixtures/rounds`
endpoints of the API Football.

Usage example:
--------------
    from api_football.endpoints.fixtures import get_fixtures_by_league

    fixtures = await get_fixtures_by_league(league_id=39, season=2020)
"""

from __future__ import annotations

from typing import Any

from api_football_sdk.client import get_client


async def get_fixture_by_id(fixture_id: int) -> dict[str, Any]:
    client = get_client()
    response = await client.get("/fixtures", params={"id": fixture_id})
    return response.json()["response"][0]


async def get_fixtures_by_ids(ids: list[int]) -> list[dict[str, Any]]:
    fixture_ids = "-".join(str(i) for i in ids)
    client = get_client()
    response = await client.get("/fixtures", params={"ids": fixture_ids})
    return response.json()["response"]


async def get_fixtures_by_date(date: str) -> list[dict[str, Any]]:
    client = get_client()
    response = await client.get("/fixtures", params={"date": date})
    return response.json()["response"]


async def get_fixtures_by_status(status: str) -> list[dict[str, Any]]:
    client = get_client()
    response = await client.get("/fixtures", params={"status": status})
    return response.json()["response"]


async def get_fixtures_in_progress() -> list[dict[str, Any]]:
    client = get_client()
    response = await client.get("/fixtures", params={"live": "all"})
    return response.json()["response"]


async def get_last_fixtures(count: int) -> list[dict[str, Any]]:
    client = get_client()
    response = await client.get("/fixtures", params={"last": count})
    return response.json()["response"]


async def get_next_fixtures(count: int) -> list[dict[str, Any]]:
    client = get_client()
    response = await client.get("/fixtures", params={"next": count})
    return response.json()["response"]


async def get_fixtures_by_league(league_id: int, season: int) -> list[dict[str, Any]]:
    client = get_client()
    response = await client.get(
        "/fixtures", params={"league": league_id, "season": season}
    )
    return response.json()["response"]


async def get_fixtures_by_team(team_id: int, season: int) -> list[dict[str, Any]]:
    client = get_client()
    response = await client.get(
        "/fixtures", params={"team": team_id, "season": season}
    )
    return response.json()["response"]


async def get_fixtures_by_dates(
    league_id: int, season: int, from_date: str, to_date: str
) -> list[dict[str, Any]]:
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
    return response.json()["response"]


async def get_fixtures_by_round(
    league_id: int, season: int, round_name: str
) -> list[dict[str, Any]]:
    client = get_client()
    response = await client.get(
        "/fixtures",
        params={
            "league": league_id,
            "season": season,
            "round": round_name,
        },
    )
    return response.json()["response"]


async def get_fixtures_rounds(league_id: int, season: int) -> list[str]:
    client = get_client()
    response = await client.get(
        "/fixtures/rounds", params={"league": league_id, "season": season}
    )
    return response.json()["response"]


async def get_fixtures_rounds_with_dates(league_id: int, season: int) -> list[str]:
    client = get_client()
    response = await client.get(
        "/fixtures/rounds",
        params={"league": league_id, "season": season, "dates": "true"},
    )
    return response.json()["response"]


async def get_fixtures_head_to_head(team1_id: int, team2_id: int) -> list[dict[str, Any]]:
    h2h = f"{team1_id}-{team2_id}"
    client = get_client()
    response = await client.get("/fixtures/headtohead", params={"h2h": h2h})
    return response.json()["response"]
