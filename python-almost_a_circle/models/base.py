#!/usr/bin/python3
"""Base class"""


class Base:
    """Base class"""

    def __init__(self, id=None):
        """Base class constructor"""
        __nb_objects = 0
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
