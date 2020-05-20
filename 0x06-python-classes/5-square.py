#!/usr/bin/python3


class Square:
    """
    Class makes a square
    """

    def __init__(self, size=0):
        """
        initialization of square

        Args:
            size: height/width of square
        """

        self.__size = size

    @property
    def size(self):
        """
          get size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size
        """
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

    def my_print(self):
        """
        prints square using character #
        """
        if self.__size == 0:
            print()
            return
        for n in range(self.__size):
            for n in range(self.__size):
                print("#", end=' ')
            print()
        return
