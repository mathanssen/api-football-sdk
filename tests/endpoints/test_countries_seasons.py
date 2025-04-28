import httpx
import pytest
from api_football_sdk.endpoints.countries_seasons import get_supported_seasons


@pytest.mark.asyncio
async def test_get_supported_seasons(mock_respx):
    mock_respx.get("/leagues/seasons").mock(
        return_value=httpx.Response(200, json={"response": [2022, 2023, 2024]})
    )

    seasons = await get_supported_seasons()
    assert seasons == [2022, 2023, 2024]
