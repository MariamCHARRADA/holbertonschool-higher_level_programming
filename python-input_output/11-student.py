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

    def to_json(self, attrs=None):
        """returns the JSON representation of a Student instance"""
        if attrs is not None:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all Student attributes with those in json"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
