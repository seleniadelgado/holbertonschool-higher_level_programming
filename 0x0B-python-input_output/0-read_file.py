#!/usr/bin/python3
"""function reads a text filr and prints it to stdout"""


def read_file(filename=""):
    with open(filename, 'r') as f:
        print(f.read(), end="")
