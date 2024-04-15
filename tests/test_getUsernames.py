import main
from unittest.mock import patch, MagicMock

def test_getUsernames():

    function_mock = MagicMock(return_value = {1: 'Bret'})

    with patch('main.getUsernames', function_mock):
        result = main.getUsernames().get(1)

    assert result == 'Bret', "Funkcja nie zwrocila oczekiwanych danych"

    function_mock.assert_called_once()