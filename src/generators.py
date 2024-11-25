from typing import Any, Iterator


def filter_by_currency(transactions_list: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """Функция принимает список словарей и возвращает итератор словарей отфильтрованный по заданной валюте"""
    return filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions_list)


def transaction_descriptions(transactions_list: list[dict[str, Any]]) -> Iterator[str]:
    """Функция принимает список словарей транзакция и возвращает описание каждой операции по очереди"""
    return map(lambda x: x['description'], transactions_list)


def card_number_generator(start, finish):
    for numb in range(start, finish):
        card_numb = str(numb)
        while len(card_numb) < 16:
            card_numb = "0" + card_numb
        format_card_numb = f"{card_numb[0:4]} {card_numb[4:8]} {card_numb[8:12]} {card_numb[12:16]}"
        yield format_card_numb
