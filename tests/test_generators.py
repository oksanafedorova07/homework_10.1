import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions, transactions)


def test_filter_by_currency_currency(trans_list: list) -> None:
    for trans in trans_list:
        assert True


def test_filter_by_currency() -> None:
    """Функция для тестирования функции списка операций по валюте"""
    result = filter_by_currency(transactions, "USD")
    assert next(result) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


if __name__ == "__main__":
    with pytest.raises(StopIteration):
        filter_by_currency([], "USD")


if __name__ == "__main__":
    with pytest.raises(StopIteration):
        filter_by_currency(transactions, "")


@pytest.mark.parametrize("descrip", [("Перевод организации")])
def test_transaction_descriptions(descrip: str) -> None:
    """Функция для тестирования функции, формирующей список описания операций"""
    result_descriptions = transaction_descriptions(transactions)
    assert next(result_descriptions) == descrip


if __name__ == "__main__":
    with pytest.raises(StopIteration):
        transaction_descriptions([])


def test_card_number_generator() -> None:
    """Функция для тестирования генератора, формирующего номера банковских карт в определенном формате"""
    card_number = card_number_generator(1, 9999)
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    assert next(card_number) == "0000 0000 0000 0003"
    assert next(card_number) == "0000 0000 0000 0004"
    assert next(card_number) == "0000 0000 0000 0005"
    assert next(card_number) == "0000 0000 0000 0006"
    assert next(card_number) == "0000 0000 0000 0007"
    assert next(card_number) == "0000 0000 0000 0008"
    assert next(card_number) == "0000 0000 0000 0009"
    assert next(card_number) == "0000 0000 0000 0010"
    assert next(card_number) == "0000 0000 0000 0011"
    assert next(card_number) == "0000 0000 0000 0012"
    assert next(card_number) == "0000 0000 0000 0013"
    assert next(card_number) == "0000 0000 0000 0014"
    assert next(card_number) == "0000 0000 0000 0015"
    assert next(card_number) == "0000 0000 0000 0016"
    assert next(card_number) == "0000 0000 0000 0017"
    assert next(card_number) == "0000 0000 0000 0018"
    assert next(card_number) == "0000 0000 0000 0019"
    assert next(card_number) == "0000 0000 0000 0020"
    assert next(card_number) == "0000 0000 0000 0021"
    assert next(card_number) == "0000 0000 0000 0022"
    assert next(card_number) == "0000 0000 0000 0023"
    assert next(card_number) == "0000 0000 0000 0024"
    assert next(card_number) == "0000 0000 0000 0025"
