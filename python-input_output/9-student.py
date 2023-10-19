#!/usr/bin/python3
"""Write a class Student that defines a student”"""


class Student:
    """A class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializes a new Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """returns the JSON representation of a Student instance"""
        return self.__dict__
