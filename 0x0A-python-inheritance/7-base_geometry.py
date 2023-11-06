#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """contains some methods"""
    def area(self):
        """calls an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """if > 0 validates it"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
