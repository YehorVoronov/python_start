# super() = function in a child class to call method from a parent class (superclass).
#  allows you to extend the functionality of the inherited method

class Shape:
    def __init__(self, color, filled,):
        self.color = color
        self.filled = filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else "not filled" }")


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius
    def describe(self):
        print(f"It is a circle with a radius: {self.radius} ")
        super().describe()


class Square(Shape):
     def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

class Triangle:
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

circle = Circle("red", True, 22)
square = Square("red", True, 12)
print(circle.color)
circle.describe()
square.describe()