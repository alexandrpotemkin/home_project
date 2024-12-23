import pytest

from src.decorators import log


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """
    Функция сложения двух чисел.

    :param x: Первое число.
    :param y: Второе число.
    :return: Сумма чисел x и y.
    """
    return x + y


@log()
def divide(x: int, y: int) -> float:
    """
    Функция деления двух чисел.

    :param x: Делимое.
    :param y: Делитель.
    :return: Результат деления x на y.
    """
    return x / y


# Вызовы функций для демонстрации работы декоратора
my_function(3, 4)
try:
    divide(10, 0)
except ZeroDivisionError:
    pass


def test_my_function_log(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function start" in captured.out
    assert "my_function ok" in captured.out


def test_divide_log_error(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    captured = capsys.readouterr()
    assert "divide start" in captured.out
    assert "divide error: ZeroDivisionError" in captured.out
