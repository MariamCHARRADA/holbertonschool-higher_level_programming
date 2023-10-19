#!/usr/bin/python3
"""creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
