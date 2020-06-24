#!/usr/bin/python3
"""defines class Square"""


class Square:
    """
    square with private instance atr size
    """
    def __init__(self, size=0):
        """
        initialize square

        Args:
            size: size of width/height of square
        """
        self.__size = size

    @property
    def size(self):
        """
        checks type of size and value
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        elif not type(value) is int:
            raise TypeError("size must be an integer")

    def area(self):
        """
        get area of square
        """
        return self.__size**2
