#!/usr/bin/python3
def no_c(my_string):
    string = my_string.translate({ord('c'): ''})
    string = string.translate({ord('C'): ''})
    return string
    