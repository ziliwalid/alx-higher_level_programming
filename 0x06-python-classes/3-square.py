#!/usr/bin/python3
"""describes a class Square"""


class Square:
    """square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """init the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
    def area(self):
        """calculates the area according to the args
        Returns:
            The area of the square
        """
        return (self.__size) ** 2
