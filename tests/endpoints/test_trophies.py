import httpx
import pytest
from api_football_sdk.endpoints.leagues import get_all_leagues


@pytest.mark.asyncio
async def test_get_all_leagues(mock_respx):
    mock_respx.get("/leagues").mock(
        return_value=httpx.Response(200, json={"response": [{"league": {"id": 1}}]})
    )

    leagues = await get_all_leagues()
    assert isinstance(leagues, list)
    assert leagues[0]["league"]["id"] == 1
