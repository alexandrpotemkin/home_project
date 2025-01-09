from typing import Dict, List

import pytest

from src.banking_operations_filter import count_transactions_by_category, search_transactions_by_description


def test_search_transactions_by_description() -> None:
    transactions: List[Dict[str, str]] = [
        {"id": "1", "description": "Оплата за услуги связи"},
        {"id": "2", "description": "Покупка продуктов"},
        {"id": "3", "description": "Оплата ЖКХ"},
    ]

    assert search_transactions_by_description(transactions, "Оплата") == [
        {"id": "1", "description": "Оплата за услуги связи"},
        {"id": "3", "description": "Оплата ЖКХ"},
    ]

    assert search_transactions_by_description(transactions, "Покупка") == [
        {"id": "2", "description": "Покупка продуктов"}
    ]

    assert search_transactions_by_description(transactions, "Нет в списке") == []

    with pytest.raises(ValueError):
        search_transactions_by_description([], "Оплата")


def test_count_transactions_by_category() -> None:
    transactions: List[Dict[str, str]] = [
        {"id": "1", "description": "Оплата за услуги связи"},
        {"id": "2", "description": "Покупка продуктов"},
        {"id": "3", "description": "Оплата ЖКХ"},
        {"id": "4", "description": "Ресторан"},
        {"id": "5", "description": "Оплата за услуги связи"},
    ]

    categories: List[str] = ["оплата", "покупка", "ресторан"]

    assert count_transactions_by_category(transactions, categories) == {"оплата": 3, "покупка": 1, "ресторан": 1}

    assert count_transactions_by_category(transactions, ["неизвестная категория"]) == {"неизвестная категория": 0}

    with pytest.raises(ValueError):
        count_transactions_by_category([], categories)

    with pytest.raises(ValueError):
        count_transactions_by_category(transactions, [])

    with pytest.raises(ValueError):
        count_transactions_by_category([], [])
