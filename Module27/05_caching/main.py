# TODO здесь писать код
import functools
from typing import Callable, Dict


def chash_func_fibo(func: Callable) -> Callable:
    """
    Декоратор, который кэширует результаты вызова
    функции и позволяет избежать повторных
    вычислений для одних и тех же аргументов
    """

    numbers_dict: Dict[int: int] = {0: 0, 1: 1}

    @functools.wraps(func)
    def wrapped_func(number):
        if number in numbers_dict:
            return numbers_dict[number]
        else:
            numbers_dict[number] = func(number)
        return numbers_dict[number]
    return wrapped_func


@chash_func_fibo
def fibonacci(number: int) -> int:
    """Функция вычисления числа Фибоначи"""
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
