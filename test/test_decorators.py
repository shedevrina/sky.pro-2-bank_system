import pytest

from src.decorators import log


def test_log_negative_filename(coll_negative_type):
    with pytest.raises(TypeError) as e:
        list(*(log(i) for i in coll_negative_type))
    assert str(e.value) == "Ошибка данных"


def test_log_massage(capsys):

    @log()
    def my_function(x, y):
        return x + y

    result = my_function(2, 3)
    assert result == 5

    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_massage_wirh_file():

    @log()
    def my_function(x, y):
        return x + y

    with pytest.raises(ValueError) as e:
        my_function(2, "3")

    assert str(e.value) == "Данные не складываются"


# @pytest.mark.parametrize("input_data, expected", [((1, 1), 2), (("13", "1"), "131"), ((1.1, 1), 2.1), ])
# def test_log(input_data, expected):
#
#     @log()
#     def my_function(x, y):
#         return x + y
#
#     assert my_function(input_data) == expected
