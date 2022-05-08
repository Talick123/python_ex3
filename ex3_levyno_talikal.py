'''
Written by: Noga Levy (ID: 315260927, login: levyno)
             and Tali Kalev (ID: 208629691, login: talikal)

Goal of the Program: create shapes classes (circle, square, rectangle)
then create class of shapes collections.
'''

from abc import ABC, abstractmethod
from math import pi

#==========CLASSES=============

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
    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shapes(self):
        return self._shapes

    @shapes.setter
    def shapes(self, shapes):
        #takes objects that are of type Shape
        shapes_l = [x for x in shapes if isinstance(x, Shape)]
        ls = sorted(shapes_l, key = lambda s : s.area()) #sorting by area
        self._shapes = ls

    def __len__(self):
        return len(self.shapes)

    def insert(self, s):
        if isinstance(s, Shape):
            area = s.area()
            for i in range(self.__len__()):
                if self.shapes[i].area() < area:
                    continue
                else:
                    self.shapes.insert(i, s)
                    break

    def __str__(self):
        l = []
        for x in self.shapes:
            l.append(str(x))
        s = "\n".join(l)
        return "Shapes in collection:\n{}".format(s)

    def biggestPerimeterDiff(self):
        if len(self.shapes) <= 0:
            return 0
        max = 0
        min = self.shapes[0].perimeter()
        for x in self.shapes:
            if x.perimeter() > max:
                max = x.perimeter()
            if x.perimeter() < min:
                min = x.perimeter()
        return max - min

    def sameAreaAs(self, s):
        ls = []
        if isinstance(s, Shape):
            ls = [x for x in self.shapes if x.area() == s.area()]
        return ls

    def howManyQuadrilaterals(self):
        ls = [x for x in self.shapes if isinstance(x, Rectangle)]
        return len(ls)


# =================END OF CLASSES===============
'''
#Creating 3 Shapes
c = Circle(90)
r = Rectangle(4, 6)
s = Square(-3)

#Printing
print(c)
print(r)
print(s)

#Checking le function
print(c <= r)
print(r <= s)
print(s <= s)

#Checking area function
print(c.area())
print(r.area())
print(s.area())

#Checking perimeter function
print(c.perimeter())
print(r.perimeter())
print(s.perimeter())

#Checking width property function
print(r.width)
print(s.width)

#Creating object of type ShapesCollection
ls =[s,r,c]
a = ShapesCollection(ls)

#Checking functions of ShapesCollection class
print(a.biggestPerimeterDiff())
print(a)
list2 = a.sameAreaAs(s)
for x in list2:
    print(x)
print(a.howManyQuadrilaterals())
'''
