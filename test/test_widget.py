import pytest

from src import widget


@pytest.mark.parametrize(
    "account_string, expected",
    [
        ("Visa Platinum 1000100010001", "Visa Platinum 1000 10** **** 0001"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(account_string, expected):
    """Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции"""
    assert widget.mask_account_card(account_string) == expected


def test_mask_account_card_negative_type(coll_negative_type):
    """Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки,
    в зависимости от типа входных данных (карта или счет)"""
    with pytest.raises(TypeError) as info_type:
        for i in coll_negative_type:
            widget.mask_account_card(i)
    assert str(info_type.value) == "Не верный тип данных"


def test_get_date(coll_data):
    """Тестирование правильности преобразования даты"""
    assert widget.get_date(coll_data[0]) == "11.3.2024"
    assert widget.get_date(coll_data[1]) == "12.1.1998"


def test_get_date_negative_type(coll_negative_type):
    """Проверка работы функции на различных входных форматах даты,
    включая граничные случаи и нестандартные строки с датами."""
    with pytest.raises(TypeError) as inf_error_type:
        for i in coll_negative_type:
            widget.get_date(i)
    assert str(inf_error_type.value) == "Не верный тип данных"


def test_get_date_negative_value(coll_data_negative_value):
    """Проверка работы функции на различных входных форматах даты, не в формате ISO или других типах данных"""
    with pytest.raises(ValueError) as inf_error_value:
        for i in coll_data_negative_value:
            widget.get_date(i)
    assert str(inf_error_value.value) == "Ошибка даты в ISO"
