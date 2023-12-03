import functools
from typing import Callable
import time


def slower(func: Callable) -> None:
    """ Декоратор """

    @functools.wraps(func)
    def wrapper():
        """
        Обертка, которая перед выполнением
        декорируемой функции ждёт
        несколько секунд.
        """
        print("ждём несколько секунд")
        time.sleep(1)
        func()

    return wrapper


@slower
def check_web_site() -> None:
    """
    Функция, которая постоянно проверяет,
    изменились ли данные на веб-странице или её код
    """
    print("Проверка сайта")


count = 1

while count < 10:
    check_web_site()
    count += 1
