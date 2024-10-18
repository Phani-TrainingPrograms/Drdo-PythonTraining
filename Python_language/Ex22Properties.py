#@property = Decorator used to define a method as a property(member that can be accessed like an
# attribute)
# Advantage: U can create accessors to the private members like getters and setters. In Python,
# U can also have deleters where U can remove a property at runtime. This is typically done when
# U dont want to expose the property after some operations are done.

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return f"{self.__width:.2f} cm²"

    @property
    def height(self):
        return f"{self.__height:.2f} cm²"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print("Width must be greater than Zero(0)")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("Width must be greater than Zero(0)")


rectangle = Rectangle(20, 30)
print(rectangle.width)
print(rectangle.height)
rectangle.height = 56.56
