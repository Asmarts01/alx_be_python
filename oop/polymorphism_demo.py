# creating a set of classes that demonstrate method overriding and polymorphic behavior.
class Shape():
    def area(self):
        raise NotImplementedError("Subclasses must implement this error")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)
