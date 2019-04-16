#!/usr/bin/python3
"""takes in a URL sends request to URL and displays body of the response."""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as a:
            a = a.read()
            print("{}".format(a.decode("utf8")))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
