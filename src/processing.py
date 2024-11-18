from typing import Any


def filter_by_state(list_of_operations: list[dict[str, Any]], state_value: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция принимает список словарей с банковскими операциями
    и возвращает отфильтрованный список словарей со значением по ключу
    'state' = 'EXECUTED'(состояние = ВЫПОЛНЕНО)"""
    filter_list = []
    for operation in list_of_operations:
        if operation["state"] == state_value:
            filter_list.append(operation)
    return filter_list


def sort_by_date(list_of_operations: list[dict[str, Any]], sorting_order: bool = True) -> list[dict[str, Any]]:
    """Функция принимает список словарей с банковскими операциями
    и возвращает отсортированный список словарей по дате в порядке убывания"""
    sorted_list = sorted(list_of_operations, key=lambda x: x["date"], reverse=sorting_order)
    return sorted_list
