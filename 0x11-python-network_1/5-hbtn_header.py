#!/usr/bin/python3
"""Take in a URL, send a request, and display the val of X-Request-Id"""
import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    r = r.headers.get('X-Request-Id')
    print(r)
