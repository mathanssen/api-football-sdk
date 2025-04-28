import httpx
import pytest
from api_football_sdk.endpoints.standings import get_standings_by_league


@pytest.mark.asyncio
async def test_get_standings_by_league(mock_respx):
    league_id = 10
    season = 2024
    mock_respx.get("/standings").mock(
        return_value=httpx.Response(
            200, json={"response": [{"league": {"id": league_id}}]}
        )
    )

    standings = await get_standings_by_league(league_id, season)
    assert isinstance(standings, list)
    assert standings[0]["league"]["id"] == league_id
