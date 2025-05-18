def filter_by_currency(list_transactions: list[dict], value: str) -> iter:
    """Функция - принимает на вход список словарей транзакции. Возвращает итератор, который поочередно выдает
    транзакции, где валюта операции соответствует заданной (например, USD)."""

    if not isinstance(list_transactions, list) or not isinstance(value, str):
        raise TypeError("Ошибка данных")
    else:
        value.upper()
        for i in list_transactions:
            if "operationAmount" not in i:
                raise KeyError("Ключ не обнаружен")
            elif (
                value == i["operationAmount"]["currency"]["code"] or value == i["operationAmount"]["currency"]["name"]
            ):
                yield i


def transaction_descriptions(list_transactions: list[dict]) -> iter:
    """Генератор. Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""

    if not isinstance(list_transactions, list):
        raise TypeError("Ошибка данных")
    else:
        for list_transaction in list_transactions:

            if "description" not in list_transaction:
                raise KeyError("Ключ не найден")
            else:
                yield list_transaction.get("description")


def card_number_generator(start: int, stop: int) -> str:
    """Генератор. Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генерирует номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Принимает начальное и конечное значения для генерации диапазона номеров."""
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Ошибка данных")
    if isinstance(start, bool) or isinstance(stop, bool):
        raise TypeError("Ошибка данных")
    elif start == stop:
        raise ValueError("Заданы не верные значения")
    else:
        if start < stop and 0 <= start < 9999999999999999 and 0 < stop <= 9999999999999999:
            num_cart = (i for i in range(start, stop))
            full_num_cart = ((16 - len(str(x))) * "0" + str(x) for x in num_cart)
            return (str(x[:4]) + " " + str(x[4:8]) + " " + str(x[8:12]) + " " + str(x[12:16]) for x in full_num_cart)
        else:
            raise ValueError("Заданы не верные значения")
