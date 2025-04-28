import httpx
import pytest
from api_football_sdk.endpoints.players import get_player_by_id


@pytest.mark.asyncio
async def test_get_player_by_id(mock_respx):
    player_id = 7
    season = 2024
    mock_respx.get("/players").mock(
        return_value=httpx.Response(
            200, json={"response": [{"player": {"id": player_id}}]}
        )
    )

    player = await get_player_by_id(player_id, season)
    assert player["player"]["id"] == player_id
