import re


def filter_transactions_by_keyword(transactions, keyword):
    result = []
    # Используем \b для точного соответствия словам
    pattern = rf"\b{keyword}[а-я]*\b"
    for transact in transactions:
        if re.search(pattern, transact.get("description", ""), re.IGNORECASE):
            result.append(transact)
    return result


def count_transactions_by_categories(transactions, categories):
    result = {}
    for category in categories:
        result[category] = 0  # Инициализируем счётчик для каждой категории

    for transact in transactions:
        description = transact.get("description", "")
        for category in categories:
            # Используем \b для корректного поиска категории
            if re.search(rf"\b{category}[а-я]*\b", description, re.IGNORECASE):
                result[category] += 1

    return result


transactions = [
    {"description": "Открытие вклада", "amount": 5000, "status": "EXECUTED", "date": "2023-12-01"},
    {"description": "Перевод с карты на карту", "amount": 1000, "status": "CANCELED", "date": "2023-11-15"},
    {"description": "Оплата услуг", "amount": 2000, "status": "PENDING", "date": "2023-12-05"},
    {"description": "Покупка билетов", "amount": 1500, "status": "CANCELED", "date": "2023-10-20"},
]

keyword = "услуг"
categories = ["вклад", "карту", "услуг"]

# print(filter_transactions_by_keyword(transactions, keyword))
# print(count_transactions_by_categories(transactions, categories))