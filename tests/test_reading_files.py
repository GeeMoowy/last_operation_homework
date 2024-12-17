from unittest.mock import patch, mock_open

import pandas as pd
import pytest

import src
from src.reading_file import get_reading_csv, get_reading_exel


def test_get_reading_csv():
    mock_data = "id;state;date;amount\n650703;EXECUTED;2023-09-05T11:30:32Z;16210\n3598919;EXECUTED;2020-12-06T23:00:58Z;29740"
    expected = [
        {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210'},
        {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740'}
    ]
    with patch("builtins.open", mock_open(read_data=mock_data), create=True):
        result = get_reading_csv("test_transactions.csv")
    assert result == expected


def test_get_reading_csv_not_file():
    result = get_reading_csv("test_transactions1.csv")
    assert result == []


@patch('src.reading_file.pd.read_excel')
def test_get_reading_exel(mock_get):
    expected_data = 'test_exel.xlsx'
    mock_get.return_value = pd.DataFrame([
        {'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210}
    ])
    expected_result = [
        {'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210}
    ]
    assert get_reading_exel(expected_data) == expected_result


@patch('src.reading_file.pd.read_excel')
def test_get_reading_exel_empty(mock_get):
    expected_data = 'test_exel_empty.xlsx'
    mock_get.return_value = pd.DataFrame([])
    expected_result = []
    assert get_reading_exel(expected_data) == expected_result
