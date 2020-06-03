#!/usr/bin/python3
"""defines class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """init student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dict representation of Student obj"""
        return self.__dict__
