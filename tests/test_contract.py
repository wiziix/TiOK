import requests
import json
import pytest
from src.app import create_app
from main import app, getUsernames, getThumbnails


@pytest.fixture(scope="module")
def client():
    #Test client for the Flask application
    with app.test_client() as client:
        yield client


# Test for /albums endpoint
def test_albums_endpoint(client):
    response = client.get("/albums")
    assert response.status_code == 200



# Test for /posts endpoint
def test_posts_endpoint(client):
    response = client.get("/posts")
    assert response.status_code == 200



# Test for /albums/photos/<username> endpoint

def test_photos_endpoint(client):
    # Assuming username exists in the dataset
    username = "Leopoldo_Corkery"
    response = client.get(f"/albums/photos/{username}")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"


# Test for getUsernames function
def test_get_usernames():
    usernames = getUsernames()
    assert isinstance(usernames, dict)
    assert len(usernames) == 10  # Assuming it fetches 10 usernames


# Test for getThumbnails function
def test_get_thumbnails():
    thumbnails = getThumbnails()
    assert isinstance(thumbnails, dict)
    # Assuming it fetches thumbnails for every 50 photos
    assert len(thumbnails) > 0


# Mocking the external API calls
def test_external_api_calls(monkeypatch):
    def mock_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, content):
                self.content = content

            def json(self):
                return json.loads(self.content)

        if args[0].endswith("/users"):
            return MockResponse('[{"id": 1, "username": "Leanne Graham"}, {"id": 2, "username": "Ervin Howell"}]')
        elif args[0].endswith("/photos"):
            return MockResponse('[{"albumId": 1, "thumbnailUrl": "https://example.com/thumbnail1.jpg"}, {"albumId": 2, "thumbnailUrl": "https://example.com/thumbnail2.jpg"}]')

    monkeypatch.setattr(requests, "get", mock_requests_get)
