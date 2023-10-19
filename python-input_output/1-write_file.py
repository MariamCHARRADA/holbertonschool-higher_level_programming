#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
