def filter_by_state(transactions: list[{}], state = 'EXECUTED') -> list[{}]:
    new_dict = []

    for transaction in transactions:
        if transaction['state'] == state:
            new_dict += transaction['state']
        else:
            continue

    return new_dict

def sort_by_date(transactions: list[{}], reverse=True) -> list[{}]:
    sorted_date = sorted(transactions, key=lambda x: x['date'])
    return sorted_date
