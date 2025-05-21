import pytest
from weather import WeatherAPI


def test_get_current_weather_condition(weather_api):
    # Test with a valid city
    city = "Mumbai"
    weather_condition = weather_api.get_current_weather_condition(city)
    assert weather_condition is not None
    assert isinstance(weather_condition, str)
    assert weather_condition in [
        "Clear",
        "Clouds",
        "Rain",
        "Drizzle",
        "Thunderstorm",
        "Fog",
        "Mist",
        "Wind",
    ]  # Expected weather conditions

    # Test with an invalid city
    with pytest.raises(Exception):  # expecting an execption for invalid city
        weather_api.get_current_weather_condition("InvalidCity")


@pytest.fixture
def weather_api():
    return WeatherAPI()
