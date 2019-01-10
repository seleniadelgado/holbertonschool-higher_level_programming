#!/usr/bin/python3
class Rectangle():

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """defining init and objects"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
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
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """defining height"""
        return self.__height

    @height.setter
    def height(self, value):
        """defining height with new value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """defining area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """defining perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.width)

    def __str__(self):
        """defining str to print # in rectangle"""
        s = ""
        s = s.join((self.__height - 1) * (s + str(
            self.print_symbol) * self.__width + "\n"))
        s += str(self.print_symbol) * self.__width
        return s

    def __repr__(self):
        """defining repr to print string"""
        return "Rectangle (" + str(
            self.__width) + "," + str(self.__height) + ")"

    def __del__(self):
        """defining del"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """defining rectangle to get largest area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        uno = rect_1.area()
        dos = rect_2.area()
        if uno == dos or uno > dos:
            return rect_1
        if dos > uno:
            return rect_

    @classmethod
    def square(cls, size=0):
        """defining a rectangle with size to equal 0"""
        return Rectangle(size, size)
