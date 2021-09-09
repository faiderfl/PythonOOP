#Liskov Substituion Principle: 
#Let φ(x) be a property provable about objects x of type T. Then φ(y) should be true for objects y of type S where S is a subtype of T.
#if we have a base class T and subclass S, you should be able to substitute the main class T with the subclass S without breaking the code.

class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

    def get_area(self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
    @Rectangle.width.setter
    def width(self, value):
        self._width = value
        self._height = value
    @Rectangle.height.setter
    def height(self, value):
        self._width = value
        self._height = value

def get_squashed_height_area(Rectangle):
    Rectangle.height = 1
    area = Rectangle.get_area()
    return area

rectangle = Rectangle(5, 5)
square = Square(5)
assert get_squashed_height_area(rectangle) == 5  # expected 5
assert get_squashed_height_area(square) == 1  # expected 5