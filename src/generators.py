from typing import Any, Iterator


def filter_by_currency(transactions_list: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """Функция принимает список словарей и возвращает итератор словарей отфильтрованный по заданной валюте"""
    return filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions_list)


def transaction_descriptions(transactions_list: list[dict[str, Any]]) -> Iterator[str]:
    """Функция принимает список словарей транзакция и возвращает описание каждой операции по очереди"""
    return map(lambda x: x['description'], transactions_list)
