import pytest

# Тестирования модуля masks.py
@pytest.fixture
def coll_number():
    """Номер карты пользователя"""
    return [1000100010001, 1000100010001000, 100010001000100010, 1000100010001000100]


@pytest.fixture
def coll_account():
    """Номер счета пользователя"""
    return [20002000200020002000, 20002000200020002003]


@pytest.fixture
def coll_negative_type():
    """Негативные данные для проверки номера счета//даты"""
    return [True, -3, [1, "hello", [0]], {}, [], None]


@pytest.fixture
def coll_data():
    return ["2024-03-11T02:26:18.671407", "1998-01-12T"]


@pytest.fixture
def coll_data_negative_value():
    return ["2024-03-00T02:26:18.671407", "YY-MM-DDT02:26:18.671407", ""]


# Тестирования модуля processing.py
@pytest.fixture
def coll_list_dict():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719571, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def coll_state():
    """Статусы запросов"""
    return ["EXECUTED", "CANCELED"]


def coll_negative_list_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-00-0T18:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": ""},
    ]


# Тестирования модуля generators.py
@pytest.fixture
def coll_transactions():
    return [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
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
