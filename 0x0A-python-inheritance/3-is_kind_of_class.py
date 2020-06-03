#!/usr/bin/python3
""" contains iskindofclass function"""


def is_kind_of_class(obj, a_class):
    """ returns true if object is kind of an instance of class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
