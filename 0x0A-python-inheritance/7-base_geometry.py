#!/usr/bin/python3
class BaseGeometry():
    """BaseGeometry new class"""

    def area(self):
        """def area, area is not defined"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """testing string and value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
