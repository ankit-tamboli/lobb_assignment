import pytest
from mood_match import is_mood_matched


# mood_weather_map = {
#     "happy": [
#         "Clear",
#         "Clouds",
#     ],
#     "sad": [
#         "Rain",
#         "Drizzle",
#         "Thunderstorm",
#     ],
#     "calm": ["Fog", "Mist"],
#     "energetic": ["Clear", "Wind"],
# }

# testing for each mood according to the mood_weather_map 
def test_mood_weather_match_happy():
    assert is_mood_matched("happy", "Clear") is True
    assert is_mood_matched("happy", "Clouds") is True
    assert is_mood_matched("happy", "Rain") is False

def test_mood_weather_match_sad():
    assert is_mood_matched("sad", "Rain") is True
    assert is_mood_matched("sad", "Thunderstorm") is True
    assert is_mood_matched("sad", "Clear") is False

def test_mood_weather_match_calm():
    assert is_mood_matched("calm", "Fog") is True
    assert is_mood_matched("calm", "Mist") is True
    assert is_mood_matched("calm", "Clouds") is False

def test_mood_weather_match_energetic():
    assert is_mood_matched("energetic", "Wind") is True
    assert is_mood_matched("energetic", "Clear") is True
    assert is_mood_matched("energetic", "Rain") is False

def test_mood_weather_match_case_insensitivity():
    assert is_mood_matched("Happy", "Clear") is True  # Should handle capitalized mood

def test_mood_weather_invalid_mood():
    assert is_mood_matched("bored", "Clear") is False  # Not in mood map

def test_mood_weather_empty_mood():
    with pytest.raises(ValueError):
        is_mood_matched("", "Clear")
