#!/usr/bin/python3
"""create a function that returns a rep of pascal triangle of n"""


def pascal_triangle(n):
    dlist = []
    uno = 1
    if n <= 0:
        return dlist
    for row in range(n):
        items = []
        for i in range(0, row + 1):
            if i == 0 or i == row or row == 0:
                items.append(uno)
            else:
                items.append(dlist[row - 1][i] + dlist[row - 1][i - 1])
        dlist.append(items)
    return dlist
