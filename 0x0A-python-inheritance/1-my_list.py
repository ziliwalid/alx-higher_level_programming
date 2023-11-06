#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """subclass"""
    def __init__(self):
        """inits the pbject"""
        super().__init__()

    def print_sorted(self):
        """prints"""
        print(sorted(self))
