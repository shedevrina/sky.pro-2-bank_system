from unittest.mock import patch

import pytest

from src.utils import transaction_json_conver


@patch("")
def test_transaction_json_conver_negative_value():

    with pytest.raises(ValueError) as e:
        transaction_json_conver(optional_list="John")

    assert str(e.value) == "Invalid JSON data."
