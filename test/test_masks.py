import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(coll_number):
    """Тестирование на позитивную работу маски номера карты"""
    assert get_mask_card_number(coll_number[0]) == "1000 10** **** 0001"
    assert get_mask_card_number(coll_number[1]) == "1000 10** **** 1000"
    assert get_mask_card_number(coll_number[2]) == "1000 10** **** 0010"
    assert get_mask_card_number(coll_number[3]) == "1000 10** **** 0100"


def test_get_mask_card_number_with_negative_number():
    """Тестирование на отрицательную работу маски номера. Тип данных верный - аргумент не верный"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(1000)
    assert str(exc_info.value) == "Не корректная длина номера карты"


def test_get_mask_card_number_with_negative_type(coll_negative_type):
    """Тестирование на отрицательную работу маски номера. Тип данных не верный"""
    with pytest.raises(TypeError) as exc_type_info:
        for i in coll_negative_type:
            get_mask_card_number(i)
    assert str(exc_type_info.value) == "Не верный тип данных"


def test_get_mask_account(coll_account):
    """Тестирование на позитивную работу маски номера счета"""
    assert get_mask_account(coll_account[0]) == "**2000"
    assert get_mask_account(coll_account[1]) == "**2003"


def test_get_mask_account_with_negative_number():
    """Тестирование на отрицательную работу маски счета. Тип данных верный - аргумент не верный"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(10001000)

        assert str(exc_info.value) == "Не верный номер. Попробуйте ввести номер ещё раз"


def test_get_mask_account_with_negative_type(coll_negative_type):
    """Тестирование на отрицательную работу маски счета. Тип данных не верный"""
    with pytest.raises(TypeError) as exc_type_info:
        for i in coll_negative_type:
            get_mask_account(i)
        assert str(exc_type_info.value) == "Не верный тип данных"
