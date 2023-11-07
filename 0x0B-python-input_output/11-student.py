#!/usr/bin/python3
"""
Contains the clas "Student"
"""


class Student:
    """student"""
    def __init__(self, first_name, last_name, age):
        """Init student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dict of student with args"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                nDict[a] = self.__dict__[a]
            except FileNotFoundError:
                pass
        return nDict

    def reload_from_json(self, json):
        """replaces all attr"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
