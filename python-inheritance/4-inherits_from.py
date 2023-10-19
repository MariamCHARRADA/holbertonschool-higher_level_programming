#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """returns True if the object is exactly an instance of the specified class"""
    issubclass(type(obj), a_class)
