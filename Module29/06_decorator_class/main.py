# TODO здесь писать код
import functools
from typing import Callable, Any
import time


class LoggerDecorator:
    """ Класс декоратор"""
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs) -> Any:
        self.num_calls += 1
        start_time = time.time()
        print('Вызов функции {name}'.format(name=self.__name__, ))
        print('Аргументы: {args}, {kwargs}'.format(args=args, kwargs=kwargs))
        print('Результат:', self.func(*args, **kwargs))
        end_time = time.time()
        print("Время выполнения: {work_time} секунд".format(work_time=end_time - start_time))
        return self.func(*args, **kwargs)


@LoggerDecorator
def complex_algorithm(arg1: int, arg2: int) -> int:
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)
