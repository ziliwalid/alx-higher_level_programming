#!/usr/bin/python3
"""
function append_write
"""


def append_write(filename="", text=""):
    """returns num of chars added"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
