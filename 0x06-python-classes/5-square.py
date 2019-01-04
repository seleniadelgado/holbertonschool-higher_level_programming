#!/usr/bin/python3
class Square():
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            print("Size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("Size must be >= 0", end="")
            raise ValueError

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
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

    def area(self):
        return (self.size * self.size)
