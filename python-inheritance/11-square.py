#!/usr/bin/python3
"""Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """initialize square size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns square area"""
        return self.__size**2

    def __str__(self):
        """returns square description"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
