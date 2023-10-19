#!/usr/bin/python3
""" returns a list of lists of integers"""


def pascal_triangle(n):
    """returns a list of lists of integers"""
    a_list = []
    row = [1]
    for i in range(n):
        a_list.append(row)
        row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]

    return a_list
