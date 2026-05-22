from abc import ABC,abstractmethod

from matplotlib.patches import Rectangle 

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

circle1 = Circle(7)

print("Circle Area =", circle1.area())

print()


rectangle1 = Rectangle(10, 5)

print("Rectangle Area =", rectangle1.area())

print()


triangle1 = Triangle(8, 4)

print("Triangle Area =", triangle1.area())
