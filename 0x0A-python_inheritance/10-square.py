#!/usr/bin/python3
"""defines class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square inherits class Rectangle"""
    def __init__(self, size):
        """
        initializes square

        Args:
            size
        """
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)
