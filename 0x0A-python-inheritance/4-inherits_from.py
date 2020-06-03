#!/usr/bin/python3
""" contains inherits from function"""


def inherits_from(obj, a_class):
    """ returns True if object is a subclass of a_class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True