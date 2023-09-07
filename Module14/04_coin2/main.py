# TODO здесь писать код
import math


def check(number, id_point):
    while number < 0:
        print("Введите положительное число ")
        if id_point == 'x':
            number = float(input("X: "))
        elif id_point == 'y':
            number = float(input("Y: "))
    return number


def coin_place(point_x, point_y):
    return math.sqrt(point_x ** 2 + point_y ** 2)


def check_coin(radius_search, radius_coin):
    if radius_search >= radius_coin:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")


def main():
    print("Введите координаты монетки:")
    point_x = check(float(input("X: ")), 'x')
    point_y = check(float(input("Y: ")), 'y')
    radius_search = float(input("Введите радиус: "))
    radius_coin = coin_place(point_x, point_y)
    print(f"radius_coin = {radius_coin}")
    check_coin(radius_search, radius_coin)


main()
