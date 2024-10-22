from typing import Any, Dict, List, Optional


def filter_by_state(list_of_dictionaries: List[Dict[str, Any]], state: Optional[str] = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Эта функция принимает список банковских операций в виде словарей и фильтрует их по значению ключа 'state'.
    Если значение ключа 'state' совпадает с переданным аргументом, операция добавляется в результат.

    :param list_of_dictionaries: Список словарей с банковскими операциями.
    :param state: Значение ключа 'state', по которому происходит фильтрация. По умолчанию 'EXECUTED'.
    :return: List[Dict[str, str]]: Отфильтрованный список словарей
    """
    return [item for item in list_of_dictionaries if item.get("state") == state]


def sort_by_date(list_of_dictionaries: List[Dict[str, Any]], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.

    Эта функция сортирует переданный список банковских операций по значению ключа 'date'.
    Даты должны быть в формате строки ISO ('YYYY-MM-DDTHH:MM:SS.microsecond').
    Сортировка может выполняться в порядке возрастания или убывания.

    :param list_of_dictionaries: Список словарей с банковскими операциями.
    :param descending: Порядок сортировки. По умолчанию True (по убыванию).
    :return: List[Dict[str, str]]: Отсортированный список словарей
    """

    return sorted(list_of_dictionaries, key=lambda x: x.get("date", ""), reverse=descending)