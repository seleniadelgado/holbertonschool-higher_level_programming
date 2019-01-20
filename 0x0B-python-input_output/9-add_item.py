#!/usr/bin/python3
import sys
"""that adds all arguments to a Python list, and then save them to a file"""


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
     my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []
args = sys.argv[1:]

for i in args:
    my_list.append(i)
save_to_json_file(my_list, "add_item.json") #writes object to a text file
