import os

from typing import Any, Dict

import requests

from requests import get


from dotenv import load_dotenv

load_dotenv()
values = os.getenv("PASSWORD")
# keys = os.getenv("API_KEY")
# headers = {keys: values}


def currency_conversion(transaction: dict) -> Any:
    """Функция конвертации"""
    amout = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amout}"
    payload: dict[Any, Any] = {}
    response = requests.get(url, headers={"apikey": values}, data=payload)
    result = response.json()
    return result["result"]
