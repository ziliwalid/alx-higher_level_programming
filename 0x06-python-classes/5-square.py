#!/usr/bin/python3
"""describes a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of square's side
    """
    def __init__(self, size=0):
        """init square
        Args:
            size (int): size of square's side
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates the square's area
        Returns:
            The square's area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The square's side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a square's side
        Returns:
            nada
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
    
    def my_print(self):
        """square printing
        Returns:
            nada, just like in betty XD
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))

                
