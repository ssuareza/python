from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"detail": "ok"}


def test_auth():
    response = client.get("/auth", headers={"Authorization": "Bearer apikey"})
    assert response.status_code == 200
    assert response.json() == {"detail": "Authenticated"}


def test_auth_no_credentials():
    response = client.get("/auth")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}
