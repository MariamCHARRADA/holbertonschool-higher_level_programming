#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = list(set_1 - set_2)
    difff = list(set_2 - set_1)
    return diff + difff
