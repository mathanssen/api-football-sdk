import pytest
from api_football_sdk.exceptions import (
    APIFootballError,
    APIFootballHTTPError,
    APIFootballRequestError,
    ConfigurationError,
)


def test_api_football_error_inheritance():
    assert issubclass(APIFootballRequestError, APIFootballError)
    assert issubclass(APIFootballHTTPError, APIFootballError)


def test_configuration_error():
    with pytest.raises(ConfigurationError):
        raise ConfigurationError("Missing API key")
