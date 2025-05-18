import os
from pathlib import Path

import pandas as pd


def read_csv(file_name):
    """Функция считывания данных из .csv-файла"""
    files = []
    path_project = Path(__file__).parent.parent
    path_csv = rf"{path_project}\data"
    files += os.listdir(path_csv)

    if file_name in files:
        path_file = rf"{path_csv}\{file_name}"
        read = pd.read_csv(path_file, encoding="utf-8", delimiter=";")
        list_dict = read.to_dict(orient="records")
        return list_dict
    else:
        return "Заданный файл не обнаружен"


def read_xlsx(file_name):
    """Функция считывания данных из .xlsx-файла"""
    files = []
    path_project = Path(__file__).parent.parent
    path_xlsx = rf"{path_project}\data"
    files += os.listdir(path_xlsx)

    if file_name in files:
        data_from_xlsx = pd.read_excel(rf"{path_xlsx}\{file_name}")
        list_dict = data_from_xlsx.to_dict(orient="records")
        return list_dict
    else:
        return "Заданный файл не обнаружен"
