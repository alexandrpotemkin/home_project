import json
import logging
import os
from typing import Dict, List

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    :param file_path: Путь до JSON-файла.
    :return: Список словарей с данными о транзакциях или пустой список, если файл пустой,
             содержит не список или не найден.
    """
    if not os.path.exists(file_path):
        logger.error(f"Файл {file_path} не найден.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Файл {file_path} успешно загружен. Найдено {len(data)} транзакций.")
                return data
            else:
                logger.error(f"Файл {file_path} содержит некорректные данные (ожидался список).")
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}.")
    except OSError as e:
        logger.error(f"Ошибка чтения файла {file_path}: {e}")

    logger.warning(f"Возвращён пустой список транзакций для файла {file_path}.")
    return []
