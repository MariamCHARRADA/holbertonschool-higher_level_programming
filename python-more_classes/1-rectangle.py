#!/usr/bin/python3
'''a class Rectangle that defines a rectangle'''


class Rectangle():
    '''a class Rectangle that defines a rectangle'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
        '''width getter'''
        return self.__width
    
    @width.setter
    def width(self, value):
        '''width setter'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if not value >= 0:
            raise ValueError('width must be >=0')
    
    @property
    def height(self):
        '''height getter'''
        return self.__height
    
    @height.setter
    def height(self, value):
        '''height setter'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if not value >= 0:
            raise ValueError('height must be >=0')
    