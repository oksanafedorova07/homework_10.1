transactions = [
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
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(all_transactions: list, currency: str) -> None:
    """Функция, которая выдает транзакции, где валюта операции соответствует заданной."""
    if all_transactions == []:
        return "Нет данных"
        raise StopIteration("Нет данных")
    elif all_transactions != []:
        for transaction in all_transactions:
            filtered_transactions = [
                filter(
                    lambda transaction: transaction.get("operationAmount").get("currency").get("name") == currency,
                    all_transactions,
                )
            ]
            yield filtered_transactions
    usd_transactions = filter_by_currency(transaction, "USD")
    for _ in range(2):
        print(next(usd_transactions))
        for transaction in all_transactions:
            if transaction.get("operationAmount").get("currency").get("name") == currency:
                yield transaction
            else:
                continue
    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(5):
        print(next(usd_transactions))


def transaction_descriptions(list_transactions):
    """Функция, которая возвращает описание каждой операции по очереди"""
    if list_transactions == []:
        return "Нет данных"
        raise StopIteration("Нет данных")
    elif list_transactions != []:
        for transaction in list_transactions:
            yield transaction.get("description")
        for i, trans in enumerate(list_transactions):
            transaction = list_transactions[i].get("description")
            yield transaction
    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions))

        def transaction_descriptions(list_transactions):
            """Функция, которая возвращает описание каждой операции по очереди"""
            if list_transactions == []:
                return "Нет данных"
                raise StopIteration("Нет данных")
            elif list_transactions != []:
                for transaction in list_transactions:
                    yield transaction.get("description")
                for i, trans in enumerate(list_transactions):
                    transaction = list_transactions[i].get("description")
                    yield transaction
            descriptions = transaction_descriptions(transactions)
            for _ in range(5):
                print(next(descriptions))

        def card_number_generator(initial_value, final_value):
            """Функция-генератор для формирования номеров банковских карт в определенном формате"""
            for number in range(initial_value, final_value + 1):
                card_number = str(number)
                while len(card_number) < 16:
                    card_number = "0" + card_number
                yield f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
            for card_number in card_number_generator(1, 20):
                return card_number
