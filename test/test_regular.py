import pytest

from src.regular import category_transactions, regular_word


def test_regular_word(coll_transactions):
    assert regular_word(coll_transactions, "организации") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
    assert regular_word(coll_transactions, "счет") == [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264269,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def test_type_regular_word(coll_negative_type):
    with pytest.raises(TypeError) as inf_error_type:
        for i in coll_negative_type:
            regular_word(i)
        assert str(inf_error_type.value) == "Не верный тип данных"


# def test_value_regular_word():
#     with pytest.raises(ValueError) as inf_error_value:
#         regular_word([{}], word="test")
#         assert str(inf_error_value.value) == "Пустой список транзакций"


def test_category_transactions(coll_transactions, coll_list_description):
    assert category_transactions(coll_transactions, coll_list_description) == {
        "Перевод со счета на счет": 2,
        "test": 0,
    }


def test_type_category_transactions(coll_negative_type):
    with pytest.raises(TypeError) as inf_error_type:
        for i in coll_negative_type:
            category_transactions(i, i)
        assert str(inf_error_type.value) == "Не верный тип данных"


def test_value_category_transactions():
    with pytest.raises(ValueError) as inf_error_value:
        category_transactions([], [])
        assert str(inf_error_value.value) == "Пустые данные"
