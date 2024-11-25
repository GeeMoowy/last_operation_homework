from typing import Any, Iterator


def filter_by_currency(transactions_list: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """Функция принимает список словарей и возвращает итератор словарей отфильтрованный по заданной валюте"""
    return filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions_list)
