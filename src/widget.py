from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account: str) -> str:
    """Для title. Тип и номер карты или счета маскируется. Для карты и счёта разные маски."""
    if not isinstance(account, str):
        raise TypeError("Не верный тип данных")
    else:

        if account.split(" "):
            account_set = account.split(" ")

            if len(account_set) >= 2:
                number = int(account_set[-1])

                if "Счет" in account_set:
                    mask_account = get_mask_account(int(number))
                    return f"Счет {mask_account}"

                elif "Visa" in account_set or "Maestro" in account_set or "MasterCard" in account_set:
                    mask_number = get_mask_card_number(int(number))
                    massage = " ".join(account_set[:-1])
                    return f"{massage} {mask_number}"
                else:
                    raise ValueError("Ошибка значения данных")
        else:
            raise ValueError("Ошибка значения данных")


def get_date(date_format: str) -> str:
    """Преобразования формата даты из "2024-03-11T02:26:18.671407" в "ДД.ММ.ГГГГ" ("11.03.2024")"""
    if type(date_format) != str:
        raise TypeError("Не верный тип данных")
    else:

        if len(date_format) >= 11 and "T" in date_format:
            data_day = date_format.split("T")
            list_data = list(data_day[0].split("-"))
            for i in list_data:
                if int(i) > 0:
                    continue
                else:
                    raise ValueError("Ошибка даты в ISO")

            date_object = datetime.strptime(data_day[0], "%Y-%m-%d").date()
            return f"{date_object.day}.{date_object.month}.{date_object.year}"
        else:
            raise ValueError("Ошибка даты в ISO")
