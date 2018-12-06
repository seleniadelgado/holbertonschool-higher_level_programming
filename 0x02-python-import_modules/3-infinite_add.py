#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)-1
    if args == 0:
        print("0")
    elif args == 1:
        print(sys.argv[1])
    else:
        sum = 0
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])
        print("{}".format(sum))
