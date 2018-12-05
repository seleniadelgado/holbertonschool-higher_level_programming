#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        string = ord(str[i])
        if string >= 97 and string <= 122:
            string = string - 32
        print("{}".format(chr(string)), end="")
    print("")
