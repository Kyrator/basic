# TODO здесь писать код
import functools
import time
from collections.abc import Callable
from datetime import datetime
from typing import Any


def log_methods(strftime: str) -> Callable:
    """
    Декоратор класса получает другой декоратор и принимает
    его ко всем методам класса
    """

    def decorate(cls):
        """
        Проходит по методам класса и
        ищет функции созданные нами и
        отправляет в функцию расчет создание
        и завершения функции
        """
        for i_method in dir(cls):
            if i_method.startswith('__'):
                continue
            cur_method = getattr(cls, i_method)
            name = cls.__name__
            if hasattr(cur_method, '__call__'):
                decorated_method = createtime(cur_method, name, strftime)
                setattr(cls, i_method, decorated_method)
        return cls

    return decorate


def createtime(func: Callable, name: str, format_date: str) -> Callable:
    """
    Декоратор класса. Принимает функцию и название класса
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """
        Функцию расчет создание
        и завершения функции
        """
        norm_format = ''
        name_func = name + '.' + func.__name__
        data_now = datetime.now()
        for symb in format_date:
            if symb.isalpha():
                norm_format += '%' + symb
            else:
                norm_format += symb
        format_data = data_now.strftime(norm_format)
        print('Запускается \'{name_func}\'. Дата и время запуска: {format_data}'.format(
            name_func=name_func,
            format_data=format_data,
        ))
        start = time.time()
        func(*args, **kwargs)
        work_hour = time.time() - start
        print('Завершение \'{name_func}\', время работы = {time_work}s'.format(
            name_func=name_func,
            time_work=round(work_hour, 3),
        ))
        print()
        return func

    return wrapper


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

