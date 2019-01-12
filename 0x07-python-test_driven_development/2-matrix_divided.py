#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    a = "matrix must be a matrix (list of lists) of integers/floats"
    b = "each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(a)
        for box in matrix:
            if type(box) is not list:
                raise TypeError(a)
    if len(matrix) > 1:
        row = len(matrix[0])
        for rows in matrix:
            if len(rows) is not row:
                raise TypeError(b)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for a in matrix:
        littlelist = []
        for b in a:
            if type(b) is not int and type(b) is not float:
                raise TypeError(a)
            result = b / div
            result = round(result, 2)
            littlelist.append(result)
        new_matrix.append(littlelist)
    return (new_matrix)
