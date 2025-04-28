import pytest
import respx
from api_football_sdk.client import get_client
from httpx import AsyncClient


@pytest.fixture
def api_client() -> AsyncClient:
    """
    Fixture to get a shared API client instance for tests.
    """
    client = get_client()._client
    return client


@pytest.fixture
def mock_respx():
    """
    Fixture to enable respx HTTPX mocking.
    """
    with respx.mock(base_url="https://api-football-v1.p.rapidapi.com/v3") as mock:
        yield mock
