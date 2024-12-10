import json
import os
from json import JSONDecodeError
from pathlib import Path
from typing import Any
import requests
from dotenv import load_dotenv


PATH_TO_DIR = Path(__file__).parent.parent
PATH_TO_FILE = Path(PATH_TO_DIR, "data", "operations.json")


load_dotenv()
apilayer_key = os.getenv("API_KEY")


def transactions_list(file_path: Path) -> list[dict[str, Any]]:
    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as json_file:
            try:
                transactions = json.load(json_file)
            except JSONDecodeError:
                return []
            except FileNotFoundError:
                return []
        return transactions
    else:
        return []


def currency_conversion(transaction: dict[str, Any]) -> float:
    if transaction["operationAmount"]["currency"]["code"] != "RUB":
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {
            "amount": transaction["operationAmount"]["amount"],
            "from": transaction["operationAmount"]["currency"]["code"],
            "to": "RUB"
        }
        headers = {
            "apikey": f"{apilayer_key}"
        }
        response = requests.get(url, headers=headers, params=payload)
        result = response.json()
        return result['result']
    return float(transaction["operationAmount"]["amount"])


print(currency_conversion({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }))