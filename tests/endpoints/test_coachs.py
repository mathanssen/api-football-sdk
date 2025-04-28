import httpx
import pytest
from api_football_sdk.endpoints.coachs import get_coach_by_id


@pytest.mark.asyncio
async def test_get_coach_by_id(mock_respx):
    coach_id = 10
    mock_respx.get("/coachs").mock(
        return_value=httpx.Response(
            200, json={"response": [{"coach": {"id": coach_id}}]}
        )
    )

    coach = await get_coach_by_id(coach_id)
    assert coach["coach"]["id"] == coach_id
