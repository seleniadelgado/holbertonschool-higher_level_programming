#!/usr/bin/python3
class Student():
    """Class student that defines"""

    def __init__(self, first_name, last_name, age):
        """defines attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary rep of student"""
        return self.__dict__
