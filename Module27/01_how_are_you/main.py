# TODO здесь писать код
import functools
from typing import Callable


def how_are_you(func: Callable) -> None:
    """ Декоратор """
    @functools.wraps(func)
    def wrapper():
        """
        Обертка, которая выводит "Как дела? Хорошо.
        А у меня не очень! Ладно, держи свою функцию."
        """
        print("Как дела? Хорошо.")
        print("А у меня не очень! Ладно, держи свою функцию.")
        func()

    return wrapper


@how_are_you
def test() -> None:
    """ Функция, которая выводит "Тут что-то происходит..." """
    print('<Тут что-то происходит...>')


test()
