import main
from unittest.mock import patch, MagicMock

def test_getThumbnails():

    function_mock = MagicMock(
        return_value = {1: "https://via.placeholder.com/150/92c952"}
    )

    with patch("main.getThumbnails", function_mock):
        result = main.getThumbnails().get(1)

    assert (
        result == "https://via.placeholder.com/150/92c952"
    ), "Funkcja nie zwrocila oczekiwanych danych"

    function_mock.assert_called_once()