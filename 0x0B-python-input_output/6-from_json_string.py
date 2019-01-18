#!/usr/bin/python3
"""function that returns an object (Python Data Structure) represented by a Json
string"""
import json


def from_json_string(my_str):
    return json.loads(my_str)
