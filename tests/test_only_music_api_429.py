import requests
from fastapi.testclient import TestClient
from unittest.mock import patch, Mock
from main import app

client = TestClient(app)


@patch("utils.outbound_request.requests.request")
def test_only_music_api_fails(mock_request):
    # First call: weather API - return success
    mock_weather_resp = Mock()
    mock_weather_resp.status_code = 200
    mock_weather_resp.json.return_value = {"weather": [{"main": "Clear"}]}

    # Second call: music API - fail with 429
    mock_music_error = Mock()
    mock_music_error.status_code = 429
    mock_music_error.json.return_value = {"message": "Rate limit exceeded"}
    mock_music_error.raise_for_status.side_effect = requests.exceptions.HTTPError(
        response=mock_music_error
    )

    def side_effect(*args, **kwargs):
        if "weather" in args[1]:
            return mock_weather_resp
        else:
            return mock_music_error

    mock_request.side_effect = side_effect

    response = client.post("/recommendation", json={"mood": "happy", "city": "Mumbai"})
    assert response.status_code == 429
    assert "Rate limit exceeded" in response.json()["detail"]
