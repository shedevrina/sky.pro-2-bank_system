from src.data_files import read_xlsx, read_csv
from unittest.mock import patch


@patch("pandas.read_exel")
def test_read_xlsx(mock_exel):
    mock_exel.return_value.to_dict.return_value = [{"test":"test"}, {"test2":"test2"}]
    assert read_xlsx("test_patch") == [{"test":"test"}, {"test2":"test2"}]
    mock_exel.assert_called_once("test_patch")
