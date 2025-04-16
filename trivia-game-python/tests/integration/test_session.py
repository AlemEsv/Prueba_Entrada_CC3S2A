from fastapi.testclient import TestClient
from app.session import app

client = TestClient(app)

def test_get_questions():
    response = client.get("/questions/")
    assert response.status_code == 200
    assert isinstance(response.json(),list)