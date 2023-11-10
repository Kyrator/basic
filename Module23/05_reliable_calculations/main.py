# TODO здесь писать код
import math


# Здесь создайте функцию get_sage_sqrt
def get_sage_sqrt(number_func):
    try:
        return math.sqrt(number_func)
    except ValueError as exc:
        return "Ошибка \"{exc}\". Квадратный корень существует только от неотрицательных чисел".format(exc=exc)
    except Exception as exc:
        return "Ошибка \"{exc}\".".format(exc=exc)


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")
