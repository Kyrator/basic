# TODO здесь писать код
from collections.abc import Callable
import functools


def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий и выводящий количество вызовов
    декодируемой функции
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("Функция {func} была вызвана: {count} раз".format(
            func=func.__name__, count=wrapper.count
        ))
        return res

    wrapper.count = 0
    return wrapper


@counter
def test():
    print("test")


count = 0
while count < 10:
    test()
    count += 1
