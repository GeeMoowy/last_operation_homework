from typing import Any, Iterator


def filter_by_currency(transactions_list: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]] | str:
    """Функция принимает список словарей и возвращает итератор словарей отфильтрованный по заданной валюте"""
    for transaction in transactions_list:
        if transaction is None:
            continue
        currency_code = transaction.get('currency_code')
        if currency_code == currency:
            yield transaction


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


if __name__ == '__main__':
    result = filter_by_currency([
        {
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
        },
        {
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
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ], 'USD')
