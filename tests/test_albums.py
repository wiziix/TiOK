from src.app import create_app
from main import app
import re

def test_albums():
    flask_app = app
    username_pattern = "<td>(.*?)</td>"
    photo_pattern = r'https:\/\/via\.placeholder\.com\/150\/[0-9a-fA-F]{6}'

    with flask_app.test_client() as test_client:
        response = test_client.get('/albums')
        match_results = re.findall(username_pattern, response.text, re.IGNORECASE)
        assert response.status_code == 200
        assert match_results[0] == 'Bret'
        assert match_results[-2] == 'Moriah.Stanton'
        match_results2 = re.findall(photo_pattern, response.text, re.IGNORECASE | re.DOTALL)
        assert match_results2[0] == 'https://via.placeholder.com/150/92c952'
        assert match_results2[-1] == 'https://via.placeholder.com/150/92bfbf'