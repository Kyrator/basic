# TODO здесь писать код
import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:
    """ Декоратор дает возможность принимать другому декоратору принимать произвольные аргументы"""

    def decorator_maker(*args, **kwargs):
        def decorator_wrapped(func: Callable):
            return decorator_to_enhance(func, *args, **kwargs)

        return decorator_wrapped

    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """ Декоратор """

    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print("Переданные арг и кварг в декоратор:", dec_args, dec_kwargs)
        return func(*func_args, **func_kwargs)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
