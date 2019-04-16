#!/usr/bin/python3
import urllib.request
from sys import argv
"""Take in a URL, send a request, and display the val of X-Request-Id"""
if __name__ == "__main__":
    url = urllib.request.Request(argv[1])
    with urllib.request.urlopen(url) as response:
        info_dict = dict(response.info())
        value = info_dict.get('X-Request-Id')
        print("{}".format(value))
