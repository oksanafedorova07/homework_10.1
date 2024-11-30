from typing import Union


def get_mask_card_number(cart_nember: Union[int, str]) -> str:
    """Функция маскировки номера бенковской карты"""
    return str(cart_nember)[0:4] + str(cart_nember)[16:] + "**" + "****" + str(cart_nember)[12:]


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция маскировки номера банковского счета"""
    return "**" + str(account_number)[16:]
