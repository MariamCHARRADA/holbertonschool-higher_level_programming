#!/usr/bin/python3
'''a class Rectangle that defines a rectangle '''


class Rectangle:
    '''a class Rectangle that defines a rectangle'''

    def __init__(self, width=0, height=0):
        '''initialize height and width'''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''gets the rectangle width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the rectangle width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >=0')
        else:
            self.__width = value

    @property
    def height(self):
        '''gets the rectangle height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the rectangle height'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >=0')
        else:
            self.__height = value

    def area(self):
        '''returns the rectangle area'''
        return self.width * self.height

    def perimeter(self):
        '''returns the rectangle perimeter'''
        if not (self.width == 0 or self.height == 0):
            return 2 * (self.width + self.height)
        else:
            return 0

    def __str__(self):
        '''prints rectangle with character #'''
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ('#' * self.width + '\n') * (self.height - 1)
        rectangle += '#' * self.width
        return rectangle
