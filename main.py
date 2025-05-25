# import os
# import re
# from collections import Counter
# from itertools import count
# from random import choice

from src.data_files import read_csv, read_xlsx

# from src.decorators import log
# from src.external_api import external_api
from src.generators import filter_by_currency, transaction_descriptions

# from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.regular import category_transactions, regular_word
from src.utils import transaction_json_conver
from src.widget import get_date, mask_account_card


def main():
    # Старт
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. ")

    # Выбор файла с транзакциями
    print(
        "Выберите необходимый пункт меню:\n1. Получить информацию о транзакциях из JSON-файла"
        "\n2. Получить информацию о транзакциях из CSV-файла\n3. Получить информацию о транзакциях из XLSX-файла"
    )

    key_data_type = {1: "JSON-файл", 2: "CSV-файл", 3: "XLSX-файл"}
    user_choice_file = int(input("Ввод: "))

    while user_choice_file not in [1, 2, 3]:
        print("Укажите корректный номер!")
        user_choice_file = int(input("Ввод: "))

    print(f"\nДля обработки выбран {key_data_type[user_choice_file]}.")

    # Забираем данные из выбранного файла и переводим их в список словарей
    if user_choice_file == 1:
        df = transaction_json_conver("data/operations.json")
    elif user_choice_file == 2:
        df = read_csv("transactions.csv")
    elif user_choice_file == 3:
        df = read_xlsx("transactions_excel.xlsx")

    # Выбор статуса для фильтра транзакций
    print(
        "\nВведите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, "
        "CANCELED, PENDING"
    )

    status_transactions = ["EXECUTED", "CANCELED", "PENDING"]
    user_choice_status = str(input("Ввод: ")).upper()

    while user_choice_status not in status_transactions:
        print(f'Статус операции "{user_choice_status}" недоступен.')
        user_choice_status = str(input("Ввод: ")).upper()

    # Фильтр транзакций по выбранному статусу
    try:
        status_filter_transactions = filter_by_state(df, user_choice_status)
        print(f'\nОперации отфильтрованы по статусу "{user_choice_status}".')

        # Сортировка транзакций по дате
        print("\nОтсортировать операции по дате? Да/Нет")
        user_choice_date = str(input("Ввод: ")).upper()

        while user_choice_date not in ["ДА", "НЕТ"]:
            print("Не корректный выбор!")
            user_choice_date = str(input("Ввод: ")).upper()

        if user_choice_date == "ДА":
            print("\nОтсортировать по возрастанию или по убыванию? По возрастанию/По убыванию")
            user_choice_sort = str(input("Ввод: ")).lower()

            while user_choice_sort not in ["по возрастанию", "по убыванию"]:
                print("Не корректный выбор!")
                user_choice_sort = str(input("Ввод: ")).lower()

            if user_choice_sort == "по убыванию":
                status_date_filter_transactions = sort_by_date(status_filter_transactions)
            elif user_choice_sort == "по возрастанию":
                status_date_filter_transactions = sort_by_date(status_filter_transactions, False)
            else:
                status_date_filter_transactions = status_filter_transactions
        else:
            status_date_filter_transactions = status_filter_transactions

        # Фильтр транзакций валюте RUB
        print("\nВыводить только рублевые транзакции? Да/Нет")
        user_choice_rub = str(input("Ввод: ")).upper()

        while user_choice_rub not in ["ДА", "НЕТ"]:
            print("Не корректный выбор!")
            user_choice_rub = str(input("Ввод: ")).upper()

        if user_choice_rub == "ДА":
            status_date_currency_filter_transactions = list(filter_by_currency(status_date_filter_transactions, "RUB"))
        else:
            status_date_currency_filter_transactions = status_date_filter_transactions

        # Подсчёт количества транзакций по description
        list_description_transactions = []
        amount_list = len(status_date_currency_filter_transactions)
        generator_description = transaction_descriptions(status_date_currency_filter_transactions)
        while amount_list > 0:
            list_description_transactions.append(next(generator_description))
            amount_list -= 1
        type_transactions = category_transactions(
            status_date_currency_filter_transactions, list_description_transactions
        )
        print(f"\n{type_transactions}")

        # Фильтр транзакций по слову
        print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_choice_pattern = str(input("Ввод: ")).upper()

        while user_choice_pattern not in ["ДА", "НЕТ"]:
            print("Не корректный выбор!")
            user_choice_pattern = str(input("Ввод: ")).upper()

        if user_choice_pattern == "ДА":

            user_pattern_word = str(input("Введите слово: "))

            # Вызов функции с регулярным выражением, для поиска по слову
            status_date_currency_word_filter_transactions = regular_word(
                status_date_currency_filter_transactions, user_pattern_word
            )
        else:
            status_date_currency_word_filter_transactions = status_date_currency_filter_transactions

        # Распечатываем итоговый результат по фильтрации транзакций
        len_filter_transactions = len(status_date_currency_word_filter_transactions)
        print("\nРаспечатываю итоговый список транзакций...")
        print(f"\nВсего банковских операций в выборке: {len_filter_transactions}")

        # Вывод транзакций в формате
        # 18.07.2018 Перевод организации
        # Visa Platinum 7492 65** **** 7202 -> Счет **0034
        # Сумма: 8390 руб.
        if len_filter_transactions == 0:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        else:
            for i in status_date_currency_word_filter_transactions:

                try:
                    print(
                        f"\n{get_date(i['date'])} "
                        f"{next(transaction_descriptions(status_date_currency_word_filter_transactions))}"
                    )
                    print(f"{mask_account_card(i['from'])} -> {mask_account_card(i['to'])}")
                    print(f"Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
                except ValueError:
                    print("Нет данных")
    except:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
