#!/usr/bin/python3
"""
class BaseGeometry / subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """rectangle"""
    def __init__(self, width, height):
        """instantiation of the rec"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
