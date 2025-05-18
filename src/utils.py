import json
import logging
from pathlib import Path
from typing import Union

# Формат записи лога в файл должен включать метку времени, название модуля,
# уровень серьезности и сообщение, описывающее событие или ошибку, которые произошли.
logger = logging.getLogger(__name__)

root_path = Path(__file__).resolve().parents[1]

# Создаем хендлер для вывода в файл
file_hendler = logging.FileHandler(f"{root_path}/logs/utils_log.log")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(message)s")
file_hendler.setFormatter(file_formatter)
logger.addHandler(file_hendler)
logger.setLevel(logging.DEBUG)

# logger.debug('Debug message')g
# logger.info('Info message')
# logger.warning('Warning message')
# logger.error('Error message')
# logger.critical('Critical message')
# logger.debug('Debug message')


def transaction_json_conver(filepath="json.json") -> Union[dict, list[dict]]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    optional_list = []

    logger.info("Received JSON file with transaction")

    try:
        with open(filepath, encoding="utf-8") as f:
            logger.info("File is opened")
            transactions = json.load(f)
            logger.info("Data is unloading from JSON ")

        return transactions

    # !!!!! доделать !!!!
    except json.JSONDecodeError:
        print("Invalid JSON data.")
        logger.critical("Invalid JSON data")
        return optional_list

    except ValueError:
        print("Invalid JSON data.")
        logger.critical("Invalid JSON data")
        return optional_list
