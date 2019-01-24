#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """class inherits from rectangle"""


    def __init__(self, size, x=0, y=0, id=None):
        width = size
        height = size
        super().__init__(width, height, x, y, id)
        self.__width = size
        self.__height = size

    def __str__(self):
        return "[Square] {} {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
 
