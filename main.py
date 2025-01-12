import os
from src.file_reader import read_transactions_from_csv, read_transactions_from_excel
from src.utils import load_transactions
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.decorators import log


@log()
def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        print("4. Выйти из программы")

        choice = input("Введите номер пункта: ").strip()

        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            file_path = os.path.join(os.path.dirname(__file__), "data", "transactions.json")
            transactions = load_transactions(file_path)
        elif choice == "2":
            print("Для обработки выбран CSV-файл.")
            file_path = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")
            transactions = read_transactions_from_csv(file_path)
        elif choice == "3":
            print("Для обработки выбран XLSX-файл.")
            file_path = os.path.join(os.path.dirname(__file__), "data", "transactions.xlsx")
            transactions = read_transactions_from_excel(file_path)
        else:
            print("Неверный пункт меню. Программа завершена.")
            return

        if not transactions:
            print("Не удалось загрузить данные транзакций.")
            return

        # Фильтрация по статусу
        valid_states = {"EXECUTED", "CANCELED", "PENDING"}
        while True:
            state = input(
                f"Введите статус, по которому необходимо выполнить фильтрацию. "
                f"Доступные статусы: {', '.join(valid_states)}\n"
            ).strip().upper()

            if state in valid_states:
                transactions = filter_by_state(transactions, state)
                print(f"Операции отфильтрованы по статусу \"{state}\"")
                break
            else:
                print(f"Статус операции \"{state}\" недоступен.")

        if not transactions:
            print(f"Нет операций со статусом \"{state}\".")
            continue

        # Сортировка по дате
        sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
        if sort_choice in {"да", "yes"}:
            order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
            descending = order not in {"по возрастанию", "возрастание"}
            transactions = sort_by_date(transactions, descending)

        # Фильтрация по валюте
        currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
        if currency_choice in {"да", "yes"}:
            transactions = list(filter_by_currency(transactions, "RUB"))

        if not transactions:
            print("Нет операций, соответствующих вашему запросу.")
            continue

        # Вывод результатов
        print("Операции, соответствующие вашему запросу:")
        for transaction in transactions:
            print(transaction)


if __name__ == '__main__':
    main()