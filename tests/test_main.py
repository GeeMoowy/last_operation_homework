import unittest
from unittest.mock import patch

from main import choice_and_filter_by_state, choice_and_filter_by_description, choice_and_read, choice_sort_by_date, \
    choice_and_filter_by_currency, main


def test_choice_and_filter_by_state_valid_status():
    transactions = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'PENDING'}
    ]

    with patch('builtins.input', side_effect=['EXECUTED']):
        result = choice_and_filter_by_state(transactions)
        assert result == [
            {'id': 1, 'state': 'EXECUTED'}], f'Expected [{{"id": 1, "state": "EXECUTED"}}], got {result}'


def test_choice_and_filter_by_state_invalid_then_valid():
    transactions = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'PENDING'}
    ]
    with patch('builtins.input', side_effect=['INVALID', 'CANCELED']):
        result = choice_and_filter_by_state(transactions)
        assert result == [
            {'id': 2, 'state': 'CANCELED'}], f'Expected [{{"id": 2, "state": "CANCELED"}}], got {result}'


class TestChoiceAndFilterByDescription(unittest.TestCase):
    @patch('builtins.input', side_effect=['да', 'Открытие вклада'])
    def test_filter_by_description(self, mock_input):
        transactions = [
            {'id': 1, 'description': 'Перевод организации'},
            {'id': 2, 'description': 'Открытие вклада'},
            {'id': 3, 'description': 'Перевод со счета на счет'}
        ]
        expected_result = [{'id': 2, 'description': 'Открытие вклада'}]
        result = choice_and_filter_by_description(transactions)
        self.assertEqual(result, expected_result)

    @patch('builtins.input', side_effect=['нет'])
    def test_no_filter(self, mock_input):
        transactions = [
            {'id': 1, 'description': 'Перевод организации'},
            {'id': 2, 'description': 'Открытие вклада'},
            {'id': 3, 'description': 'Перевод со счета на счет'}
        ]
        result = choice_and_filter_by_description(transactions)
        self.assertEqual(result, transactions)


def test_choice_sort_by_date():
    mock_list = [{'date': '2023-01-01'}, {'date': '2023-01-02'}, {'date': '2023-01-03'}]
    mock_list1 = [{'date': '2023-01-03'}, {'date': '2023-01-02'}, {'date': '2023-01-01'}]

    with patch('builtins.input', side_effect=['да', 'по убыванию']), \
            patch('builtins.print') as mock_print:
        result = choice_sort_by_date(mock_list)
        assert result == [{'date': '2023-01-03'}, {'date': '2023-01-02'},
                          {'date': '2023-01-01'}], "Сортировка по убыванию не сработала"

    with patch('builtins.input', side_effect=['да', 'по возрастанию']), \
            patch('builtins.print') as mock_print:
        result = choice_sort_by_date(mock_list)
        assert result == [{'date': '2023-01-01'}, {'date': '2023-01-02'},
                          {'date': '2023-01-03'}], "Сортировка по возрастанию не сработала"

    with patch('builtins.input', side_effect=['да', 'по убыванию']), \
            patch('builtins.print') as mock_print:
        result = choice_sort_by_date(mock_list1)
        assert result == [{'date': '2023-01-03'}, {'date': '2023-01-02'},
                          {'date': '2023-01-01'}], "Сортировка по возрастанию не сработала"

    with patch('builtins.input', side_effect=['нет']), \
            patch('builtins.print') as mock_print:
        result = choice_sort_by_date(mock_list)
        assert result == mock_list, "Функция должна вернуть исходный список"


def test_choice_and_filter_by_currency():
    # Подготовка тестовых данных
    mock_transactions = [
        {'id': 1, 'currency_code': 'RUB', 'amount': 100},
        {'id': 2, 'currency_code': 'USD', 'amount': 200},
        {'id': 3, 'currency_code': 'RUB', 'amount': 300},
    ]

    # Тестирование фильтрации по рублевым транзакциям
    with patch('builtins.input', side_effect=['да']), \
         patch('src.generators.filter_by_currency', return_value=[mock_transactions[0], mock_transactions[2]]):
        result = choice_and_filter_by_currency(mock_transactions)
        assert result == [
            {'id': 1, 'currency_code': 'RUB', 'amount': 100},
            {'id': 3, 'currency_code': 'RUB', 'amount': 300}], "Тест не пройден: ожидались только рублевые транзакции."

    # Тестирование возврата всех транзакций
    with patch('builtins.input', side_effect=['нет']):
        result = choice_and_filter_by_currency(mock_transactions)
        assert result == mock_transactions, "Тест не пройден: ожидались все транзакции."

    print("Все тесты пройдены успешно!")


def test_main_function():
    with patch('builtins.print') as mock_print, \
            patch('builtins.input', side_effect=['1', 'да', 'по возрастанию', 'да', 'да', 'да']), \
            patch('main.choice_and_read', return_value=[
                {
                    'id': 441945886,
                    'state': 'EXECUTED',
                    'date': '2019-08-26T10:50:58.294041',
                    'amount': '31957.58',
                    'currency_name': 'руб.',
                    'currency_code': 'RUB',
                    'from': 'Maestro 1596837868705199',
                    'to': 'Счет 64686473678894779589',
                    'description': 'Перевод организации'}]), \
            patch('main.choice_and_filter_by_state', return_value=[
                {
                    'id': 441945886,
                    'state': 'EXECUTED',
                    'date': '2019-08-26T10:50:58.294041',
                    'amount': '31957.58',
                    'currency_name': 'руб.',
                    'currency_code': 'RUB',
                    'from': 'Maestro 1596837868705199',
                    'to': 'Счет 64686473678894779589',
                    'description': 'Перевод организации'}]), \
            patch('main.choice_sort_by_date', return_value=[
                {
                    'id': 441945886,
                    'state': 'EXECUTED',
                    'date': '2019-08-26T10:50:58.294041',
                    'amount': '31957.58',
                    'currency_name': 'руб.',
                    'currency_code': 'RUB',
                    'from': 'Maestro 1596837868705199',
                    'to': 'Счет 64686473678894779589',
                    'description': 'Перевод организации'}]), \
            patch('main.choice_and_filter_by_currency', return_value=[
                {
                    'id': 441945886,
                    'state': 'EXECUTED',
                    'date': '2019-08-26T10:50:58.294041',
                    'amount': '31957.58',
                    'currency_name': 'руб.',
                    'currency_code': 'RUB',
                    'from': 'Maestro 1596837868705199',
                    'to': 'Счет 64686473678894779589',
                    'description': 'Перевод организации'}]), \
            patch('main.choice_and_filter_by_description', return_value=[
                {'id': 441945886,
                 'state': 'EXECUTED',
                 'date': '2019-08-26T10:50:58.294041',
                 'amount': '31957.58',
                 'currency_name': 'руб.',
                 'currency_code': 'RUB',
                 'from': 'Maestro 1596837868705199',
                 'to': 'Счет 64686473678894779589',
                 'description': 'Перевод организации'}]):
        main()

        # Проверяем, что вывод был корректным
        mock_print.assert_any_call('Распечатываю итоговый список транзакций...')
        mock_print.assert_any_call('Всего банковских операций в выборке: 1')


@patch('main.transactions_list', autospec=True)
def test_choice_and_read_json(mock_transactions_list):
    # Подготовка тестовых данных
    mock_transactions_list.return_value = [
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
        }
    ]

    result = choice_and_read('1')
    expected_result = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
            "description": "Перевод организации"
        }
    ]
    assert result == expected_result


@patch('main.get_reading_csv', autospec=True)
def test_choice_and_read_csv(mock_get_reading_csv):
    # Подготовка тестовых данных
    mock_get_reading_csv.return_value = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
            "description": "Перевод организации"
        }
    ]

    result = choice_and_read('2')
    expected_result = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
            "description": "Перевод организации"
        }
    ]
    assert result == expected_result


@patch('main.get_reading_exel', autospec=True)
def test_choice_and_read_excel(mock_get_reading_exel):
    # Подготовка тестовых данных
    mock_get_reading_exel.return_value = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
            "description": "Перевод организации"
        }
    ]

    result = choice_and_read('3')
    expected_result = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
            "description": "Перевод организации"
        }
    ]
    assert result == expected_result
