from typing import Any, Iterator


def filter_by_currency(transactions_list: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]] | str:
    """Функция принимает список словарей и возвращает итератор словарей отфильтрованный по заданной валюте"""
    transaction_by_currency: list[dict[str, Any]] = list(
        filter(lambda x: x.get("operationAmount").get("currency").get("code") == currency, transactions_list)
    )
    try:
        for transaction in transaction_by_currency:
            yield transaction
    except StopIteration:
        if not transactions_list:
            return "Нет доступных транзакций"
    return ""


def transaction_descriptions(transactions_list: list[dict[str, Any]]) -> Iterator[str] | str:
    """Функция принимает список словарей транзакция и возвращает описание каждой операции по очереди"""
    try:
        for transaction in transactions_list:
            yield transaction["description"]
    except StopIteration:
        if not transactions_list:
            return "Нет доступных транзакций"
    return ""


def card_number_generator(start: int, finish: int) -> Iterator[str] | str:
    """Функция принимает начальное и конечное значение для генерации диапазона номеров банковских карт"""
    if start < 0 or finish > 9999_9999_9999_9999:
        raise ValueError("Неверное значение диапазона")  # Вызываем исключение, если числа вне диапазона
    for numb in range(start, finish + 1):
        card_numb = str(numb)
        while len(card_numb) < 16:
            card_numb = "0" + card_numb
        format_card_numb = f"{card_numb[0:4]} {card_numb[4:8]} {card_numb[8:12]} {card_numb[12:16]}"
        yield format_card_numb
    return ""
