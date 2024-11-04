from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной валюте.

    Args:
        transactions (List[Dict]): Список транзакций.
        currency_code (str): Код валюты для фильтрации (например, 'USD').

    Yields:
        Dict: Транзакция, соответствующая заданной валюте.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Возвращает итератор с описанием каждой операции.

    Args:
        transactions (List[Dict]): Список транзакций.

    Yields:
        str: Описание операции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера карт в формате 'XXXX XXXX XXXX XXXX' в заданном диапазоне.

    Args:
        start (int): Начальное значение диапазона.
        end (int): Конечное значение диапазона.

    Yields:
        str: Номер карты в формате 'XXXX XXXX XXXX XXXX'.
    """
    for number in range(start, end + 1):
        yield (
            f"{number:016d}"[:4]
            + " "
            + f"{number:016d}"[4:8]
            + " "
            + f"{number:016d}"[8:12]
            + " "
            + f"{number:016d}"[12:16]
        )
