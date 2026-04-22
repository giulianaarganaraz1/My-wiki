from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_note():
    response = client.post("/notes", json={
        "title": "Test",
        "content": "Hola"
    })

    assert response.status_code == 200