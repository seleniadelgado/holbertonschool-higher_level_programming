#!/usr/bin/python3
"""imports Rectangle(9-rectangle.py)"""

Rectangle = __import__('9-rectangle').Rectangle
"""inherits from Rectangle"""


class Square(Rectangle):
    """new class with inheritance"""

    def __init__(self, size):
        """instantiation of module"""
        self.integer_validator("size", size)
        self.__size = size
        self._Square__width = size
        self._Square__height = size

    def __str__(self):
        """str to define a string"""
        s = ""
        s = "[Square] {}/{}".format(self.__width, self.__height)
        return s

    def area(self):
        """str to define the area of the square"""
        return self.__width * self.__height
