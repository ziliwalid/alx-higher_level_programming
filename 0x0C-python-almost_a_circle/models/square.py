#!/usr/bin/python3
"""represents square and inherits"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """representing a square, inheriting from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Inits new square

        Args:
            size (int): The size of the new Square
            x (int): The x coordinate of the new Square
            y (int): The y coordinate of the new Square
            id (int): The identity of the new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """settter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates square"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """gets a representation for square data in a dict"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """return a human-readable representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

