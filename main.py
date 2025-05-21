import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from weather import WeatherAPI
from mood_match import is_mood_matched
from music import MusicAPI

app = FastAPI()


class MoodCityInput(BaseModel):
    mood: str
    city: str


@app.post("/recommendation")
def recommend_song(data: MoodCityInput):
    try:

        # Fetch the current weather condition based on the city
        weather_api = WeatherAPI()
        current_weather = weather_api.get_current_weather_condition(data.city)

        # Check if the weather matches the mood
        mood_matched = is_mood_matched(data.mood, current_weather)

        # Fetch a recommended song based on the mood
        music_api = MusicAPI()
        track = music_api.get_top_tracks_by_tag(data.mood)

        return {
            "weather": current_weather,
            "mood_weather_match": mood_matched,
            "recommended_song": track,
        }

    except requests.exceptions.HTTPError as http_err:
        print("here coming nezkuko////", http_err)
        if http_err.response.status_code == 429:
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded. Please try again after some time.",
            )
        raise HTTPException(status_code=502, detail="External service error.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/getmoods")
def mood_list():
    # this mood list is just for reference
    # its not enforced in any other functions
    return {
        "moods": [
            "happy",
            "sad",
            "calm",
            "energetic",
        ]
    }
