#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnum = number % 10
print("Last digit of {} is".format(number), end=" ")
if number >= 0:
    if lastnum > 5:
        print("{} and is greater than five".format(lastnum))
    elif lastnum == 0:
        print("{} and is 0".format(lastnum))
    elif lastnum < 6 and lastnum != 0:
        print("{} and is less than 6 and not 0".format(lastnum))
elif number < 0:
    negnum = (((number * -1) % 10)*-1)
    print("{} and is less than 6 and not 0".format(negnum))
