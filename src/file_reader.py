from typing import List, Dict
import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает финансовые операции из CSV-файла.

    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями.
    :raises ValueError: Если произошла ошибка при чтении файла.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient='records')
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {e}")


def read_transactions_from_excel(file_path: str) -> List[Dict[str, str]]:
    """
    Считывает финансовые операции из Excel-файла.

    :param file_path: Путь к Excel-файлу.
    :return: Список словарей с транзакциями.
    :raises ValueError: Если произошла ошибка при чтении файла.
    """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient='records')
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel-файла: {e}")
