from unittest.mock import patch, MagicMock

import main


def test_getUserData():

    request_mock = MagicMock(return_value = MagicMock(json = lambda: {"username" : "Bret"}))

    with patch('requests.get', request_mock):

        data = main.getUserData().json()

    request_mock.assert_called_once_with("https://jsonplaceholder.typicode.com/users")

    assert data == {"username" : "Bret"}, "Funkcja getUserData nie zwrocila oczekiwanych danych"


def test_getUsernames():

    function_mock = MagicMock(return_value = {1: 'Bret'})

    with patch('main.getUsernames', function_mock):
        result = main.getUsernames(main.getUserData()).get(1)

    assert result == 'Bret', "Funkcja nie zwróciła wartości Bret"

    function_mock.assert_called_once()

test_getUserData()
test_getUsernames()


