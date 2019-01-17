#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """checks if it is a kind of class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
