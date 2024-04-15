from src.app import create_app
from main import app
import re

def test_posts():
    flask_app = app
    pattern = "<td>(.*?)</td>"

    with flask_app.test_client() as test_client:
        response = test_client.get('/posts')
        match_results = re.findall(pattern, response.text, re.IGNORECASE)
        assert response.status_code == 200
        assert match_results[0] == 'Bret'
        assert match_results[-2] == 'Moriah.Stanton'
