#!/usr/bin/python3
for a in range(1, 90):
    if a < 10:
        print("{:02d}, ".format(a), end='')
    if a == 89:
        print("{}".format(a))
    else:
        num1 = a / 10
        num2 = a % 10
        if num1 < num2 and a > 10:
            print("{:02d}, ".format(a), end='')
