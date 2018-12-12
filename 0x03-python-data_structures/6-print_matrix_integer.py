#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = 0
    i = 0
    for a in range(len(matrix)):
        for i in range(len(matrix[a])):
            if i == len(matrix[i]) - 1:
                print("{:d}".format(matrix[a][i]), end="")
            if i < len(matrix[i]) - 1:
                print("{:d}".format(matrix[a][i]), end=" ")
        print("")
