#!/usr/bin/python3
"""creating a square class"""


class Square():
    """class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            raise TypeError
        elif value < 0:
            print("size must be >= 0")
            raise ValueError
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        if len(value) != 2:
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        if type(value[0]) is not int or type(value[1]) is not int:
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        if value[0] < 0 or value[1] < 0:
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        elif self.size > 0:
            for n in range(self.__position[1]):
                print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            print()

    def area(self):
        return(self.size * self.size)
