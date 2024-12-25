from typing import Any, Dict
from unittest.mock import MagicMock, patch

from src.external_api import convert_to_rub


@patch("your_module.requests.get")
@patch("your_module.os.getenv", return_value="test_api_key")
def test_convert_to_rub_usd(mock_getenv: MagicMock, mock_get: MagicMock) -> None:
    """
    Тестирует функцию convert_to_rub для транзакции в USD.

    Проверяет корректность обращения к API и конвертации суммы в рубли.
    """
    mock_response: Dict[str, float] = {"result": 7500.0}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    transaction: Dict[str, Any] = {"amount": 100, "currency": "USD"}
    result: float = convert_to_rub(transaction)
    assert result == 7500.0


@patch("your_module.requests.get")
@patch("your_module.os.getenv", return_value="test_api_key")
def test_convert_to_rub_rub(mock_getenv: MagicMock, mock_get: MagicMock) -> None:
    """
    Тестирует функцию convert_to_rub для транзакции в рублях.

    Проверяет, что сумма возвращается без изменений для RUB.
    """
    transaction: Dict[str, Any] = {"amount": 1000, "currency": "RUB"}
    result: float = convert_to_rub(transaction)
    assert result == 1000.0
