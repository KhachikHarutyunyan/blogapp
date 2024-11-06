import pytest

from fastapi.testclient import TestClient


from main import app

@pytest.fixture(scope="function")
def test_client():
    with TestClient(app=app) as client:
        yield client

def test_greating(test_client: TestClient):
    response = test_client.get("/")
    
    assert response.status_code == 200