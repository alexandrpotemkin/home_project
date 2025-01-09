from typing import Any, Dict, List
from unittest.mock import Mock, patch

import pandas as pd
import pytest

from src.file_reader import read_transactions_from_csv, read_transactions_from_excel


@pytest.fixture
def sample_csv_data() -> pd.DataFrame:
    """Пример данных для CSV."""
    return pd.DataFrame(
        {
            "date": ["2023-01-01", "2023-01-02"],
            "amount": [100.5, -50.75],
            "description": ["Groceries", "Transport"],
        }
    )


@pytest.fixture
def sample_excel_data() -> pd.DataFrame:
    """Пример данных для Excel."""
    return pd.DataFrame(
        {
            "date": ["2023-01-01", "2023-01-02"],
            "amount": [200.0, -100.5],
            "description": ["Restaurant", "Utilities"],
        }
    )


@patch("pandas.read_csv")
def test_read_transactions_from_csv_success(mock_read_csv: Mock, sample_csv_data: pd.DataFrame) -> None:
    """
    Успешное чтение транзакций из CSV-файла.

    :param mock_read_csv: Мок объекта pandas.read_csv.
    :param sample_csv_data: Пример данных для CSV.
    """
    mock_read_csv.return_value = sample_csv_data
    result: List[Dict[str, Any]] = read_transactions_from_csv("dummy_path.csv")
    expected: List[Dict[str, Any]] = [
        {"date": "2023-01-01", "amount": 100.5, "description": "Groceries"},
        {"date": "2023-01-02", "amount": -50.75, "description": "Transport"},
    ]
    assert result == expected
    mock_read_csv.assert_called_once_with("dummy_path.csv")


@patch("pandas.read_csv")
def test_read_transactions_from_csv_invalid_file(mock_read_csv: Mock) -> None:
    """
    Ошибка при чтении CSV-файла.

    :param mock_read_csv: Мок объекта pandas.read_csv.
    """
    mock_read_csv.side_effect = Exception("Test error")
    with pytest.raises(ValueError, match="Ошибка при чтении CSV-файла: Test error"):
        read_transactions_from_csv("invalid_path.csv")


@patch("pandas.read_excel")
def test_read_transactions_from_excel_success(mock_read_excel: Mock, sample_excel_data: pd.DataFrame) -> None:
    """
    Успешное чтение транзакций из Excel-файла.

    :param mock_read_excel: Мок объекта pandas.read_excel.
    :param sample_excel_data: Пример данных для Excel.
    """
    mock_read_excel.return_value = sample_excel_data
    result: List[Dict[str, Any]] = read_transactions_from_excel("dummy_path.xlsx")
    expected: List[Dict[str, Any]] = [
        {"date": "2023-01-01", "amount": 200.0, "description": "Restaurant"},
        {"date": "2023-01-02", "amount": -100.5, "description": "Utilities"},
    ]
    assert result == expected
    mock_read_excel.assert_called_once_with("dummy_path.xlsx")


@patch("pandas.read_excel")
def test_read_transactions_from_excel_invalid_file(mock_read_excel: Mock) -> None:
    """
    Ошибка при чтении Excel-файла.

    :param mock_read_excel: Мок объекта pandas.read_excel.
    """
    mock_read_excel.side_effect = Exception("Test error")
    with pytest.raises(ValueError, match="Ошибка при чтении Excel-файла: Test error"):
        read_transactions_from_excel("invalid_path.xlsx")
