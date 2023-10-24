#!/usr/bin/python3
"""Square
this modules describes class quare
"""


class Square():
    """describing square"""

    def __init__(self, size=0, position=(0, 0)):
        """constructor

        Args:
            size (int):  size of one esquare's edge
            position (tuple): square's data (coordinates)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """the size of a square's side"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Getter or setter of square's position"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) is 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """gets the square's area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square using #"""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
