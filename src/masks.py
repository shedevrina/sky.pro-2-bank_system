def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты — XXXX XX** **** XXXX"""

    if isinstance(card_number, int):
        pass
    else:
        raise TypeError("Не верный тип данных")

    card_number_str = str(card_number)
    len_card_number_str = len(card_number_str)

    if (
        len_card_number_str == 13
        or len_card_number_str == 16
        or len_card_number_str == 18
        or len_card_number_str == 19
    ):
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    else:
        raise ValueError("Не корректная длина номера карты")


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета — **XXXX"""
    if isinstance(account_number, int):
        pass
    else:
        raise TypeError("Не верный тип данных")

    account_number_str = str(account_number)

    if len(account_number_str) == 20:
        return f"**{account_number_str[-4:]}"
    else:
        raise ValueError("Не корректная длина номера счета")
