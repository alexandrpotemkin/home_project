from typing import Any, Dict, List
from unittest.mock import mock_open, patch

from src.utils import load_transactions


def test_load_transactions_valid_file() -> None:
    """
    Тестирует функцию load_transactions с корректным JSON-файлом.

    Проверяет, что данные корректно загружаются и возвращаются как список словарей.
    """
    mock_data: str = '[{"amount": 100, "currency": "USD"}, {"amount": 200, "currency": "RUB"}]'
    with patch("builtins.open", mock_open(read_data=mock_data)), patch("os.path.exists", return_value=True):
        result: List[Dict[str, Any]] = load_transactions("mock_file.json")
    assert result == [{"amount": 100, "currency": "USD"}, {"amount": 200, "currency": "RUB"}]


def test_load_transactions_invalid_json() -> None:
    """
    Тестирует функцию load_transactions с некорректным JSON-файлом.

    Проверяет, что функция возвращает пустой список при ошибке разбора JSON.
    """
    mock_data: str = "INVALID JSON"
    with patch("builtins.open", mock_open(read_data=mock_data)), patch("os.path.exists", return_value=True):
        result: List[Dict[str, Any]] = load_transactions("mock_file.json")
    assert result == []
