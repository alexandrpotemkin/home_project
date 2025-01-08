from typing import Any, Dict, List
from unittest.mock import Mock, patch

import pandas as pd
import pytest

from src.file_reader import read_transactions_from_csv, read_transactions_from_excel


@pytest.fixture
def sample_csv_data() -> str:
    """Возвращает пример содержимого CSV-файла."""
    return "date,amount,description\n2023-01-01,100,Groceries\n2023-01-02,-50,Transport"


@pytest.fixture
def sample_excel_data() -> pd.DataFrame:
    """Возвращает пример содержимого Excel в виде DataFrame."""
    return pd.DataFrame(
        {"date": ["2023-01-01", "2023-01-02"], "amount": [100, -50], "description": ["Groceries", "Transport"]}
    )


@patch("pandas.read_csv")
def test_read_transactions_from_csv(mock_read_csv: Mock, sample_csv_data: str) -> None:
    """
    Тест для read_transactions_from_csv с использованием mock для pandas.read_csv.
    """
    # Настройка mock
    mock_read_csv.return_value = pd.DataFrame(
        [
            {"date": "2023-01-01", "amount": 100, "description": "Groceries"},
            {"date": "2023-01-02", "amount": -50, "description": "Transport"},
        ]
    )

    # Проверка
    result: List[Dict[str, Any]] = read_transactions_from_csv("dummy_path.csv")
    expected: List[Dict[str, Any]] = [
        {"date": "2023-01-01", "amount": 100, "description": "Groceries"},
        {"date": "2023-01-02", "amount": -50, "description": "Transport"},
    ]
    assert result == expected
    mock_read_csv.assert_called_once_with("dummy_path.csv")


@patch("pandas.read_excel")
def test_read_transactions_from_excel(mock_read_excel: Mock, sample_excel_data: pd.DataFrame) -> None:
    """
    Тест для read_transactions_from_excel с использованием mock для pandas.read_excel.
    """
    # Настройка mock
    mock_read_excel.return_value = sample_excel_data

    # Проверка
    result: List[Dict[str, Any]] = read_transactions_from_excel("dummy_path.xlsx")
    expected: List[Dict[str, Any]] = [
        {"date": "2023-01-01", "amount": 100, "description": "Groceries"},
        {"date": "2023-01-02", "amount": -50, "description": "Transport"},
    ]
    assert result == expected
    mock_read_excel.assert_called_once_with("dummy_path.xlsx")


def test_read_transactions_from_csv_invalid_file() -> None:
    """
    Тест для read_transactions_from_csv с несуществующим файлом.
    """
    with pytest.raises(ValueError, match="Ошибка при чтении CSV-файла"):
        read_transactions_from_csv("nonexistent.csv")


def test_read_transactions_from_excel_invalid_file() -> None:
    """
    Тест для read_transactions_from_excel с несуществующим файлом.
    """
    with pytest.raises(ValueError, match="Ошибка при чтении Excel-файла"):
        read_transactions_from_excel("nonexistent.xlsx")
