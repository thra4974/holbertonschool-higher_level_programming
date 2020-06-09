#!/usr/bin/python3
""" Contains Base module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json rep of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
