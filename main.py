import re
from pathlib import Path

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date, filter_by_user_word
from src.reading_file import get_reading_csv, get_reading_exel
from src.utils import transactions_list

PATH_TO_ROOT = Path(__file__).parent
PATH_TO_DATA = Path(PATH_TO_ROOT, 'data')


def main():
    text = '''Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла'''
    print(text)
    list_of_point_text = re.findall(r'\d',text)
    while True:
        user_point = input('Введите номер необходимого пункта: ')
        if user_point == '1':
            print('Для обработки выбран JSON-файл.')
            json_path = Path(PATH_TO_DATA, 'operations.json')
            all_transactions = transactions_list(json_path)
            break
        elif user_point == '2':
            print('Для обработки выбран CSV-файл.')
            csv_path = Path(PATH_TO_DATA, 'transactions.csv')
            all_transactions = get_reading_csv(csv_path)
            break
        elif user_point == '3':
            print('Для обработки выбран XLSX-файл.')
            excel_path = Path(PATH_TO_DATA, 'transactions_excel.xlsx')
            all_transactions = get_reading_exel(excel_path)
            break
        else:
            print('Введите целое число от 1 до 3.')

    while True:
        print('''Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
        user_status = input()
        if user_status.upper() == "EXECUTED" or user_status.upper() == "CANCELED" or user_status.upper() == "PENDING":
            result_filter_by_state = filter_by_state(all_transactions, user_status)
            print(f'Операции отфильтрованы по статусу "{user_status.upper()}"')
            print(result_filter_by_state)
            break
        else:
            print(f'Статус операции "{user_status}" недоступен.')

    sort_order = None
    while True:
        sort_data = input('Отсортировать операции по дате? Да/Нет: ')
        if sort_data.lower() == "да":
            while True:
                sort_by = input('Отсортировать по возрастанию или по убыванию? ')
                if sort_by.lower() == 'по возрастанию':
                    sort_order = sort_by_date(result_filter_by_state, sorting_order=False)
                    break
                elif sort_by.lower() == 'по убыванию':
                    sort_order = sort_by_date(result_filter_by_state)
                    break
                else:
                    print('Введите только значения: по возрастанию или по убыванию')
            break
        elif sort_data.lower() == "нет":
            sort_order = result_filter_by_state
            break
        else:
            print('Введите только значения: да или нет')
    print(sort_order)
    while True:
        user_currency = input('Выводить только рублевые транзакции? Да/Нет: ')
        if user_currency.lower() == 'да':
            filtered_by_rub = []
            for transaction in list(filter_by_currency(sort_order, 'RUB')):
                filtered_by_rub.append(transaction)
            print(filtered_by_rub)
            break
        elif user_currency.lower() == 'нет':
            filtered_by_rub = sort_order
            print(filtered_by_rub)
            break
        else:
            print('Введите только значения: да или нет')

    input_answer = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ')
    if input_answer.lower() == 'да':
        user_word = input('Введите описание операции(например: Перевод организации):')
        filtered_by_description = filter_by_user_word(filtered_by_rub, user_word)
        print(filtered_by_description)
    else:
        filtered_by_description = filtered_by_rub
        print(filtered_by_description)

    print('Распечатываю итоговый список транзакций...')
    print(f'Всего банковских операций в выборке: {}')





if __name__ == "__main__":
    main()