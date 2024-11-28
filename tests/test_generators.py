import pytest

from typing import Any

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(list_of_transactions: list[dict[str, Any]], my_currency: str) -> None:
    generator = filter_by_currency(list_of_transactions, my_currency)
    assert next(generator) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert next(generator) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
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
