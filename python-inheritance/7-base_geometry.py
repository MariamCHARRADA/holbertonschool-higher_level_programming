#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """BaseGeography class"""

    def area(self):
        """public method to raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public method that validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
