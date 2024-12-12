from unittest.mock import mock_open, patch

from src.utils import amount_transaction, transactions_list


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 441945886}]')
def test_transactions_list(mock_file) -> None:
    transactions = transactions_list("data/operations.json")
    assert transactions == [{"id": 441945886}]


@patch("builtins.open", new_callable=mock_open, read_data='')
def test_transactions_list_empty(mock_file):
    transactions = transactions_list("data/operations.json")
    assert transactions == []


@patch("builtins.open", new_callable=mock_open, read_data='{"id": 441945886}]')
def test_transactions_list_incorrect(mock_file):
    transactions = transactions_list("data/operations.json")
    assert transactions == []


def test_amount_transaction_rub(my_transaction_rub):
    assert amount_transaction(my_transaction_rub) == 31957.58


res = {
    'success': True, 'query':
        {'from': 'USD', 'to': 'RUB', 'amount': 8221.37
         }, 'info':
        {'timestamp': 1733867463, 'rate': 103.045091
         }, 'date': '2024-12-10', 'result': 847171.819795}


@patch('requests.get')
def test_amount_transaction_usd(mock_get, my_transaction_usd):
    mock_get.return_value.json.return_value = res
    assert amount_transaction(my_transaction_usd) == 847171.819795
