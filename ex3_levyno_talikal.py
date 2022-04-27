'''
Written by: Noga Levy (ID: 315260927, login: levyno)
             and Tali Kalev (ID: 208629691, login: talikal)

Goal of the Program:
'''

from abc import ABC, abstractmethod
from math import pi


class Shape(object):
        @abstractmethod
        def perimeter(self):
            pass

        @abstractmethod
        def area(self):
            pass

        def __le__(self, other):
            return self.area() <= other.area()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            self._radius = 1
        else:
            self._radius = radius

    def __str__(self):
        return "Circle: radius = {}".format(self.radius)

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return (self.radius**2) * pi


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width):
        if width <= 0:
            self._width = 1
        else:
            self._width = width

    @height.setter
    def height(self, height):
        if height <= 0:
            self._height = 1
        else:
            self._height = height

    def __str__(self):
        return "Rectangle: width = {}, height = {}".format(self.width, self.height)

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def __str__(self):
        return "Square: length = {}".format(self.width)


class ShapesCollection(object):
    def __init__(self):
        


c = Circle(90)
r = Rectangle(4, 6)
s = Square(-3)

print(c)
print(r)
print(s)

print(c <= r)
print(r <= s)
print(s <= s)

print(c.area())
print(r.area())
print(s.area())

print(c.perimeter())
print(r.perimeter())
print(s.perimeter())

print(r.width)
print(s.width)
