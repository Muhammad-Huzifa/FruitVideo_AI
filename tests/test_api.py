"""API tests for FruitVideo AI."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_service_information() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["name"] == "FruitVideo AI API"
    assert response.json()["documentation"] == "/docs"


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_generate_returns_demo_video() -> None:
    prompt = "A bright orange rotating on a clean white background"
    response = client.post("/generate", json={"prompt": prompt})

    assert response.status_code == 200
    assert response.json()["prompt"] == prompt
    assert response.json()["status"] == "success"
    assert response.json()["demo"] is True
    assert response.json()["video_url"].startswith("https://")


def test_generate_rejects_an_empty_prompt() -> None:
    response = client.post("/generate", json={"prompt": "   "})

    assert response.status_code == 422
