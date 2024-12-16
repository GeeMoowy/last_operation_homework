import csv
from pathlib import Path
from typing import Union, Any

import pandas as pd


def get_reading_csv(path_to_csv: Union[str, Path]) -> list[dict[str, Any]]:
    with open(path_to_csv, encoding='UTF-8') as csv_file:
        reader_csv = csv.DictReader(csv_file, delimiter=';')
        for row in reader_csv:
            data = [row for row in reader_csv]
    return data


def get_reading_exel(path_to_exel: Union[str, Path]) -> list[dict[str, Any]]:
    df = pd.read_excel(path_to_exel)
    dict_list = df.to_dict(orient='records')
    return dict_list

#print(get_reading_csv('C:/Users/USER/PycharmProjects/last_operation_homework/data/transactions.csv'))
#print(get_reading_exel('C:/Users/USER/PycharmProjects/last_operation_homework/data/transactions_excel.xlsx'))