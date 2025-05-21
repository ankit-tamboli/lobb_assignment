# import requests
# import random

# API_KEY = "9382cc87fbff4c6760b84ce5fb5c1360"


# def get_song_by_mood(mood: str):
#     if not mood:
#         raise ValueError("Mood must be provided.")

#     tag = f"{mood}"

#     url = f"http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag={tag}&api_key={API_KEY}&format=json"
#     response = requests.get(url)
#     response.raise_for_status()
#     data = response.json()

#     tracks = data.get("tracks", {}).get("track", [])

#     if not tracks:
#         raise Exception(f"No tracks found for mood '{mood}' with Indian tag.")

#     # this will randomly choose a track from the tracks list
#     random_track = random.choice(tracks)
#     return {"title": random_track["name"], "artist": random_track["artist"]["name"]}


from utils.outbound_request import make_outbound_request
from utils.config import LASTFM_API_KEY
import random


class MusicAPI:
    def __init__(self, base_url="http://ws.audioscrobbler.com/2.0/", format="json"):
        self.api_key = LASTFM_API_KEY
        self.base_url = base_url
        self.format = format

    def get_top_tracks_by_tag(self, mood, user_context=None):
        tag = f"{mood}"
        url = f"{self.base_url}"

        params = {
            "method": "tag.gettoptracks",
            "tag": tag,
            "api_key": self.api_key,
            "format": self.format,
        }
        response = make_outbound_request(
            "GET", url, params=params, user_context=user_context
        )
        data = response.json()

        if "tracks" not in data or not data["tracks"]["track"]:
            raise Exception("No tracks found.")

        tracks = data.get("tracks", {}).get("track", [])

        # this will randomly choose a track from the tracks list
        random_track = random.choice(tracks)
        return {"title": random_track["name"], "artist": random_track["artist"]["name"]}
