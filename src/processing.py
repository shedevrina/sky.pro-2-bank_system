from src.widget import get_date


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
    указанному значению."""
    new_dict = []
    num_state = 0

    if type(transactions) != list[dict] and type(state) != str:
        raise TypeError("Не верный тип данных")
    else:

        for transaction in transactions:
            if "state" in transaction:

                if transaction["state"] == state:
                    new_dict.append(transaction)
                    num_state += 1
                else:
                    continue
            else:
                continue
    if num_state == 0:
        raise KeyError("Значения по ключу не найдены")
    else:
        pass

    return new_dict


def sort_by_date(transactions: list[dict], sorted_status: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date)."""
    to_sorted_transactions = []

    if type(transactions) != list[dict] and type(sorted_status) != bool:
        raise TypeError("Не верный тип данных")

    for transaction in transactions:
        if get_date(transaction["date"]):
            to_sorted_transactions.append(transaction)
        else:
            continue

    sorted_date = sorted(to_sorted_transactions, key=lambda x: (x["date"], x["id"]), reverse=sorted_status)

    return sorted_date
