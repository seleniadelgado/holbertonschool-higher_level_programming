#!/usr/bin/python3
import requests
from sys import argv
"""Take in a URL, send a request, and display the val of X-Request-Id"""
if __name__ == "__main__":
    r = requests.get(argv[1])
    r = r.headers['X-Request-Id']
    print("{}".format(r))
