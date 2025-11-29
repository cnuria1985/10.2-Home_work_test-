import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number(true_number_card):
    assert get_mask_card_number(true_number_card) == '1234 56** **** 3456'

def test_get_mask_account(true_number_account):
    assert get_mask_account(true_number_account) == '**7890'



