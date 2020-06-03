#!/usr/bin/python3
"""contains add_attribute function"""


def add_attribute(my_obj, name, new_val):
    """ adds new attribute to an object if possible"""

    if not hasattr(my_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        hasattr(my_obj, '__dict__')
        setattr(my_obj, name, new_val)
