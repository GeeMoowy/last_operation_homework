from pathlib import Path
from typing import Any
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date, filter_by_user_word
from src.reading_file import get_reading_csv, get_reading_exel
from src.utils import transactions_list
from src.widget import get_date, mask_account_card


PATH_TO_ROOT = Path(__file__).parent
PATH_TO_DATA = Path(PATH_TO_ROOT, 'data')


def choice_and_read(user_point: str) -> list[dict[str, Any]]:
    if user_point == '1':
        print('Для обработки выбран JSON-файл.')
        json_path = Path(PATH_TO_DATA, 'operations.json')
        list_of_transactions =  transactions_list(json_path)
        formater_list = []
        for transaction in list_of_transactions:
            if transaction == {}:
                continue
            format_dict = {
                'id': transaction['id'],
                'state': transaction['state'],
                'date': transaction['date'],
                'amount': transaction['operationAmount']['amount'],  # Извлечение из вложенного словаря
                'currency_name': transaction['operationAmount']['currency']['name'],
                'currency_code': transaction['operationAmount']['currency']['code'],
                'from': transaction.get('from'),
                'to': transaction['to'],
                'description': transaction['description']
            }
            formater_list.append(format_dict)
        return formater_list
    elif user_point == '2':
        print('Для обработки выбран CSV-файл.')
        csv_path = Path(PATH_TO_DATA, 'transactions.csv')
        return get_reading_csv(csv_path)
    elif user_point == '3':
        print('Для обработки выбран XLSX-файл.')
        excel_path = Path(PATH_TO_DATA, 'transactions_excel.xlsx')
        return get_reading_exel(excel_path)


def choice_and_filter_by_state(all_transactions):
    print('Введите статус, по которому необходимо выполнить фильтрацию.\n'
          'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ')
    while True:
        user_status = input().upper()
        if user_status in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f'Операции отфильтрованы по статусу "{user_status.upper()}"')
            return filter_by_state(all_transactions, user_status)
        else:
            print(f'Статус операции "{user_status}" недоступен.')


def choice_sort_by_date(list_for_sort):
    while True:
        sort_data = input('Отсортировать операции по дате? Да/Нет: ')
        if sort_data.lower() == "да":
            while True:
                sort_by = input('Отсортировать по возрастанию или по убыванию? ')
                if sort_by.lower() == 'по возрастанию':
                    return sort_by_date(list_for_sort, sorting_order=False)
                elif sort_by.lower() == 'по убыванию':
                    return sort_by_date(list_for_sort)
                else:
                    print('Введите только значения: по возрастанию или по убыванию')
        elif sort_data.lower() == "нет":
            return list_for_sort
        else:
            print('Введите только значения: да или нет')


def choice_and_filter_by_currency(list_for_filter):
    while True:
        user_currency = input('Выводить только рублевые транзакции? Да/Нет: ')
        if user_currency.lower() == 'да':
            filtered_by_rub = []
            gen_filtered_by_rub = filter_by_currency(list_for_filter, 'RUB')
            for item in gen_filtered_by_rub:
                filtered_by_rub.append(item)
            return filtered_by_rub
        elif user_currency.lower() == 'нет':
            return list_for_filter
        else:
            print('Введите только значения: да или нет')


def choice_and_filter_by_description(list_for_filter):
    input_answer = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ')
    if input_answer.lower() == 'да':
        user_word = input('Введите описание операции(например: Перевод организации):')
        return filter_by_user_word(list_for_filter, user_word)
    else:
        return list_for_filter


def main():
    print('''Привет! Добро пожаловать в программу работы с банковскими транзакциями.\nВыберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')
    while True:
        user_point = input('Введите номер необходимого пункта: ')
        if user_point in ['1', '2', '3']:
            break
        else:
            print('Введите целое число от 1 до 3.')
    all_transactions = choice_and_read(user_point)
    filtered_by_state = choice_and_filter_by_state(all_transactions)
    sorted_by_date = choice_sort_by_date(filtered_by_state)
    filtered_by_currency = choice_and_filter_by_currency(sorted_by_date)
    filtered_by_description = choice_and_filter_by_description(filtered_by_currency)
    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке: {len(filtered_by_description)}')

    for transaction in filtered_by_description:
        print(f"{get_date(transaction['date'])} {transaction['description']}")
        if not transaction.get('from'):
            print(f"{mask_account_card(transaction['to'])}")
        else:
            print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")
        print(f"Сумма: {transaction['amount']} {transaction['currency_name']}")
        print()


if __name__ == "__main__":
    main()