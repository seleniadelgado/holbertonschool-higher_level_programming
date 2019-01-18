#!/usr/bin/python3
"""function that writes a string to a text file and returns the number of chars
written"""
def write_file(filename="", text=""):
    with open(filename, 'w+') as f:
        return f.write(text)
