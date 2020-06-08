#!/usr/bin/python3
""" Contains Base module"""


class Base:
    """defines class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructs Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
