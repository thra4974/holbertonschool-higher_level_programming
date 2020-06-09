#!/usr/bin/python3
""" Contains Rectangle Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines Class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructs rectangle"""
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ gets size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets width and height (size) to value"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns string rep of Rectangle"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """assigns argument to each attribute"""
        if len(args) > 0:
            c = 0
            att = ["id", "size", "x", "y"]
            for arg in args:
                setattr(self, att[c], args[c])
                c += 1
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

    def to_dictionary(self):
        """ returns dict representation of Square"""
        square_dictionary = {}
        att = ["id", "size", "x", "y"]
        for name in att:
            square_dictionary[name] = getattr(self, name)
        return square_dictionary
