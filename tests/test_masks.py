from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_info: int) -> None:
    assert get_mask_card_number(card_info) == '7000 79** **** 6361'


def test_get_mask_account(account_info: int) -> None:
    assert get_mask_account(account_info) == '**4305'
