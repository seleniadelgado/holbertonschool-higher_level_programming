#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for j in range(len(my_string)):
        if my_string[j] == "c" or my_string[j] == "C":
            continue
        else:
            newstring = newstring + my_string[j]
    return newstring
