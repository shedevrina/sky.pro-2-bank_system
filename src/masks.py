from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты — XXXX XX** **** XXXX"""

    card_number_str = str(card_number)

    if len(card_number_str) == 16:
        return f"{card_number_str[:4]}  {card_number_str[5:7]}** **** {card_number_str[-4:]}"
    else:
        return "Не верный номер карты. Попробуйте ещё раз."


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция маскировки номера банковского счета — **XXXX"""

    account_number_str = str(account_number)

    if len(account_number_str) >= 6:
        return f"**{account_number_str[-4:]}"
    else:
        return "Не верный номер счета. Попробуйте ещё раз."
