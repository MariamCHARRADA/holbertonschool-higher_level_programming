#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if 'a' <= ch <= 'z':
            print("{}".format(chr(ord(ch) - 32)), end="")
        else:
            print("{}".format(ch), end="")
