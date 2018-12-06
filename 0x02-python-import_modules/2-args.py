#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)-1
    if args == 1:
        print("{:d} argument:".format(args))
        print("{:d}: {}".format(args, sys.argv[1]))
    if args == 0:
        print("{:d} arguments.".format(args))
    if args >= 2:
        print("{:d} arguments:".format(args))
        for i in range(1, (len(sys.argv))):
            print("{:d}: {}".format(i, sys.argv[i]))
