#!/usr/bin/python3
"""
module :(
"""


def text_indentation(text):
    """splits text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    case = 0
    for a in case:
        if case == 0:
            if a == ' ':
                continue
            else:
                case = 1
        if case == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                case = 0
            else:
                print(a, end="")
