#!/usr/bin/python3
"""
inherits_from function
"""


def inherits_from(obj, a_class):
    """true if object is a subclass of a_class"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
