#!/usr/bin/python3
"""importing from rectangle, class that inherits from rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """new class Square inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class that inherits from Rectangle, calls the super class"""
        width = size
        height = size
        self.__size = size
        super().__init__(width, height, x, y, id)
        self.__width = size
        self.__height = size

    def __str__(self):
        """override what str prints in parent class to a str about Square."""
        return "[Square] {} {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """setter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """gets the value for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.__height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """method that updates the values of each instance
        as values are passed in"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        if len(args) is 0 or args is None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """public method which returns the
        dictionary representation of a Square"""
        return {"id":  self.id, "size": self.size, "x": self.x, "y": self.y}
