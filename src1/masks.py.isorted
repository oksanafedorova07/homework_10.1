from typing import Union


def get_mask_card_number(cart_nember: Union[int, str]) -> None:
    """Функция маскировки номера бенковской карты"""
    return cart_nember[0:4], cart_nember[16:] + "**", "****", cart_nember[12:]


def get_mask_account(account_number: Union[int, str]) -> None:
    """Функция маскировки номера банковского счета"""
    return "**" + account_number[16:]
