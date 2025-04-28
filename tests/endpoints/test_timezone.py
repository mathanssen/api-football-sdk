import httpx
import pytest
from api_football_sdk.endpoints.timezone import get_timezones


@pytest.mark.asyncio
async def test_get_timezones(mock_respx):
    mock_respx.get("/timezone").mock(
        return_value=httpx.Response(
            200, json={"response": ["Europe/London", "America/Sao_Paulo"]}
        )
    )

    timezones = await get_timezones()
    assert "Europe/London" in timezones
