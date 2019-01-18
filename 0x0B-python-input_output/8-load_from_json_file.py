#!/usr/bin/python3
import json
"""function that creates an Object from "JSON file"""


def load_from_json_file(filename):
    with open(filename) as f:
        return json.load(f)
