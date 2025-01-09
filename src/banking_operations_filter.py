import re
from collections import Counter
from typing import Dict, List


def search_transactions_by_description(transactions: List[Dict[str, str]], query: str) -> List[Dict[str, str]]:
    """
    Фильтрует список банковских операций по заданной строке поиска в описании.
    """
    if not transactions:
        raise ValueError("Список транзакций пуст.")

    result = []
    for transaction in transactions:
        description = transaction.get("description", "")
        if re.search(re.escape(query), description, re.IGNORECASE):
            result.append(transaction)

    return result


def count_transactions_by_category(transactions: List[Dict[str, str]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество банковских операций по категориям.
    """
    if not transactions:
        raise ValueError("Список транзакций пуст.")
    if not categories:
        raise ValueError("Список категорий пуст.")

    category_counter: Counter[str] = Counter()
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_counter[category] += 1

    # Гарантируем наличие всех категорий в результатах
    for category in categories:
        category_counter.setdefault(category, 0)

    return dict(category_counter)
