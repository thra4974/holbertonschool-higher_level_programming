#!/usr/bin/python3
""" contains iskindofclass function"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
