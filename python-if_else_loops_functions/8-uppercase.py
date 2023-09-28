#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(i) in range(97, 123):
            print("{}".format(chr(ord(i) + 97)))
            i += 1
        else:
            print("{}".format(chr(i)))
