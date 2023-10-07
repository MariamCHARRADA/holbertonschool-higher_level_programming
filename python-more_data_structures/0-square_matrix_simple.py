#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[x * x for x in row] for row in matrix]
    return new
