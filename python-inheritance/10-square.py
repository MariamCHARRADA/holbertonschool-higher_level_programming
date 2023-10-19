#!/usr/bin/python3
"""BaseGeography class"""


class BaseGeometry:
    """BaseGeography class"""

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """initialize square size"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """initialize square size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''returns square area'''
        return self.__size ** 2
