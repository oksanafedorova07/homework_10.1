import pytest
from typing_extensions import Union

from src.masks import get_mask_card_number, get_mask_account

def test_mask_card_number(cart_nember: Union[int, str]) -> str:
    assert get_mask_card_number('1526894329845268') == '1526 89** **** 5268'



def test_mask_card_nunber_with_wrong_quantity():
    assert get_mask_card_number('998700560967876543') == 'Неправильно задан номер карты'
    assert get_mask_card_number('12567834902309') == 'Неправильно задан номер карты'



def test_mask_card_number_empty():
    assert get_mask_card_number(' ') == 'Неправильно задан номер карты'

