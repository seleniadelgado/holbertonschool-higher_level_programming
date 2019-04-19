#!/usr/bin/python3
"""python script that takes in a letter and sends a POST with letter as parm"""
1
import requests
from sys import argv

if __name__ == "__main__":
    if (len(argv) < 2):
        values = {'q': ""}
    else:
        values = {'q': argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', values)
    try:
        dict_1 = r.json()
        if len(dict_1) == 0:
            print("No result")
        else:
            print("[{}] {}".format(dict_1['id'], dict_1['name']))
    except:
        print("Not a valid JSON")