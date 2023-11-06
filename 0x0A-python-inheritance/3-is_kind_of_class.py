#!/usr/bin/python3
"""
is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """True if object is instance or inherited from a_class"""
    return (isinstance(obj, a_class))
