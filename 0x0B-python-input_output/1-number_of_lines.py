#!/usr/bin/python3
"""function that returns a number of lines of a text file"""


def number_of_lines(filename=""):
    with open(filename, "r") as f:
        return len(f.readlines())
