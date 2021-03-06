#!/usr/bin/python3
"""defines a Class: rectangle """


class Rectangle:
    """ rectangle w/ priv instance attributes width and height """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializing a Rectangle
        Args:
            size: height/width of rectangle
        """
        Rectangle.number_of_instances += 1
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
        returns informal string intepretation of rectangle
        """
        str_rectangle = ""
        if self.width == 0 or self.height == 0:
            return str_rectangle
        for n in range(self.height):
            str_rectangle += str(self.print_symbol) * self.width
            if n < self.height - 1:
                str_rectangle += "\n"
        return str_rectangle

    def __repr__(self):
        """
        returns formal interpretation of rectangle
        """
        repr_str = "Rectangle({:d}, {:d})".format(self.width, self.height)
        return repr_str

    def __del__(self):
        """
        deletes an instance of a rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        return rectangle with largest area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        return rect as a square
        """
        new_rect = cls(size, size)
        return new_rect
