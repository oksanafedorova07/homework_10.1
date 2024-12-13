import pytest
from src.widget import mask_account_cart, get_date

@pytest.mark.parametrize("user_input, masked_output",[("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361")
    ("Счет 73654108430135874305", "Счет **4305"),
                                                      ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                      ("Счет 64686473678894779589", "Счет **9589"),
                                                      ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                                      ("Счет 35383033474447895560", "Счет **5560"),
                                                      ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                                      ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                                                      ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                                                      ("Счет 73654108430135874305", "Счет **4305")])




def test_mask_account_cart(user_input, masked_output) -> None:
    assert mask_account_cart(user_input) == masked_output

def test_mask_account_cart() -> None:
    assert mask_account_cart("73654108430135874305") == "**4305"
@pytest.mark.parametrize('value, expected', [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024-08-06", "06.08.2024")
])

def test_get_date(value, expected):
    assert get_date(value) == expected

@pytest.mark.parametrize("value, expected",[("2024.03.11T02:26:18.671407", "11.03.2024"),
                                            ("2024.08.06", "06.08.2024")])

def test_get_date(value, expected):
    assert get_date(value) == expected

@pytest.mark.parametrize("value, expected", [(" ", "Некорректная дата!")
                                            (" ", "Нукорректная дата!")])

def test_get_date(value, expected):
    assert get_date(value) != expected

