#!/usr/bin/python3
'''
A class that defines a square by:
- Private instance attribute: size:
    - property def size(self): to retrieve it
    - property setter def size(self, value): to set it:
        - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
        - if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Instantiation with optional size: def __init__(self, size=0):
- Public instance method: def area(self): that returns the current square area
'''
class Square():
    '''
    A class that defines a square 
    '''
    def __init__(self, size=0):
        '''initialize square size'''
        if type(size)!= int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        '''size getter'''
        return self.__size
    
    @size.setter
    def size(self, value):
        '''size setter'''
        if type(value)!= int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        '''returns square area'''
        return self.__size ** 2
