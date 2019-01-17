#!/usr/bin/python3
"""imports from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """new class with inheritance"""

    def __init__(self, width, height):
        """makes a new rectangle validating it's sides"""
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height

    def __str__(self):
        """defining str to print"""
        s = ""
        s = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return s

    def area(self):
        """defining area of a rectangle"""
        return self.__height * self.__width
