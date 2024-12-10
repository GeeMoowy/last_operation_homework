import json
import os
from json import JSONDecodeError
from typing import Any
import requests
from dotenv import load_dotenv

load_dotenv()
apilayer_key = os.getenv("API_KEY")


def transactions_list(file_path: str) -> list[dict[str, Any]]:
    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as json_file:
            try:
                transactions = json.load(json_file)
            except JSONDecodeError:
                return []
        return transactions
    else:
        return []


def amount_transaction(transaction: dict[str, Any]) -> float:
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
        return float(result['result'])
    return float(transaction["operationAmount"]["amount"])
