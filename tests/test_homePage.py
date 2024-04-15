from src.app import create_app
from main import app

def test_home_page():
    flask_app = app
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"API JSON" in response.data
        assert b"albums" in response.data
        assert b"posts" in response.data