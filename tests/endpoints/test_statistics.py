import httpx
import pytest
from api_football_sdk.endpoints.statistics import get_statistics_by_fixture


@pytest.mark.asyncio
async def test_get_statistics_by_fixture(mock_respx):
    fixture_id = 11111
    mock_respx.get("/fixtures/statistics").mock(
        return_value=httpx.Response(200, json={"response": [{"team": {"id": 1}}]})
    )

    stats = await get_statistics_by_fixture(fixture_id)
    assert isinstance(stats, list)
    assert stats[0]["team"]["id"] == 1
