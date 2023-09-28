#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(i) in range(97, 123):
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print("{}".format(chr(i)), end="")
