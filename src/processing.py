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


if __name__ == '__main__':
    result = filter_by_user_word([
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 615064591,
    "state": "CANCELED",
    "date": "2018-10-14T08:21:33.419441",
    "operationAmount": {
      "amount": "77751.04",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 3928549031574026",
    "to": "Счет 84163357546688983493"
  },
  {
    "id": 147815167,
    "state": "EXECUTED",
    "date": "2018-01-26T15:40:13.413061",
    "operationAmount": {
      "amount": "50870.71",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 4598300720424501",
    "to": "Счет 43597928997568165086"
  },
  {
    "id": 518707726,
    "state": "EXECUTED",
    "date": "2018-11-29T07:18:23.941293",
    "operationAmount": {
      "amount": "3348.98",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "MasterCard 3152479541115065",
    "to": "Visa Gold 9447344650495960"
  }
], "Перевод с карты на счет")
    print(result)