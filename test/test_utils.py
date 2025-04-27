from unittest.mock import patch

from src.utils import transaction_json_conver


@patch("src.utils.json.load")
@patch("src.utils.open")
def test_transaction_json_conver(mock_open, mock_json_load):
    mock_json_load.return_value = dict({"the_data": "This is fake data"})
    assert transaction_json_conver("filepath") == {"the_data": "This is fake data"}

    mock_json_load.return_value = [{"the_data": "This is real data"}, {"name": "John"}]
    assert transaction_json_conver("filepath") == [{"the_data": "This is real data"}, {"name": "John"}]
