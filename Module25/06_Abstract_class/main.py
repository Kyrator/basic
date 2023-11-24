# TODO здесь писать код
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __init__(self):
        self.text = ""

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(self.radius * math.pi, 2)


class Rectangle(Shape):
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def area(self):
        return round(self.height * self.weight, 2)


class Triangle(Shape):
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def area(self):
        return round(((self.height * self.weight) / 2), 2)


# Примеры работы с классом:
# Создание экземпляров классов

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
