#!/usr/bin/python3
"""
class BaseGeometry / subclass Rectangle
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """calls an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """if > 0 validates"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """rectangle"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def __str__(self):
        """represents a rec using string format"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

