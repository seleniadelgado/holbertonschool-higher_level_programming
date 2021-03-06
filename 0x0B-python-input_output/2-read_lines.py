#!/usr/bin/python3
"""function that reads n lines of a text file and prints them"""


def read_lines(filename="", nb_lines=0):
    with open(filename, 'r') as f:
        lines = len(f.readline())
        f.seek(0)
        if nb_lines <= 0 or nb_lines >= lines:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
