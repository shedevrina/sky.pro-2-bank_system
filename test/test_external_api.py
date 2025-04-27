from unittest.mock import patch

import pytest
from requests.exceptions import RequestException

from src.external_api import external_api


def test_external_api_negative_type(coll_negative_type_transaction_json):
    with pytest.raises(TypeError) as e:
        for i in coll_negative_type_transaction_json:
            external_api(i)

    assert str(e.value) == "Не верный тип данных!"


def test_external_api_not_transaction():
    with pytest.raises(ValueError) as e:
        external_api({})

    assert str(e.value) == "Пустые данные"


def test_external_api_not_key(coll_negative_transaction_to_api):
    with pytest.raises(KeyError) as e_inf:
        for i in coll_negative_transaction_to_api:
            external_api(i)

    assert e_inf.type == KeyError


def test_external_api_currence_rub():
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "RUB", "code": "RUB"}},
    }
    assert external_api(transaction) == 8221.37


@patch("requests.get")
def test_external_api(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 1406.91225, "success": True}

    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    }
    assert external_api(transaction) == 1406.91


@patch("requests.get")
def test_external_api_code(mock_get):
    code = 400
    text = "сервер не отвечает"
    mock_get.return_value.status_code = code
    mock_get.return_value.text = text

    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    }
    assert external_api(transaction) == f"Ошибка API {code} - {text}"


@patch("requests.get")
def test_external_api_error(mock_get):
    text = "request error"
    mock_get.side_effect = RequestException(text)

    a = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    }
    assert external_api(a) == f"Ошибка при обращении к API {text}"


@patch("requests.get")
def test_external_api_other_currency(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 1406.91225, "success": True}

    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "EGP"}},
    }
    assert external_api(transaction) == 'Валюта транзакции не подходит под следующие: RUB, USD, EUR'
