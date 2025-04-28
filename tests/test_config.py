from api_football_sdk.config import settings


def test_settings_loaded():
    assert isinstance(settings.api_key, str)
    assert settings.api_host == "api-football-v1.p.rapidapi.com"
    assert settings.api_base_url.host == "api-football-v1.p.rapidapi.com"
    assert settings.user_agent.startswith("api-football-sdk")
