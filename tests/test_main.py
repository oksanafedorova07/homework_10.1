import json
import os

import pandas as pd
import pytest

from src.main import (
    count_transactions_by_categories,
    load_transactions_from_csv,
    load_transactions_from_json,
    load_transactions_from_xlsx,
)

from src.sortis import filter_transactions_by_keyword

@pytest.fixture
def data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "data")


# Тестирование функции загрузки данных из JSON
def test_load_transactions_from_json(data_dir):
    file_path = os.path.join(data_dir, "operations.json")
    transactions = load_transactions_from_json(file_path)
    assert isinstance(transactions, list), "Данные должны быть в виде списка"


# Тестирование функции загрузки данных из CSV
def test_load_transactions_from_csv(data_dir):
    file_path = os.path.join(data_dir, "transactions.csv")
    transactions = load_transactions_from_csv(file_path)
    assert isinstance(transactions, list), "Данные должны быть в виде списка"


def test_load_transactions_from_xlsx(data_dir):
    file_path = os.path.join(data_dir, "transactions_excel.xlsx")
    transactions = load_transactions_from_xlsx(file_path)
    assert isinstance(transactions, list), "Данные должны быть в виде списка"


# Тестирование функции фильтрации по ключевому слову
def test_filter_transactions_by_keyword():
    transactions = [
        {"description": "Открытие вклада", "amount": 5000, "status": "EXECUTED", "date": "2023-12-01"},
        {"description": "Перевод с карты на карту", "amount": 1000, "status": "CANCELED", "date": "2023-11-15"},
        {"description": "Оплата услуг", "amount": 2000, "status": "PENDING", "date": "2023-12-05"},
        {"description": "Покупка билетов", "amount": 1500, "status": "CANCELED", "date": "2023-10-20"},
    ]
    keyword = "карта"
    result = filter_transactions_by_keyword(transactions, keyword)
    assert len(result) == 0, f"Должно быть 1 совпадение, а найдено {len(result)}"


# Тестирование функции подсчета категорий
def test_count_transactions_by_categories():
    transactions = [
        {"description": "Открытие вклада", "amount": 5000, "status": "EXECUTED", "date": "2023-12-01"},
    ]
    categories = ["вклада"]

    # Запускаем функцию
    result = count_transactions_by_categories(transactions, categories)
    print(f"Результат подсчета: {result}")

    # Проверяем, что количество транзакций в категории 'вклад' равно 1
    assert result["вклада"] == 1, f"Ожидалось 1 транзакция в категории 'вклад', но найдено {result['вклад']}"


# Вызов теста
# Тестирование загрузки данных из JSON с некорректным путём
def test_load_transactions_from_json_invalid_path(data_dir):
    invalid_file_path = os.path.join(data_dir, "invalid_operations.json")
    with pytest.raises(ValueError):
        load_transactions_from_json(invalid_file_path)


# Тестирование загрузки данных из CSV с некорректным путём
def test_load_transactions_from_csv_invalid_path(data_dir):
    invalid_file_path = os.path.join(data_dir, "invalid_transactions.csv")
    with pytest.raises(ValueError):
        load_transactions_from_csv(invalid_file_path)


# Тестирование загрузки данных из XLSX с некорректным путём
def test_load_transactions_from_xlsx_invalid_path(data_dir):
    invalid_file_path = os.path.join(data_dir, "invalid_transactions_excel.xlsx")
    with pytest.raises(ValueError):
        load_transactions_from_xlsx(invalid_file_path)


# Тестирование подсчета категорий при пустом списке транзакций
# Тестирование подсчета категорий при пустом списке транзакций
def test_count_transactions_by_categories_empty():
    transactions = []
    categories = ["вклад", "карта", "услуг"]
    result = count_transactions_by_categories(transactions, categories)
    assert result == {"вклад": 0, "карта": 0, "услуг": 0}, "Категории должны быть с нулевым количеством транзакций"


# Тестирование фильтрации по ключевому слову, если слово не найдено
def test_filter_transactions_by_keyword_no_match():
    transactions = [
        {"description": "Открытие вклада", "amount": 5000, "status": "EXECUTED", "date": "2023-12-01"},
        {"description": "Перевод с карты на карту", "amount": 1000, "status": "CANCELED", "date": "2023-11-15"},
    ]
    keyword = "покупка"
    result = filter_transactions_by_keyword(transactions, keyword)
    assert len(result) == 0, f"Не должно быть совпадений для ключевого слова '{keyword}'"


# Тестирование загрузки пустого JSON-файла
def test_load_transactions_from_json_empty(data_dir):
    empty_file_path = os.path.join(data_dir, "empty_operations.json")
    with open(empty_file_path, "w") as f:
        json.dump([], f)
    transactions = load_transactions_from_json(empty_file_path)
    assert transactions == [], "Данные должны быть пустыми"


# Тестирование загрузки пустого XLSX-файла
def test_load_transactions_from_xlsx_empty(data_dir):
    empty_file_path = os.path.join(data_dir, "empty_transactions_excel.xlsx")
    df = pd.DataFrame()  # создаем пустой DataFrame
    df.to_excel(empty_file_path, index=False)
    transactions = load_transactions_from_xlsx(empty_file_path)
    assert transactions == [], "Данные должны быть пустыми"


if __name__ == "__main__":
    test_load_transactions_from_json()
    test_load_transactions_from_csv()
    test_load_transactions_from_xlsx()
    test_filter_transactions_by_keyword()
    test_count_transactions_by_categories()
    test_filter_transactions_by_keyword_no_match()
    test_count_transactions_by_categories_empty()
    test_load_transactions_from_json_invalid_path()
    test_load_transactions_from_xlsx_invalid_path()
    test_load_transactions_from_csv_invalid_path()
    print("Все тесты пройдены успешно!")