import pytest
import httpx
from api_football_sdk.endpoints.lineups import get_lineups_by_fixture

@pytest.mark.asyncio
async def test_get_lineups_by_fixture(mock_respx):
    fixture_id = 22222
    mock_respx.get("/fixtures/lineups").mock(
        return_value=httpx.Response(200, json={"response": [{"team": {"id": 1}}]})
    )

    lineups = await get_lineups_by_fixture(fixture_id)
    assert isinstance(lineups, list)
    assert lineups[0]["team"]["id"] == 1
