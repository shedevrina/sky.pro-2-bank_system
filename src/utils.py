import json
from typing import Union


def transaction_json_conver(filepath="json.json", optional_list=[]) -> Union[dict, list[dict]]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    try:
        with open(filepath, encoding="utf-8") as f:
            transactions = json.load(f)

        return transactions

    except json.JSONDecodeError:
        print("Invalid JSON data.")
        return optional_list

    except ValueError:
        print("Invalid JSON data.")
        return optional_list
