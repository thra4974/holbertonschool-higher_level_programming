#!/usr/bin/python3
"""defines a Class: rectangle """


class Rectangle:
    """ rectangle w/ priv instance attributes width and height """
    def __init__(self, width=0, height=0):
        """
        initializing a Rectangle
        Args:
            size: height/width of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """
        get height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set height
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """
        get width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set width
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    def area(self):
        """
        get area of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width*self.__height

    def perimeter(self):
        """
        get perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*self.__width + 2*self.__height

    def __str__(self):
        """
        returns string intepretation og rectangle
        """
        str_rectangle = ""
        if self.width == 0 or self.height == 0:
            return str_rectangle
        for n in range(self.height):
            str_rectangle += "#" * self.width
        return str_rectangle
