import os

import requests
from dotenv import load_dotenv


def external_api(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —
    float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли."""
    if not isinstance(transaction, dict):
        raise TypeError("Не верный тип данных!")

    elif transaction == {}:
        raise ValueError("Пустые данные")

    else:
        if transaction["operationAmount"]["amount"] and transaction["operationAmount"]["currency"]["code"]:

            code_value = transaction["operationAmount"]["currency"]["code"]
            amount = transaction["operationAmount"]["amount"]

            if code_value == "RUB":
                return float(amount)
            elif code_value == "EUR" or code_value == "USD":

                load_dotenv()
                api_convert_rub = os.getenv(
                    "API_KEY_CONVERT_FROM_EUR_OR_USD_TO_RUB"
                )  # получаем API-код от сайта для https://api.apilayer.com
                headers = {"apikey": f"{api_convert_rub}"}

                payload = {}
                url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code_value}&amount={amount}"

                try:
                    response = requests.get(url, headers=headers, data=payload)

                    if response.status_code == 200:
                        result = response.json()
                        return round(result["result"], 2)

                    else:
                        return f"Ошибка API {response.status_code} - {response.text}"

                except requests.RequestException as e:
                    return f"Ошибка при обращении к API {e}"
            else:
                return "Валюта транзакции не подходит под следующие: RUB, USD, EUR"

        else:
            raise KeyError
