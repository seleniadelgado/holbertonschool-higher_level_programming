#!/usr/bin/python3
import requests
"""Takes URL and prints out response"""
if __name__ == "__main__":
    a = requests.get('https://intranet.hbtn.io/status')
    p = a.text
    print("Body response:")
    print("\t- type: {}".format(type(p)))
    print("\t- content: {}".format(p))
