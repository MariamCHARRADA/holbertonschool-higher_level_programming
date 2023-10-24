#!/usr/bin/python3
"""
Defines Rectangle that inherits from Base
"""

import sys

sys.path.append("c:/holbertonschool-higher_level_programming\python-almost_a_circle")
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor"""
        __width = width
        __height = height
        __x = x
        __y = y
        super().__init__(id)


@property
def width(self):
    """width getter"""
    return self.__width


@width.setter
def width(self, value):
    """width setter"""
    self.__width = value


@property
def height(self):
    """height getter"""
    return self.__height


@height.setter
def height(self, value):
    """height setter"""
    self.__height = value


@property
def x(self):
    """x getter"""
    return self.__x


@x.setter
def x(self, value):
    """x setter"""
    self.__x = value


@property
def y(self):
    """y getter"""
    return self.__y


@y.setter
def y(self, value):
    """y setter"""
    self.__y = value
