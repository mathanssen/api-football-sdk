import httpx
import pytest
from api_football_sdk.endpoints.fixtures import get_fixture_by_id


@pytest.mark.asyncio
async def test_get_fixture_by_id(mock_respx):
    fixture_id = 12345
    mock_respx.get("/fixtures").mock(
        return_value=httpx.Response(
            200, json={"response": [{"fixture": {"id": fixture_id}}]}
        )
    )

    result = await get_fixture_by_id(fixture_id)
    assert result["fixture"]["id"] == fixture_id
