#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is []:
        return my_list
    for c in reversed(my_list):
        print("{:d}".format(c))
