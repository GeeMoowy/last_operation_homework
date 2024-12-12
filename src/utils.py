import json
import logging
import os
from json import JSONDecodeError
from typing import Any
import requests
from dotenv import load_dotenv

load_dotenv()
apilayer_key = os.getenv("API_KEY")


logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log', 'w', encoding='UTF-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transactions_list(file_path: str) -> list[dict[str, Any]]:
    if os.path.isfile(file_path):
        logger.info(f'Чтение и преобразование файла {file_path}')
        with open(file_path, "r", encoding="utf-8") as json_file:
            try:
                transactions = json.load(json_file)
            except JSONDecodeError as ex:
                logger.error(f'Произошла ошибка: {ex}')
                return []
        logger.info(f'Функция {transactions_list.__name__} завершила работу корректно')
        return transactions
    else:
        logger.info('JSON-файл не существует')
        return []


def amount_transaction(transaction: dict[str, Any]) -> float:
    try:
        logger.info(f'Проверка значения на код валюты')
        if transaction["operationAmount"]["currency"]["code"] != "RUB":
            logger.info(f'Значение в {transaction["operationAmount"]["currency"]["code"]}, обращение к API')
            url = "https://api.apilayer.com/exchangerates_data/convert"
            payload = {
                "amount": transaction["operationAmount"]["amount"],
                "from": transaction["operationAmount"]["currency"]["code"],
                "to": "RUB"
            }
            headers = {
                "apikey": f"{apilayer_key}"
            }
            try:
                response = requests.get(url, headers=headers, params=payload)
                result = response.json()
                logger.debug(f'Значение в рублях {float(result['result'])}')
                return float(result['result'])
            except requests.RequestException as ex:
                logger.error(f'Произошла ошибка: {ex}')
                return 0.0
        logger.debug(f'Валюта в рублях, значение {transaction["operationAmount"]["amount"]}')
        return float(transaction["operationAmount"]["amount"])
    except Exception as ex:
        logger.error(f'Произошла ошибка: {ex}')
        raise Exception(Exception)
