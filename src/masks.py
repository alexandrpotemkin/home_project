def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    Формат маски: ХХХХ ХХ** **** ХХХХ, где Х - это цифра.
    Показывает первые 6 цифр и последние 4 цифры, остальные символы заменяются звездочками.

    :param card_number: Номер карты в формате строки (должен содержать 16 цифр).
    :return: Замаскированный номер карты.
    :raises ValueError: Если номер карты не содержит 16 цифр или содержит нецифровые символы.
    """
    card_number = card_number.replace(" ", "")
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр.")

    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.

    Формат маски: **ХХХХ, где Х - это цифра номера.
    Показывает только последние 4 цифры номера, а перед ними - две звездочки.

    :param account_number: Номер счета в формате строки (должен содержать как минимум 6 цифр).
    :return: Замаскированный номер счета.
    :raises ValueError: Если номер счета содержит менее 6 цифр или нецифровые символы.
    """
    account_number = account_number.replace(" ", "")
    if len(account_number) < 6 or not account_number.isdigit():
        raise ValueError("Номер счета должен содержать хотя бы 6 цифр.")

    masked_account_number = f"**{account_number[-4:]}"
    return masked_account_number
