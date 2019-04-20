#!/usr/bin/python3
"""Takes a string and sends a search request to Star Wars API"""
import requests
from sys import argv

if __name__ == "__main__":
    search = argv[1]
    u = requests.get('https://swapi.co/api/people/', params={'search': search})
    search = u.json()
    print("Number of results: {}".format(search['count']))
    for person in search['results']:
        print("{}".format(person ['name']))
