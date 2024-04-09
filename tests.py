from unittest.mock import patch, MagicMock
import main

def test_getUsernames():

    function_mock = MagicMock(return_value = {1: 'Bret'})

    with patch('main.getUsernames', function_mock):
        result = main.getUsernames().get(1)

    assert result == 'Bret', "Funkcja nie zwrocila oczekiwanych danych"

    function_mock.assert_called_once()

def test_getThumbnails():

    function_mock = MagicMock(return_value = {1: "https://via.placeholder.com/150/92c952"})

    with patch('main.getThumbnails', function_mock):
        result = main.getThumbnails().get(1)

    assert result == "https://via.placeholder.com/150/92c952", "Funkcja nie zwrocila oczekiwanych danych"


test_getUsernames()
test_getThumbnails()

