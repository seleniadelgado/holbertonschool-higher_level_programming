#!/usr/bin/python3
"""imports from BaseGeometry"""

Rectangle = __import__('9-rectangle').Rectangle
"""inherits from BaseGeometry"""


class Square(Rectangle):
    """new class with inheritance"""

    def __init__(self, size):
        """makes a new rectangle validating it's sides"""
        self.integer_validator("size", size)
        self.__size = size
        self._Rectangle__width = size
        self._Rectangle__height = size

    def area(self):
        """defining area of a rectangle"""
        return self.__size * self.__size
