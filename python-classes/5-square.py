#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 4-square.py)

- Private instance attribute: size:
   - property def size(self): to retrieve it
   - property setter def size(self, value): to set it:
       - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
       - if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Instantiation with optional size: def __init__(self, size=0):
- Public instance method: def area(self): that returns the current square area
- Public instance method: def my_print(self): that prints in stdout the square with the character #:
    - if size is equal to 0, print an empty line
"""


class Square:
    """
    A class that defines a square
    """

    def __init__(self, size=0):
        """initialize square size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns square area"""
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(f"{'#' * self.__size}")
