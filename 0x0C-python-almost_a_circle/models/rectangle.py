#!/usr/bin/python3
""" Contains Rectangle Module"""
Base = __import__('base.py').Base


class Rectangle(Base):
    """defines Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructs rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width to value"""
        self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        self.__height = value

    @property
    def x(self):
        """gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x to value"""
        self.__x = value

    @property
    def y(self):
        """ gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y value"""
        self.__y = value
