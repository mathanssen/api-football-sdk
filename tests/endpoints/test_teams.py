import httpx
import pytest
from api_football_sdk.endpoints.teams import get_team_by_id


@pytest.mark.asyncio
async def test_get_team_by_id(mock_respx):
    team_id = 50
    mock_respx.get("/teams").mock(
        return_value=httpx.Response(200, json={"response": [{"team": {"id": team_id}}]})
    )

    team = await get_team_by_id(team_id)
    assert team["team"]["id"] == team_id
