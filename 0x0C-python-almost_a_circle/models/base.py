#!/usr/bin/python3
"""base class"""
import json


class Base():
    """Class called base with different methods that have an effect on
    subclasses when called."""

    __nb_objects = 0

    def __init__(self, id=None):
        """defining a cls constructor with private cls attribute. (Task 1)"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the json representation of list_dictionaries. (Task 15)"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON str rep of list_objs to a file. (Task 16)"""
        dictobj_list = []
        for obj in list_objs:
            dictobj_list.append(obj.to_dictionary())
        strobj = Base.to_json_string(dictobj_list)
        with open("{}.json".format(cls.__name__), "w+", encoding="utf-8") as f:
            f.write(strobj)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON str rep of json_string. (Task 17)"""
        empty_list = []
        if json_string is None or not json_string:
            return empty_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set with "dummy"
        instances. (Task 18)"""
        dummy1 = cls(1, 2, 3)
        dummy1.update(**dictionary)
        return dummy1

    @classmethod
    def load_from_file(cls):
        """Updates Base class by adding a class method which returns a list of
           instances. (Task 19)"""
        list_instances = []
        try:
            jstring = cls.__name__ + ".json"
            with open(jstring, "r", encoding="utf-8") as jfile:
                rfile = jfile.read()
            list_dict = Base.from_json_string(rfile)
            for i in list_dict:
                list_instances.append(cls.create(**i))
            return list_instances
        except FileNotFoundError:
            return list_instances
