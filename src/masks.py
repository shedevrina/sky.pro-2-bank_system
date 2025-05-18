import logging

from src.utils import root_path

logger_mask = logging.getLogger()
logger_mask_file_hendler = logging.FileHandler(f"{root_path}/logs/masks_los.log")
logger_mask_file_formater = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
logger_mask_file_hendler.setFormatter(logger_mask_file_formater)
logger_mask.addHandler(logger_mask_file_hendler)
logger_mask.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты — XXXX XX** **** XXXX"""

    logger_mask.info("Received cart number")

    if isinstance(card_number, int):
        pass
    else:
        logger_mask.critical("Error in DataTypy")
        raise TypeError("Не верный тип данных")

    card_number_str = str(card_number)
    len_card_number_str = len(card_number_str)

    if (
        len_card_number_str == 13
        or len_card_number_str == 16
        or len_card_number_str == 18
        or len_card_number_str == 19
    ):
        logger_mask.info("Mask for cart number is DONE")
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"

    else:
        logger_mask.debug("Non-standard card length")
        raise ValueError("Не корректная длина номера карты")


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета — **XXXX"""

    logger_mask.info("Received account number")

    if isinstance(account_number, int):
        pass
    else:
        logger_mask.critical("Error in DataTypy")
        raise TypeError("Не верный тип данных")

    account_number_str = str(account_number)

    if len(account_number_str) == 20:
        logger_mask.info("Mask for number is DONE")
        return f"**{account_number_str[-4:]}"

    else:
        logger_mask.debug("Non-standard card length")
        raise ValueError("Не корректная длина номера счета")
