import re
from collections import Counter


def get_transactions_on_search_bar(data: list[dict], search_bar: str) -> list[dict]:
    """Возвращает список словарей с данными о банковских операциях по строке поиска"""
    pattern = rf"{search_bar}"
    transactions = []
    for transaction in data:
        for tr in transaction.values():
            if re.findall(pattern, str(tr), flags=re.IGNORECASE):
                transactions.append(transaction)
    return transactions