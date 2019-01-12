#!/usr/bin/python3
"""defining a class"""


class Rectangle:

    def __init__(self, width=0, height=0):
        """defining init and objects"""
        self.width = width
        self.height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """defining the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """defining width with new value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must >= 0")
        self.__width = value

    @property
    def height(self):
        """defining height"""
        return self.__height

    @height.setter
    def height(self, value):
        """defining height with value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """defining area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """defining perimeter of rectangle"""
        if self.__height == 0 or if self.width == 0
            return 0
        return 2 * (self.__height + self.__width)
