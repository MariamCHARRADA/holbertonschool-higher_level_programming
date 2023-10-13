#!/usr/bin/python3
"""a Square class that defines a square by"""


class Square:
    """
    A class that defines a square
    """

    def __init__(self, size=0):
        """Initializes square size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns square area"""
        return self.__size**2
