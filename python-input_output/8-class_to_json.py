#!/usr/bin/python3
"""creates an Object from a “JSON file”"""


def class_to_json(obj):
    """returns the JSON representation of an object (string)"""
    return obj.__dict__
