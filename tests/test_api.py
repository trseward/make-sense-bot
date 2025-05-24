import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_submit_prompt():
    response = client.post("/submit-prompt", json={"age_group": "Middle School [12-14]", "prompt": "What is photosynthesis?"})
    assert response.status_code == 200
    assert "summary" in response.json()

def test_get_summary():
    response = client.get("/get-summary")
    assert response.status_code == 200
    assert "summary" in response.json()
