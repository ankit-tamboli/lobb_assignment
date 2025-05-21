# import requests

# API_KEY = "bd5cc0d4816a519b3ac2237586844ffa"


# def get_weather(city: str) -> str:
#     if not city:
#         raise ValueError("City name must be provided.")

#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
#     response = requests.get(url)
#     print(response.json(), "weather.py")
#     response.raise_for_status()
#     data = response.json()
#     print(data, "weather.py")
#     return data["weather"][0]["main"]


import requests
from utils.outbound_request import make_outbound_request
from utils.config import OPENWEATHER_API_KEY


class WeatherAPI:
    def __init__(
        self,
        api_key=OPENWEATHER_API_KEY,
        base_url="https://api.openweathermap.org/data/2.5",
    ):
        self.api_key = api_key
        self.base_url = base_url

    def get_current_weather_condition(self, city: str, user_context=None) -> str:
        """
        Fetches the current weather condition (like 'Clear', 'Clouds', etc.) for a given city.
        """
        if not city:
            raise ValueError("Invalid City.")

        url = f"{self.base_url}/weather"
        params = {"q": city, "appid": self.api_key}

        response = make_outbound_request(
            "GET", url, params=params, user_context=user_context
        )

        data = response.json()
        if "weather" not in data or not data["weather"]:
            raise Exception(f"No weather data found for city: {city}")

        return data["weather"][0]["main"]
