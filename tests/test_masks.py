import pytest  # noqa

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_mask_card_nunber_with_wrong_quantity() -> None:
    assert get_mask_card_number("997000792289606361") != "Неправильно задан номер карты"
    assert get_mask_card_number("70007922896063") != "Неправильно задан номер карты"


def test_mask_card_number_empty() -> None:
    assert get_mask_card_number(" ") != "Неправильно задан номер карты"


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"
