import json
import re
from collections import Counter

import pandas as pd



from src.transactions import  read_excel, again_read_csv # Фильтрация по ключевому слову



# Загрузка данных из JSON
def load_transactions_from_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            transactions = json.load(file)
        print("Данные из JSON-файла успешно загружены!")
        return transactions
    except Exception as e:
        raise ValueError(f"Ошибка при загрузке данных из JSON: {e}")


# Загрузка данных из CSV
def load_transactions_from_csv(file_path):
    try:
        # Используем pandas для загрузки CSV с правильным разделителем
        data = pd.read_csv(file_path, sep=";")
        transactions = data.to_dict(orient="records")
        print("Данные из CSV-файла успешно загружены!")
        return transactions
    except Exception as e:
        raise ValueError(f"Ошибка при загрузке данных из CSV: {e}")


# Загрузка данных из Excel
def load_transactions_from_xlsx(file_path):
    try:
        data = pd.read_excel(file_path)
        transactions = data.to_dict(orient="records")
        print("Данные из XLSX-файла успешно загружены!")
        return transactions
    except Exception as e:
        raise ValueError(f"Ошибка при загрузке данных из XLSX: {e}")


def count_transactions_by_categories(transactions, categories):
    try:
        if not transactions or not categories:
            return {category: 0 for category in categories}  # Возвращаем 0 для всех категорий, если нет данных

        result = Counter()
        for category in categories:
            for transact in transactions:
                description = transact.get("description", "")
                if re.search(rf"\b{category}\b", description, re.IGNORECASE):
                    result[category] += 1
        return dict(result)
    except Exception as e:
        raise ValueError(f"Ошибка при подсчете транзакций по категориям: {e}")


# Основная функция
def main():
    try:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Ваш выбор (1/2/3): ")

        if choice == "1":
            file_path = "../data/operations.json"  # Укажи правильный путь
            transactions = load_transactions_from_json(file_path)
        elif choice == "2":
            file_path = "../data/transactions.csv"  # Укажи правильный путь
            transactions = load_transactions_from_csv(file_path)
        elif choice == "3":
            file_path = "../data/transactions_excel.xlsx"  # Укажи правильный путь
            transactions = load_transactions_from_xlsx(file_path)
        else:
            print("Вы ввели цифру вне диапазона выбора. Программа завершена.")
            return

        if not transactions:
            print("Не удалось загрузить данные. Программа завершена.")
            return

        # Запрос статуса с улучшенной обработкой некорректного ввода
        valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
        while True:
            status = input(f"\nВведите статус для фильтрации ({', '.join(valid_statuses)}): ").strip().upper()
            if status in valid_statuses:
                break
            print(
                f"Некорректный статус: '{status}'. Пожалуйста, выберите один из доступных: {', '.join(valid_statuses)}."
            )

        # Фильтрация по статусу
        filtered_transactions = [t for t in transactions if t.get("state") == status]
        print(f"\nОперации отфильтрованы по статусу '{status}'.")

        # Сортировка по дате
        if input("\nОтсортировать операции по дате? (Да/Нет): ").strip().lower() == "да":
            order = input("Отсортировать по возрастанию или по убыванию? (возрастанию/убыванию): ").strip().lower()
            reverse_order = order == "убыванию"
            filtered_transactions = sorted(filtered_transactions, key=lambda t: t["date"], reverse=reverse_order)
            print("\nОперации отсортированы по дате.")

        # Фильтрация по ключевому слову
        if input("\nОтфильтровать список транзакций по слову в описании? (Да/Нет): ").strip().lower() == "да":
            keyword = input("Введите ключевое слово: ").strip()
            filtered_transactions = filter_transactions_by_keyword(filtered_transactions, keyword)

        # Подсчет категорий
        categories = ["вклад", "карта", "услуг"]
        category_count = count_transactions_by_categories(filtered_transactions, categories)
        print("\nПодсчет категорий операций:")
        for category, count in category_count.items():
            print(f"{category}: {count} операций")

        # Результат
        if filtered_transactions:
            print("\nРаспечатываю итоговый список транзакций...")
            for transaction in filtered_transactions:
                print(transaction)
        else:
            print("\nНе найдено ни одной транзакции, подходящей под ваш запрос.")

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()