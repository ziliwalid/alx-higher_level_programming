#!/usr/bin/python3
"""
function "wrtie_file"
"""


def write_file(filename="", text=""):
    """returns the num of chars"""
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
