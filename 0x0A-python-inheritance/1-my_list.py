#!/usr/bin/python3
class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """prints sorted list"""
        a = sorted(self)
        print(a)
