#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    if args == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    elif args == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(args - 1))
        for i in range(1, args):
            print("{}: {}".format(i, argv[i]))
