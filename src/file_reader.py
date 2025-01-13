from typing import Any, Dict, List

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает транзакции из CSV-файла и возвращает их в виде списка словарей.
    """
    try:
        data = pd.read_csv(file_path)
        transactions = data.to_dict(orient="records")
        return [
            {
                "date": str(transaction["date"]),
                "amount": float(transaction["amount"]),
                "description": str(transaction["description"]),
            }
            for transaction in transactions
        ]
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {e}")


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает транзакции из Excel-файла и возвращает их в виде списка словарей.
    """
    try:
        data = pd.read_excel(file_path)
        transactions = data.to_dict(orient="records")
        return [
            {
                "date": str(transaction["date"]),
                "amount": float(transaction["amount"]),
                "description": str(transaction["description"]),
            }
            for transaction in transactions
        ]
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel-файла: {e}")
