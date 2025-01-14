import re
from collections import Counter

transactions = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод с карты на карту",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    },
]


def search_description(operations, search_bar):
    """Функция для поиска в списке словарей операций по заданной строке — описанию с использованием библиотеки
    re."""
    search = [operation for operation in operations if re.findall(search_bar, operation["description"])]
    return search


list_categories = ["Перевод организации", "Перевод с карты на карту", "Перевод со счета на счет"]


def count_categories(operations, categories):
    """Функция для подсчета количества банковских операций определенного типа."""
    description = []
    for operation in operations:
        if operation["description"] in categories:
            description.append(operation["description"])
    counted = Counter(description)
    return counted


if __name__ == "__main__":
    # print(search_description(transactions, "Перевод организации"))

    print(count_categories(transactions, list_categories))
