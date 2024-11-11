from typing import List


def filter_by_state(list_of_operations: List[dict], state_value: str ="EXECUTED") -> List[dict]:
    """Функция принимает список словарей с банковскими операциями
    и возвращает отфильтрованный список словарей со значением по ключу
    'state' = 'EXECUTED'(состояние = ВЫПОЛНЕНО)"""
    filter_list = []
    for operation in list_of_operations:
        if operation["state"] == state_value:
            filter_list.append(operation)
    return filter_list
