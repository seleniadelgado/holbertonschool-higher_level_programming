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

    def area(self):
        sqr = self.__size * self.__size
        return sqr
