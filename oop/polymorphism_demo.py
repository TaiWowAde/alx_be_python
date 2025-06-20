import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        if not isinstance(length, (int, float)):
            raise TypeError("length must be a number")
        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
