#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """MyList class that inherits from list"""
    def print_sorted(self):
        """prints in stdout the sorted list"""
        print(sorted(self))
