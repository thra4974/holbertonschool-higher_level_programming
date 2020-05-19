#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
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
        return self.__size**2
