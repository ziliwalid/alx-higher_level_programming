#!/usr/bin/python3
"""class Student."""


class Student:
    """student"""

    def __init__(self, first_name, last_name, age):
        """Init student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dict of student with args
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict_
