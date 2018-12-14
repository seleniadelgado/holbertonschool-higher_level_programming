#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = {}
    list2 = list(a_dictionary.keys())
    for v in range(0, len(list2)):
        items = list2[v]
        newdict[items] = a_dictionary.get(items) * 2
    return newdict
