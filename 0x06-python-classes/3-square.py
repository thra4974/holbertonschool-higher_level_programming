#!/usr/bin/python3


class Square:
    """ square w/private instance atr size """

    def __init__(self, size=0):
        """
        initialize square

        Args:
            size: size of width/height of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        elif not type(size) is int:
            raise TypeError("size must be an integer")

    def area(self):
        """
        get area of square

        Returns:
            area of square
        """

        return self.__size**2
