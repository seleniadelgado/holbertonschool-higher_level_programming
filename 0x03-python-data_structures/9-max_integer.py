#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return
    my_list.sort()
    return my_list[-1]
