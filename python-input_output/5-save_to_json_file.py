#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
