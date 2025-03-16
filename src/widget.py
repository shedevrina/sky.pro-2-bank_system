from typing import Union


def mask_account_card(account: str) -> str:
    '''Тип и номер карты или счета маскируется. Для карты и счёта разные маски.'''
    if 'Счет' in account:
        return (f'{account[:4]} **{account[-4:]}')
    else:
        account_set = account.split(' ')
        account_set_number_mask = f'{account_set[-1][:4]} {account_set[-1][5:7]}** **** {account_set[-1][-4:]}'
        account_set[-1] = account_set_number_mask
        return ' '.join(account_set)

def get_date(date_format: str) -> str:
    '''Преобразования формата даты из "2024-03-11T02:26:18.671407" в "ДД.ММ.ГГГГ" ("11.03.2024")'''
    date_format_set = date_format.split('T')
    date_format_set_day = date_format_set[0].split('-')
    return f'{date_format_set_day[-1]}.{date_format_set_day[1]}.{date_format_set_day[0]}'