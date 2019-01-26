#!/usr/bin/python3
import json

class Base():
    """base called class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """defining a class called Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the json representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        dictobj_list = []
        for obj in list_objs:
            dictobj_list.append(obj.to_dictionary())
        strobj = Base.to_json_string(dictobj_list)
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(strobj)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        empty_list = []
        if json_string is None or not json_string:
            return empty_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy1 = cls(1, 2, 3)
        dummy1.update(**dictionary)
        return dummy1

    @classmethod
    def load_from_file(cls):
        """Updates Base class by adding the class method that returns a list of
           instances"""
        list_instances = []
        if not "{}.json".format(cls.__name__):
            return list_instances
        jstring = cls.__name__ + ".json"
        with open (jstring, "r", encoding="utf-8") as jfile:
            rfile = jfile.read()
            list_dict = Base.from_json_string(rfile)
        for i in list_dict:
            list_instances.append(cls.create(**i))
        return list_instances
