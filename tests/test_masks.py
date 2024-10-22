import pytest

from src.masks import get_mask_account, get_mask_card_number


# Параметризованные тесты для get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


# Проверка исключений для get_mask_card_number
@pytest.mark.parametrize(
    "invalid_card_number",
    [
        "899",  # слишком короткий номер
        "89909221136652295742",  # слишком длинный номер
        "hfrd482guri4786f",  # некорректные символы
    ],
)
def test_get_mask_card_number_invalid(invalid_card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card_number)


# Тесты для get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("64686473678894779589", "**9589"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


# Проверка исключений для get_mask_account
@pytest.mark.parametrize(
    "invalid_account_number",
    [
        "353",  # слишком короткий номер
        "ger845",  # некорректные символы
    ],
)
def test_get_mask_account_invalid(invalid_account_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(invalid_account_number)
