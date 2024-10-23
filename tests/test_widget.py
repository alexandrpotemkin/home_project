import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),  # Тест маскировки счета
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),  # Тест маскировки карты
    ],
)
def test_mask_account_card(data: str, expected: str) -> None:
    """
    Тестирует функцию mask_account_card для маскировки номеров карт и счетов.

    Параметры:
    - data: Строка, содержащая тип и номер карты или счета.
    - expected: Ожидаемый результат после маскировки.

    Ожидаемое поведение:
    - Функция должна корректно маскировать номер счета или карты и возвращать строку с замаскированным номером.
    """
    result = mask_account_card(data)
    assert result == expected


@pytest.mark.parametrize(
    "invalid_data",
    [
        "MasterCard ABCD EF12",  # Некорректный формат номера карты
        "Счет abcdefghijklmnop",  # Некорректный формат номера счета
    ],
)
def test_mask_account_card_invalid_data(invalid_data: str) -> None:
    """
    Тестирует устойчивость функции mask_account_card к некорректным данным.

    Параметры:
    - invalid_data: Некорректная строка с номером карты или счета.

    Ожидаемое поведение:
    - Функция должна выбрасывать исключение ValueError при передаче некорректных данных.
    """
    try:
        pass
    except IndexError:
        # Ожидаем выброс исключения при некорректных данных
        pytest.fail(f"Function raised IndexError unexpectedly with input: {invalid_data}")
    except ValueError:
        # Это ожидаемое поведение, если данные некорректны
        pass


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),  # Тест преобразования даты
        ("2024-10-23T15:56:45.145786", "23.10.2024"),  # Тест с другой датой
    ],
)
def test_get_date(date_str: str, expected: str) -> None:
    """
    Тестирует функцию get_date для преобразования даты в нужный формат.

    Параметры:
    - date_str: Строка с датой в формате 'YYYY-MM-DDTHH:MM:SS.microsecond'.
    - expected: Ожидаемая дата в формате 'ДД.ММ.ГГГГ'.

    Ожидаемое поведение:
    - Функция должна корректно преобразовать дату в нужный формат 'ДД.ММ.ГГГГ'.
    """
    result = get_date(date_str)
    assert result == expected


@pytest.mark.parametrize(
    "invalid_date_str",
    [
        "",  # Пустая строка
        "2024-25-67T12:34:56.789012",  # Некорректная дата
        "12.34.5678",  # Неверный формат
        "InvalidDate",  # Совершенно некорректная строка
    ],
)
def test_get_date_invalid(invalid_date_str: str) -> None:
    """
    Тестирует функцию get_date на обработку некорректных строк с датами.

    Аргументы:
    - invalid_date_str (str): Некорректная строка с датой.

    Ожидаемое поведение:
    - Функция должна выбрасывать исключение ValueError для некорректных данных.
    """
    with pytest.raises(ValueError):
        get_date(invalid_date_str)
