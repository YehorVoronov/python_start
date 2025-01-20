# @property = Decorator used to define a method as a property (can be accessed like an attribute)
# benefit: add additional logic when read, write, or delete attributes
#  gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
# getter method
    @property
    def width(self):
        return f"{self._width:.2f}"

    @property
    def height(self):
        return f"{self._height:.2f}"
# setter method    
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("width should be grater than 0")

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("should be grater than 0")
# delete method    
    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted ")
    
    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted ")

rectangle = Rectangle(3, 5)
rectangle.width = 0
rectangle.width = 8

# del rectangle.width
# del rectangle.height


print(rectangle.width, rectangle.height)