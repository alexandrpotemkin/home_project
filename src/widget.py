from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от входных данных.

    Аргументы:
        data (str): Строка, содержащая тип и номер карты или счета.

    Возвращает:
        str: Строка с замаскированным номером.
    """
    if data.startswith("Счет"):
        # Обрабатываем счет
        account_number = data.split(" ")[1]
        masked_account = get_mask_account(account_number)
        return f"Счет {masked_account}"
    else:
        # Обрабатываем карту
        parts = data.rsplit(" ", 1)
        card_type = parts[0]
        card_number = parts[1]
        masked_card = get_mask_card_number(card_number)
        return f"{card_type} {masked_card}"


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
