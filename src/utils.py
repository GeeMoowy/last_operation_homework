import json
import os
from json import JSONDecodeError
from pathlib import Path
from typing import Any, Union
import logging
import requests
from dotenv import load_dotenv


PATH_TO_ROOT = Path(__file__).parent.parent
PATH_TO_FILE = Path(PATH_TO_ROOT, 'logs', 'utils.log')


load_dotenv()
apilayer_key = os.getenv("API_KEY")


logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(PATH_TO_FILE, 'w', encoding='UTF-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transactions_list(file_path: Union[str, Path]) -> list[dict[str, Any]]:
    if os.path.isfile(file_path):
        logger.info('Чтение и преобразование файла')
        with open(file_path, "r", encoding="utf-8") as json_file:
            try:
                transactions = json.load(json_file)
            except JSONDecodeError as ex:
                logger.error(f'Произошла ошибка: {ex}')
                return []
        logger.info('Функция завершила работу корректно')
        return transactions
    else:
        logger.info('JSON-файл не существует')
        return []


def amount_transaction(transaction: dict[str, Any]) -> float:
    try:
        logger.info('Проверка значения на код валюты')
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
