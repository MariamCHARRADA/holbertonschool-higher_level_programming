#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
