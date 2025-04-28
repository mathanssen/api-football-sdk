import httpx
import pytest
from api_football_sdk.endpoints.top_scorers import get_top_scorers


@pytest.mark.asyncio
async def test_get_top_scorers(mock_respx):
    league_id = 1
    season = 2024
    mock_respx.get("/players/topscorers").mock(
        return_value=httpx.Response(200, json={"response": [{"goals": {"total": 20}}]})
    )

    top_scorers = await get_top_scorers(league_id, season)
    assert isinstance(top_scorers, list)
    assert "goals" in top_scorers[0]
