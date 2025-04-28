import httpx
import pytest
from api_football_sdk.client import get_client


@pytest.mark.asyncio
async def test_client_successful_get(mock_respx):
    route = mock_respx.get("/timezone").mock(
        return_value=httpx.Response(200, json={"response": "ok"})
    )

    client = get_client()
    response = await client.get("/timezone")

    assert response.status_code == 200
    assert response.json()["response"] == "ok"
    assert route.called


@pytest.mark.asyncio
async def test_client_raises_on_5xx(mock_respx):
    mock_respx.get("/fixtures").mock(return_value=httpx.Response(500))

    client = get_client()

    with pytest.raises(Exception):
        await client.get("/fixtures")
