from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_str: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от переданного значения.

    Аргументы:
    input_str (str): Строка с типом и номером карты или счёта.

    Возвращает:
    str: Строка с замаскированным номером карты или счёта.
    """
    input_lower = input_str.lower()

    if "счет" in input_lower:
        # Обработка счета
        account_number = input_str.split()[-1]
        return input_str.replace(account_number, get_mask_account(account_number))
    else:
        # Обработка карты
        card_number = input_str.split()[-1]
        return input_str.replace(card_number, get_mask_card_number(card_number))


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата 'YYYY-MM-DDTHH:MM:SS.microsecond' в формат 'ДД.ММ.ГГГГ'.

    Аргументы:
    date_str (str): Строка с датой в формате 'YYYY-MM-DDTHH:MM:SS.microsecond'.

    Возвращает:
    str: Строка с датой в формате 'ДД.ММ.ГГГГ'.
    """
    # Парсим строку даты и времени в объект datetime
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    # Преобразуем в строку формата "ДД.ММ.ГГГГ"
    return date_obj.strftime("%d.%m.%Y")
