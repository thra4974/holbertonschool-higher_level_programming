#!/usr/bin/python3
"""defines class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """init student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict representation of Student obj"""
        if attrs is None or type(attrs) != list:
            return self.__dict__
        for n in attrs:
            if type(n) != str:
                return self.__dict__
        attrlist = {a: self.__dict__[a] for a in self.__dict__ if a in attrs}
        return attrlist
