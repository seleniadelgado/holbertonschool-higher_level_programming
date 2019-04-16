#!/usr/bin/python3
import urllib.request
from sys import argv
"""Takes URL and prints out response"""

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as a:
        a = a.read()
        print("Body response:")
        print("\t- type: {}".format(type(a)))
        print("\t- content: {}".format(a.decode("utf8")))
