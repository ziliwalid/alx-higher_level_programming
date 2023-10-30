#!/usr/bin/python3
"""
class rectangle
"""


class Rectangle:
    """rectangle"""
    def __init__(self, width=0, height=0):
        """Init rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for private instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for  height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
    """Returns a printable string representation of rectangle"""
    if self.__width != 0 and self.__height != 0:
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])
    else:
        return ''
    
    def __repr__(self):
        """does magic"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

