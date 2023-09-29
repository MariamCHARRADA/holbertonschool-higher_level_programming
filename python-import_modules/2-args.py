#!/usr/bin/python3
from sys import argv
for i in range(1, len(argv) - 1):
    if argv == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
        break
    elif argv == 0:
        print("0 arguments.")
        break
    else:
        print("{} arguments:".format(len(argv)))
        print("{}: {}".format(i, argv[i]))
