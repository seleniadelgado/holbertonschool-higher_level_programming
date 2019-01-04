#!/usr/bin/python3
class Square ():
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError
            print("size must be an integer")
        elif size < 0:
            raise ValueError
            print("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = value

    def area(self):
        return (self.__size * self.__size)
