from typing import Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

transactions: List[Dict] = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


# Тесты для filter_by_currency
def test_filter_by_currency_usd() -> None:
    """
    Проверяет корректность фильтрации транзакций по валюте USD.
    """
    usd_transactions: List[Dict] = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 3  # Обновлено ожидаемое количество транзакций с USD
    for transaction in usd_transactions:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_no_results() -> None:
    """
    Проверяет, что возвращается пустой результат, если нет транзакций с заданной валютой.
    """
    eur_transactions: List[Dict] = list(filter_by_currency(transactions, "EUR"))
    assert len(eur_transactions) == 0


def test_filter_by_currency_empty_transactions() -> None:
    """
    Проверяет работу с пустым списком транзакций.
    """
    empty_transactions: List[Dict] = list(filter_by_currency([], "USD"))
    assert len(empty_transactions) == 0


# Тесты для transaction_descriptions
def test_transaction_descriptions() -> None:
    """
    Проверяет, что возвращаются корректные описания операций.
    """
    descriptions: List[str] = list(transaction_descriptions(transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


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
