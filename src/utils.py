import json
import os
from json import JSONDecodeError
from pathlib import Path
from typing import Any


PATH_TO_DIR = Path(__file__).parent.parent
PATH_TO_FILE = Path(PATH_TO_DIR, "data", "operations.json")


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
