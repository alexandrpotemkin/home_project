import os
from typing import Dict

import requests
from dotenv import load_dotenv


def convert_to_rub(transaction: Dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными о транзакции, содержащий сумму (amount) и валюту (currency).
    :return: Сумма в рублях (float).
    """
    load_dotenv()
    amount = transaction.get("amount", 0)
    currency = transaction.get("currency", "RUB").upper()

    if currency == "RUB":
        return float(amount)

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API ключ для Exchange Rates Data API не найден в переменных окружения.")

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"from": currency, "to": "RUB", "amount": amount}
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return float(data.get("result", 0))
    else:
        response.raise_for_status()

    return 0


# transaction = {"amount": 100, "currency": "USD"}
# rub_amount = convert_to_rub(transaction)
# print(f"Сумма в рублях: {rub_amount}")
