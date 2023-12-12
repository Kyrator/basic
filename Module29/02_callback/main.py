# TODO здесь писать код
import functools
from collections.abc import Callable
from typing import Any

app = dict()


def callback(path: str) -> Callable:
    """
    Декоратор с названием пути
    """
    def decorator_callback(func: Callable) -> Callable:
        """
        Декоратор функции
        добавляет в словарь путей функцию,
        если такой путь
        """
        app[path] = func
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        return wrapped

    return decorator_callback


@callback('//')
def example() -> str:
    """Функция ответа с сайта"""
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
