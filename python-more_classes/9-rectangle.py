#!/usr/bin/python3
'''a class Rectangle that defines a rectangle '''


class Rectangle:
    '''a class Rectangle that defines a rectangle'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''initialize height and width'''
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        '''prints rectangle with print_symbol'''
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = (str(self.print_symbol) *
                     self.width + '\n') * (self.height - 1)
        rectangle += str(self.print_symbol) * self.width
        return rectangle

    def __repr__(self):
        '''returns string representing the rectangle'''
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        '''print message when an instance is deleted'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''returns the biggest rectangle based on the area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
