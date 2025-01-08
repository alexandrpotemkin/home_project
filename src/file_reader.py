from typing import Dict, List

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает транзакции из CSV-файла и возвращает их в виде списка словарей.

    :param file_path: Путь к CSV-файлу.
    :return: Список транзакций в формате словарей с ключами "date", "amount", "description".
    """
    try:
        data = pd.read_csv(file_path)
        transactions = data.to_dict(orient="records")
        return [
            {
                "date": str(transaction["date"]),
                "amount": str(transaction["amount"]),
                "description": str(transaction["description"]),
            }
            for transaction in transactions
        ]
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {e}")


def read_transactions_from_excel(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает транзакции из Excel-файла и возвращает их в виде списка словарей.

    :param file_path: Путь к Excel-файлу.
    :return: Список транзакций в формате словарей с ключами "date", "amount", "description".
    """
    try:
        data = pd.read_excel(file_path)
        transactions = data.to_dict(orient="records")
        return [
            {
                "date": str(transaction["date"]),
                "amount": str(transaction["amount"]),
                "description": str(transaction["description"]),
            }
            for transaction in transactions
        ]
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel-файла: {e}")
