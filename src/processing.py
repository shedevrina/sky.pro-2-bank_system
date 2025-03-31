def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
    указанному значению."""
    new_dict = []

    for transaction in transactions:
        if transaction["state"] == state:
            new_dict.append(transaction)
        else:
            continue

    return new_dict


def sort_by_date(transactions: list[dict], reverse_status: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date)."""
    sorted_date = sorted(transactions, key=lambda x: x["date"], reverse=reverse_status)
    return sorted_date
