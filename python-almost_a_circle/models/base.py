#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        json_string = "[]"
        if len(list_dictionaries) > 0:
            json_string = json.dumps(list_dictionaries)
        return json_string
