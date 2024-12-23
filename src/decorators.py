import functools
import sys
import time
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования начала и конца выполнения функции, её результата или ошибок, а также времени выполнения.

    :param filename: Имя файла для записи логов. Если не задан, лог выводится в консоль.
    :return: Обёрнутая функция.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            log_target = open(filename, "a") if filename else sys.stdout
            start_time = time.time()
            try:
                print(f"{func.__name__} start", file=log_target)
                result = func(*args, **kwargs)
                end_time = time.time()
                print(f"{func.__name__} ok, execution time: {end_time - start_time:.4f} seconds", file=log_target)
                return result
            except Exception as e:
                end_time = time.time()
                print(
                    f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}, "
                    f"execution time: {end_time - start_time:.4f} seconds",
                    file=log_target,
                )
                raise
            finally:
                if filename:
                    log_target.close()

        return wrapper

    return decorator
