from typing import Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тесты для filter_by_currency
def test_filter_by_currency_usd(sample_transactions: List[dict]) -> None:
    """
    Проверяет корректность фильтрации транзакций по валюте USD.
    """
    usd_transactions: List[Dict] = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 3  # Обновлено ожидаемое количество транзакций с USD
    for transaction in usd_transactions:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_no_results(sample_transactions: List[dict]) -> None:
    """
    Проверяет, что возвращается пустой результат, если нет транзакций с заданной валютой.
    """
    eur_transactions: List[Dict] = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(eur_transactions) == 0


def test_filter_by_currency_empty_transactions() -> None:
    """
    Проверяет работу с пустым списком транзакций.
    """
    empty_transactions: List[Dict] = list(filter_by_currency([], "USD"))
    assert len(empty_transactions) == 0


# Тесты для transaction_descriptions
def test_transaction_descriptions(sample_transactions: List[dict], expected_descriptions: List[str]) -> None:
    """
    Проверяет, что возвращаются корректные описания операций.
    """
    descriptions: List[str] = list(transaction_descriptions(sample_transactions))
    assert descriptions == expected_descriptions


def test_transaction_descriptions_empty() -> None:
    """
    Проверяет работу с пустым списком транзакций.
    """
    empty_descriptions: List[str] = list(transaction_descriptions([]))
    assert empty_descriptions == []


# Тесты для card_number_generator
@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start: int, end: int, expected: List[str]) -> None:
    """
    Проверяет корректность генерации номеров карт в заданном диапазоне.
    """
    generated_numbers: List[str] = list(card_number_generator(start, end))
    assert generated_numbers == expected


def test_card_number_generator_format() -> None:
    """
    Проверяет форматирование номера карты.
    """
    card_number: str = next(card_number_generator(1, 1))
    assert len(card_number) == 19
    assert card_number.count(" ") == 3
    assert (
        card_number[:4].isdigit()
        and card_number[5:9].isdigit()
        and card_number[10:14].isdigit()
        and card_number[15:].isdigit()
    )
