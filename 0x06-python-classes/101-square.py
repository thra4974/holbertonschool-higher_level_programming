#!/usr/bin/python3

"""define a class Square"""


class Square:
    """
    class makes a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initialization of square
        Args:
            size: height/width of square
            position: position of square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        get position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        set position

        Args:
            value: position square
        """
        if type(value) is not tuple or len(value) != 2 or\
           type(value[0]) is not int or value[0] < 0 or\
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        get area of square
        """
        return self.__size**2

    def my_print(self):
        """
        prints square using character hash
        """
        if self.__size == 0:
            print("")
            return
        for n in range(self.position[1]):
            print()
        for n in range(self.__size):
            for n in range(self.__position[0]):
                print("{}".format(" "), end="")
            for n in range(self.__size):
                print("{}".format("#"), end="")
            print("")
        return

    def __str__(self):
        """
        returns string representation of square
        """
        strrep = ""
        if self.__size == 0:
            return strrep
        strrep += '\n' * self.__position[1]
        for n in range(self.__size):
            strrep += " " * self.__position[0]
            strrep += "#" * self.__size
            if n < self.__size - 1:
                strrep += "\n"
        return strrep
