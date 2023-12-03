# TODO здесь писать код
import datetime
import functools
import random
from typing import Callable

error_names = ['ValueError', 'ArithmeticError', 'AssertionError', 'ImportError', 'NameError', 'OSError']


def logging(func: Callable) -> Callable:
    """ Декоратор регистрирует функцию как плагин"""

    @functools.wraps(func)
    def wrapper():
        """
        Обертка, которая перед выполнением
        декорируемой функции ждёт
        несколько секунд.
        """
        if random.randint(1, 4) == 2:
            error = random.choice(error_names)
            with open('function_errors.log', 'a') as error_file:
                answer = "{name_func} {name_error} {date}\n".format(
                    name_func=func.__name__,
                    name_error=error,
                    date=datetime.datetime.now()
                )
                error_file.writelines(answer)
                return "Возникла ошибка {error}".format(error=error)
        else:
            return f'Название функции "{func.__name__}", описание "{func.__doc__}".'

    return wrapper


@logging
def say_hello() -> str:
    """Функция привет"""
    return "Hello stranger"


@logging
def say_goodbye() -> str:
    """Функция пока"""
    return "Goodbye My Lover!"


count = 1
while count < 10:
    print(say_hello())
    print(say_goodbye())
    count += 1
