from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_recommendation():
    response = client.post("/recommendation", json={"mood": "happy", "city": "Mumbai"})
    assert response.status_code == 200
    assert "weather" in response.json()
