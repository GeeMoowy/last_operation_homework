import re
from typing import Any


def filter_by_state(list_of_operations: list[dict[str, Any]], state_value: str = 'EXECUTED') -> list[dict[str, Any]]:
    """Функция принимает список словарей с банковскими операциями
    и возвращает отфильтрованный список словарей со значением по ключу
    'state' = 'EXECUTED'(состояние = ВЫПОЛНЕНО)"""
    filter_list = []
    for operation in list_of_operations:
        if 'state' in operation:
            if operation['state'] == state_value:
                filter_list.append(operation)
        else:
            continue
    return filter_list


def filter_by_user_word(transactions_list: list[dict[str, Any]], user_word: str) -> list[dict[str, Any]]:
    """Функция принимает список словарей транзакций и возвращает список словарей
    отфильтрованных по введенному значению пользователя в ключе 'description'"""
    pattern = re.compile(user_word, re.IGNORECASE)
    filtered_by_description = []
    for transaction in transactions_list:
        description = transaction.get("description")
        if description is not None:
            if re.search(pattern, str(description)) is not None:
                filtered_by_description.append(transaction)
    return filtered_by_description


def sort_by_date(list_of_operations: list[dict[str, Any]], sorting_order: bool = True) -> list[dict[str, Any]]:
    """Функция принимает список словарей с банковскими операциями
    и возвращает отсортированный список словарей по дате в порядке убывания"""
    sorted_list = sorted(list_of_operations, key=lambda x: x["date"], reverse=sorting_order)
    return sorted_list
