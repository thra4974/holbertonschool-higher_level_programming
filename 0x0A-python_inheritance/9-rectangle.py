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
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height

            def area
