from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(list_of_transaction_modified: list[dict[str, Any]], my_currency: str) -> None:
    generator = filter_by_currency(list_of_transaction_modified, my_currency)
    assert next(generator) == {'id': 41428829,
                               'state': 'EXECUTED',
                               'date': '2019-07-03T18:35:29.512364',
                               'amount': '8221.37',
                               'currency_name': 'USD',
                               'currency_code': 'USD',
                               'from': 'MasterCard 7158300734726758',
                               'to': 'Счет 35383033474447895560',
                               'description': 'Перевод организации'
                               }


def test_filter_by_currency_empty() -> None:
    with pytest.raises(StopIteration):
        gen = filter_by_currency([], "USD")
        assert next(gen) == "Нет доступных транзакций"


def test_transaction_descriptions(list_of_transactions: list[dict[str, Any]]) -> None:
    generator = transaction_descriptions(list_of_transactions)
    assert next(generator) == "Перевод организации"


def test_transaction_descriptions_empty() -> None:
    with pytest.raises(StopIteration):
        gen = transaction_descriptions([])
        assert next(gen) == "Нет доступных транзакций"


@pytest.mark.parametrize("start, finish, result", [
    (1, 5, ["0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005"]
     ),
    (9999999999999998, 9999999999999999,
     ["9999 9999 9999 9998",
      "9999 9999 9999 9999"]
     )]
                         )
def test_card_number_generator(start: int, finish: int, result: str) -> None:
    gen = card_number_generator(start, finish)
    for res in result:
        assert next(gen) == res


@pytest.mark.parametrize("start, finish, result", [
    (-1, 5, "Неверное значение диапазона"),
    (9999_9999_9999_9999, 1_0000_0000_0000_0000, "Неверное значение диапазона")])
def test_card_number_generator_value_error(start: int, finish: int, result: str) -> None:
    with pytest.raises(ValueError):
        gen = card_number_generator(start, finish)
        assert next(gen) == "Неверное значение диапазона"
