from music import MusicAPI
import pytest


@pytest.fixture
def music_api():
    return MusicAPI()


def test_get_top_tracks_by_mood(music_api):
    # Test with a valid mood
    mood = "happy"
    track = music_api.get_top_tracks_by_tag(mood)
    assert track is not None
    assert isinstance(track, dict)
    assert "title" in track
    assert "artist" in track
    assert isinstance(track["title"], str)
    assert isinstance(track["artist"], str)

    # Test with an invalid mood
    with pytest.raises(Exception):
        music_api.get_top_tracks_by_tag("invalid_mood")
