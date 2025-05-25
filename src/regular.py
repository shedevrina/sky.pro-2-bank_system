import re
from collections import Counter

from src.generators import transaction_descriptions


def regular_word(list_transactions: list[dict], word: str) -> list:
    """Принимает список словарей с данными о банковских операциях и строку поиска, а возвращает
    список словарей, у которых в описании есть данная строка."""
    if not isinstance(list_transactions, list) and not isinstance(word, str):
        raise TypeError("Не верный тип данных")

    if len(list_transactions) == 0:
        raise ValueError("Пустой список транзакций")
    else:
        new_list = []
        generator_description = transaction_descriptions(list_transactions)

        for i in list_transactions:
            match = re.search(word, next(generator_description), flags=re.IGNORECASE)
            if match:
                new_list.append(i)
            else:
                continue
    return new_list


def category_transactions(all_transactions: list[dict], list_category: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий, а значения — это количество
    операций в каждой категории. Категории операций хранятся в поле description."""
    if not isinstance(all_transactions, list) and not isinstance(list_category, list):
        raise TypeError("Не верный тип данных")

    sum_transactions = len(all_transactions)
    sum_category = len(list_category)
    list_description_trans = []

    if sum_transactions == 0 or sum_category == 0:
        raise ValueError("Пустые данные")
    else:
        for i in all_transactions:
            list_description_trans.append(i["description"])

    counter = Counter(list_description_trans)
    dict_category = {}

    for i in list_category:
        if i in counter.keys():
            dict_category[i] = counter.get(i)
        else:
            dict_category[i] = 0

    return dict_category
