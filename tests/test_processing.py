import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> list[dict]:
    """
    Фикстура для создания тестового списка словарей с данными о транзакциях.

    Возвращает:
    - Список словарей, каждый из которых содержит id, state и дату транзакции.
    """
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize("state, expected_count", [("EXECUTED", 2), ("CANCELED", 2), ("PENDING", 0)])
def test_filter_by_state(sample_data: list[dict], state: str, expected_count: int) -> None:
    """
    Тестирует функцию filter_by_state.

    Параметры:
    - sample_data: Фикстура с тестовыми данными.
    - state: Значение статуса транзакции, по которому нужно фильтровать.
    - expected_count: Ожидаемое количество транзакций с заданным статусом.

    Проверяется, что фильтрация возвращает корректное количество записей.
    """
    filtered_data = filter_by_state(sample_data, state)
    assert len(filtered_data) == expected_count


def test_filter_by_state_empty_list() -> None:
    """
    Тестирует функцию filter_by_state с пустым списком.

    Проверяет, что функция возвращает пустой список, если на вход подан пустой список.
    """
    empty_data: list[dict] = []
    filtered_data = filter_by_state(empty_data, "EXECUTED")

    # Ожидаем, что возвращается пустой список
    assert filtered_data == []


@pytest.mark.parametrize(
    "reverse, expected_first_id", [(True, 1), (False, 4)]  # Последняя по дате операция  # Самая ранняя операция
)
def test_sort_by_date(sample_data: list[dict], reverse: bool, expected_first_id: int) -> None:
    """
    Тестирует функцию sort_by_date.

    Параметры:
    - sample_data: Фикстура с тестовыми данными.
    - reverse: Логическое значение, указывающее порядок сортировки (по убыванию или возрастанию).
    - expected_first_id: Ожидаемый ID первой записи в отсортированном списке.

    Проверяется, что функция корректно сортирует данные по дате.
    """
    sorted_data = sort_by_date(sample_data)

    if not reverse:
        sorted_data = sorted_data[::-1]  # Если сортировка по возрастанию, инвертируем результат

    assert sorted_data[0]["id"] == expected_first_id


def test_sort_by_date_with_equal_dates() -> None:
    """
    Тестирует функцию sort_by_date, проверяя корректность работы
    при наличии одинаковых дат.

    Проверяется, что сортировка корректно работает при одинаковых датах и не нарушает исходный порядок с одинаковыми
    значениями.
    """
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},  # одинаковая дата
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    sorted_data = sort_by_date(data)

    # Ожидаем, что записи с одинаковыми датами сохранят свой исходный порядок
    assert sorted_data[0]["id"] == 1
    assert sorted_data[1]["id"] == 2
    assert sorted_data[2]["id"] == 3


def test_sort_by_date_empty_list() -> None:
    """
    Тестирует функцию sort_by_date с пустым списком.

    Проверяет, что функция возвращает пустой список, если на вход подан пустой список.
    """
    empty_data: list[dict] = []
    sorted_data = sort_by_date(empty_data)

    # Ожидаем, что возвращается пустой список
    assert sorted_data == []
