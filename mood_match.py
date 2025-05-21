mood_weather_map = {
    "happy": [
        "Clear",
        "Clouds",
    ],
    "sad": [
        "Rain",
        "Drizzle",
        "Thunderstorm",
    ],
    "calm": ["Fog", "Mist"],
    "energetic": ["Clear", "Wind"],
}


def is_mood_matched(mood: str, weather: str) -> bool:
    if not mood:
        raise ValueError("Mood must be provided.")

    return weather in mood_weather_map.get(mood.lower(), [])
