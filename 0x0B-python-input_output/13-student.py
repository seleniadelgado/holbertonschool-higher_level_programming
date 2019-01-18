#!/usr/bin/python3
def __init__(self, first_name, last_name, age):
        """defines attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

 def to_json(self, attrs=None):
        if type(attrs) is list:
            dict = {}
            for i in attrs:
                if type(i) is str and i in self.__dict__:
                    dict[i] = self.__dict__.get(i)
            return dict
        else:
            return self.__dict__

def reload_from_json(self, json):
