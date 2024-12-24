import pytest

from src.widget import get_date, mask_account_card, count_transactions_in_category


@pytest.mark.parametrize("card_info, mask_card", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758")
])
def test_mask_account_card(card_info: str, mask_card: str) -> None:
    assert mask_account_card(card_info) == mask_card


@pytest.mark.parametrize("card_info, mask_card", [
    (None, ''),
    (12, ''),
    ('', '')
])
def test_mask_account_card_empty(card_info, mask_card) -> None:
    assert mask_account_card(card_info) == mask_card


def test_get_date(full_date: str) -> None:
    assert get_date(full_date) == "11.03.2024"


def test_count_transactions_in_category(list_of_transactions, list_of_category):
    assert count_transactions_in_category(list_of_transactions, list_of_category) == {
        'Перевод организации': 2, 'Перевод со счета на счет': 2, 'Перевод с карты на карту': 1}
