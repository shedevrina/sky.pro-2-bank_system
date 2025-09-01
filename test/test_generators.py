import pytest

from src import generators
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(coll_transactions):
    generator = filter_by_currency(coll_transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264269,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_negative_value(coll_negative_type):
    with pytest.raises(TypeError) as info_type:
        for i in coll_negative_type:
            list(filter_by_currency(i, i))
    assert str(info_type.value) == "Ошибка данных"


def test_filter_by_currency_negative_key():
    with pytest.raises(KeyError) as info_key:
        a = filter_by_currency([{"1": 1}, {"2": 2}], "USD")
        next(a)
    assert str(info_key.value) == "'Ключ не обнаружен'"


def test_filter_by_currency_iterator(coll_transactions):
    with pytest.raises(StopIteration):
        iter_filter_by_currency = filter_by_currency(coll_transactions, "USD")
        next(iter_filter_by_currency)
        next(iter_filter_by_currency)
        next(iter_filter_by_currency)


def test_transaction_descriptions(coll_transactions):
    a = generators.transaction_descriptions(coll_transactions)
    assert next(a) == "Перевод организации"
    assert next(a) == "Перевод со счета на счет"
    assert next(a) == "Перевод со счета на счет"


def test_transaction_descriptions_negative_value(coll_negative_type):
    with pytest.raises(TypeError) as inf_type:
        for i in coll_negative_type:
            list(transaction_descriptions(i))
    assert str(inf_type.value) == "Ошибка данных"


def test_transaction_descriptions_iterator(coll_transactions):
    with pytest.raises(StopIteration):
        iter_transaction_descriptions = transaction_descriptions(coll_transactions)
        next(iter_transaction_descriptions)
        next(iter_transaction_descriptions)
        next(iter_transaction_descriptions)
        next(iter_transaction_descriptions)


def test_transaction_descriptions_key():
    with pytest.raises(KeyError) as inf_key:
        a = transaction_descriptions([{"description": 1}, {"1": 0}])
        next(a)
        next(a)
    assert str(inf_key.value) == "'Ключ не найден'"


def test_card_number_generator():
    generator = generators.card_number_generator(1, 4)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"


def test_card_number_generator_negative_value(coll_negative_type):
    with pytest.raises(TypeError) as inf_type:
        for i in coll_negative_type:
            list(card_number_generator(i, i))
    assert str(inf_type.value) == "Ошибка данных"


def test_card_number_generator_input_value():
    with pytest.raises(ValueError) as info_value:
        card_number_generator(1, 1)
        card_number_generator(2, 1)
    assert str(info_value.value) == "Заданы не верные значения"
