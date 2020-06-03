#!/usr/bin/python3
"""defines class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class rectangle
    """
    def __init__(self, width, height):
        """
        initializes rectangle

        Args:
            width/ height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """are of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ return string rep of Rect"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
