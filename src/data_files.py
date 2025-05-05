import os
from pathlib import Path

import pandas as pd


def file_csv(file_name):
    """Функция считывания данных из .csv-файла"""
    files = []
    path_project = Path(__file__).parent.parent
    path_csv = f"{path_project}\data"
    files += os.listdir(path_csv)

    if file_name in files:
        data_from_csv = pd.read_csv(rf"{path_csv}\{file_name}")

    return data_from_csv


def file_xlsx(file_name):
    """Функция считывания данных из .xlsx-файла"""
    files = []
    path_project = Path(__file__).parent.parent
    path_xlsx = f"{path_project}\data"
    files += os.listdir(path_xlsx)

    if file_name in files:
        data_from_xlsx = pd.read_excel(rf"{path_xlsx}\{file_name}")

    return data_from_xlsx
