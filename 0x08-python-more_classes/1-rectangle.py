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
            if value <= 0:
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
            if value <= 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")
