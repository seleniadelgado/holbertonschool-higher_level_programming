#!/usr/bin/python3
"""importing from from base"""
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """defining private instance attributes, each with its own publis getter
        and setter. (Task 2, 3)"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        self.__Rect_id = super().__init__(id)

    @property
    def width(self):
        """getter for private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """setter for private instance height"""
        return self.__height

    @height.setter
    def height(self):
        """setter for private instance height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for private instance x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for private instance x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for private instance y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for private instance y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """public method that returns the area of the Rectangle instance.
        (Task 4)"""
        return self.__width * self.__height

    def display(self):
        """public method that prints in stdout the Rectangle instance with the
        char # also updates the rectangle to handle x and y. (Task 5, 7)"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding the str method so it returns something else.(Task 6)"""
        return "[Rectangle] {} {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updating the Rectangle cls by adding this public method.(Task 12)"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]
        if len(args) is 0 or args is None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Update the class Rectangle by adding the public method to
        return the dictionary representation of a Rectangle. (Task 13)"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
