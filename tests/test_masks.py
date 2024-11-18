import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_info):
    assert get_mask_card_number(card_info) == '7000 79** **** 6361'


def test_get_mask_account(account_info):
    assert get_mask_account(account_info) == '**4305'