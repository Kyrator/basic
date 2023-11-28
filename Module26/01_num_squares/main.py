# TODO здесь писать код
from collections.abc import Iterable


class Squares:
    """
    Класс-итератор.
    Генерирует последовательность из квадратов чисел от 1 до N
    """

    def __init__(self, n: int):
        self.__n = n
        self.__count = 0

    @property
    def __iter__(self) -> int:
        return self.__n

    def __next__(self) -> int:
        self.__count += 1
        return self.__count ** 2


def squares(n: int) -> Iterable[int]:
    """
    Функция-генератор.
    Генерирует последовательность из квадратов чисел от 1 до N
    """
    for i in range(1, n + 1):
        yield i ** 2


def square_numbers(n: int) -> Iterable[int]:
    """
    Генераторное выражение.
    Генерирует последовательность из квадратов чисел от 1 до N
    """
    return (i ** 2 for i in range(1, n + 1))


number = int(input("Введите число : "))

test1 = Squares(number)
test2 = squares(number)
test3 = square_numbers(number)

print("-" * 25)
for _ in range(number):
    print("test 1 =", test1.__next__())
print("-" * 25)
for _ in range(number):
    print("test 2 =", test2.__next__())
print("-" * 25)
for _ in range(number):
    print("test 3 =", test3.__next__())
