from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_read_main():
    response = client.get("/hello/hello")
    assert response.status_code == 200
    assert response.json() == "hello wrld"