#!/usr/bin/python3
""" Contains Rectangle Module"""
from models.base import Base


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
        """sets width to value and validates size and type"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height and validates type and size"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x to value and validates size and type"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y value and validates size and type"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of Rectangle instance"""
        return self.width * self.height

    def display(self):
        """ prints Rectangle instance with #"""
        print("\n" * self.y, end="")
        for n in range(self.height):
            print(" " * self.x, end="")
            for n in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returns string rep of Rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns argument to each attribute"""
        if len(args) > 0:
            c = 0
            att = ["id", "width", "height", "x", "y"]
            for arg in args:
                setattr(self, att[c], args[c])
                c += 1
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)
