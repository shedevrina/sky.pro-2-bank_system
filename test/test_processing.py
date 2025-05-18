import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(coll_list_dict, coll_state):
    """Параметризация тестов для различных возможных значений статуса"""
    assert filter_by_state(coll_list_dict, state=coll_state[0]) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}
    ]
    assert filter_by_state(coll_list_dict, state=coll_state[1]) == [
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719571, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_not_state(coll_list_dict):
    """Проверка работы функции при отсутствии словарей с указанным статусом state в списке"""
    with pytest.raises(KeyError) as inf_error:
        filter_by_state(coll_list_dict, state="123")
    assert str(inf_error.value) == "'Значения по ключу не найдены'"


def test_sort_by_date(coll_list_dict):
    """Тестирование сортировки списка словарей по датам в порядке убывания и возрастания(включая одинаковые даты)"""
    assert sort_by_date(coll_list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719571, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(coll_list_dict, sorted_status=False) == [
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719571, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
