#!/usr/bin/python3
'''
Write a class Square that defines a square by:

- Private instance attribute: size:
    - property def size(self): to retrieve it
    - property setter def size(self, value): to set it:
        - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
        - if size is less than 0, raise a ValueError exception with the message size must be >= 0
- Private instance attribute: position:
    - property def position(self): to retrieve it
    - property setter def position(self, value): to set it:
        - position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
- Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
- Public instance method: def area(self): that returns the current square area
- Public instance method: def my_print(self): that prints in stdout the square with the character #:
    - if size is equal to 0, print an empty line
    - position should be use by using space - Don’t fill lines by spaces when position[1] > 0
'''
class Square:
    '''A class that defines a square '''
    def __init__(self, size=0, position=(0, 0)):
        '''initialize square size and position'''
        self.__size = size
        self.__position = position

    @property    
    def position(self):
        '''position getter'''
        return self.__position
    
    @position.setter
    def position(self, value):
        '''position setter'''
        if (not isinstance(value, tuple) or len(value)!=2 or
            any(isinstance(i, int) for i in value) or
            any(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        '''prints in stdout the square with the character #'''
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(f"{' ' * self.__position[0]}{'#' * self.__size}")
