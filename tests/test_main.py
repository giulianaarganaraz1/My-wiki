from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_greet():
    response = client.get("/hi")
    
    assert response.status_code == 200
    assert response.json() == "Hello? World?"