import csv

import pandas as pd
from typing import Any


def read_csv(file: Any) -> list[dict]:
    """Функция для считывания файла в формате csv с помощью открытия файла и использование метода DictReader"""
    with open(file, "r", encoding="utf=8") as f:
        reader = csv.DictReader(f)
        transactions = [row for row in reader]

    return transactions


def again_read_csv(file: Any):
    """Функция для считывания файла с помощью библеотеки Pandas"""
    return pd.read_csv(file)


if __name__ in "__main__":
    print(read_csv("../data/transactions.csv"))
    print(again_read_csv("../data/transactions.csv"))


def read_excel(file: Any):
    """Функция для считывание файла в формате excel с помощью библиотеки pandas"""
    r1 = pd.read_excel(file)
    return dict(r1)


if __name__ in "__main__":
    print(read_excel("../data/transactions_excel.xlsx"))
