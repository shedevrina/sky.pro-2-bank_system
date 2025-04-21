from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.decorators import log
import os


while True:
    print("Введите номер домашней работы (слева):\n1 block - 1\nhomework_10_1 - 10.1\nhomework_11_1 - 11.1\nhomework_11_2 - 11.2\n")
    input_homework = float(input("Домашняя работа номер: "))


    # 1 block
    if input_homework == 1:
        print("\n \n--------->1 block\n")

        print(get_mask_card_number(1000100010001))
        print(get_mask_account(73654108430135874305))

        print(mask_account_card("Visa Platinum 7000792289606361"))
        print(mask_account_card("Счет 73654108430135874305"))

        print(get_date("2024-03-11T02:26:18.671407"))
        print(get_date("1998-01-12T"))

    # homework_10_1
    elif input_homework == 10.1:
        print("\n \n--------->homework_10_1 \n")

        print(
            filter_by_state(
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ]
            )
        )
        print(
            sort_by_date(
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ]
            )
        )


    # homework_11_1

    elif input_homework == 11.1:

        print("\n \n--------->homework_11_1 \n")

        transactions = [
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
        ]

        usd_transactions = filter_by_currency(transactions, "RUB")
        for i in range(4):
            print(next(usd_transactions))

        descriptions = transaction_descriptions(transactions)
        for i in range(4):
            print(next(descriptions))

        for card_number in card_number_generator(6, 7):
            print(card_number)


    # homework_11_2
    elif input_homework == 11.2:

        print("\n \n--------->homework_11_2 \n")


        @log()
        def my_function(x, y):
            """Функция складывает два числа. Типы данных для сложения [int, str, float]"""
            return x + y


        my_function(1, 2)

        filename = (input("Введите название файла('.txt') для сохранения логов:"))
        print(f"Файл с логами {filename} будет сохранён в директорию {os.getcwd()}")

        @log(filename)
        def my_function(x, y):
            """Функция складывает два числа. Типы данных для сложения [int, str, float]"""
            return x + y

        my_function(1, 2)
