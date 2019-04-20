#!/usr/bin/python3
"""takes github credentials usrnme & psswrd & uses github to display ur id)"""
import requests
from sys import argv
if __name__ == "__main__":
     username = argv[1]
     password = argv[2]
     u = requests.get('https://api.github.com/user', auth=(username,password))
     if u.status_code == 200:
         u = u.json()
         print("{}".format(u['id']))
     else:
         print("None")
