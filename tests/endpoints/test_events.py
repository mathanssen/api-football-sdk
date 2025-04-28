import httpx
import pytest
from api_football_sdk.endpoints.events import get_events_by_fixture


@pytest.mark.asyncio
async def test_get_events_by_fixture(mock_respx):
    fixture_id = 98765
    mock_respx.get("/fixtures/events").mock(
        return_value=httpx.Response(
            200, json={"response": [{"fixture": {"id": fixture_id}}]}
        )
    )

    events = await get_events_by_fixture(fixture_id)
    assert isinstance(events, list)
    assert events[0]["fixture"]["id"] == fixture_id
