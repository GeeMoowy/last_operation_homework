from collections import Counter
from typing import Any

import src.masks


def mask_account_card(card_info: str) -> str:
    """Функция принимает строку с информацией о карте и возвращает строку с маской номера"""
    # Разбиваем строку на список и присваиваем переменной номер счета/карты
    if card_info is None or type(card_info) != str or card_info == '':
        return ''
    card_info_list = card_info.split()
    card_number = card_info_list[-1]
    if card_info_list[0] == "Счет":
        mask_number = src.masks.get_mask_account(card_number)
        return str(card_info_list[0] + " " + mask_number)
    else:
        # Вызываем функцию из модуля masks
        mask_number = src.masks.get_mask_card_number(card_number)
        return str(" ".join(card_info_list[:-1]) + " " + mask_number)


def get_date(my_date: str) -> str:
    """Функция принимает строку с датой и переформатирует в 'ДД.ММ.ГГГГ'"""
    date_list = my_date[:10].split("-")
    year, month, day = date_list[0], date_list[1], date_list[2]
    return f'{day}.{month}.{year}'


def count_transactions_in_category(transactions_list: list[dict[str, Any]], category_list: list) -> dict[str, int]:
    """Функция принимает список словарей банковских транзакций и список категорий хранящихся в поле 'description',
    и возвращает словарь, где ключи - это категории, а значения - это количество категорий в списке"""
    all_category_list = []
    for transaction in transactions_list:
        if transaction['description'] in category_list:
            all_category_list.append(transaction['description'])
    result_dict = dict(Counter(all_category_list))
    return result_dict
