#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        neg = number * -1
    else:
        neg = number
    ld = neg % 10
    print("{:d}".format(ld), end="")
    return (ld)
