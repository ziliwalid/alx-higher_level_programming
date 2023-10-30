#!/usr/bin/python3
"""
class rectangle
"""


class Rectangle:
    """rectangle"""
     number_of_instances = 0
     print_symbol = "#"

     @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """biggest rect"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """Init rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
    
    def __del__(self):
        """prints something when rec is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        """prints rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string
    
    def __repr__(self):
        """does magic"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints something when rec is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


        

