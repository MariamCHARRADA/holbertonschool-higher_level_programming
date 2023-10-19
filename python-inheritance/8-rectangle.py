#!/usr/bin/python3

class BaseGeometry:
    
    class Rectangle(BaseGeometry):
        def __init__(self, width, height):
            self.__width = width
            self.__height = height
