#!/usr/bin/python3
"""takes URL, email address, sends a POST request and displays response"""
import requests
from sys import argv

if __name__ == "__main__":
    values = {'email': argv[2]}
    r = requests.post(argv[1], values)
    print(r.text)
