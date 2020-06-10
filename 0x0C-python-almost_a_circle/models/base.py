#!/usr/bin/python3
""" Contains Base module"""
import json
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string rep of list_onbjs to a file"""
        buf_list = []
        class_name = cls.__name__
        json_ext = ".json"
        filename = class_name + json_ext
        if list_objs is not None:
            for obj in list_objs:
                buf_list.append(obj.to_dictionary())
        with open(filename, "w+", encoding="utf-8") as f:
            f.write(cls.to_json_string(buf_list))

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON string rep"""
        buf_list = []
        if json_string is None:
            return buf_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dumbass = cls(1, 5)
        elif cls.__name__ == "Square":
            dumbass = cls(5)
        cls.update(dumbass, **dictionary)
        return dumbass

    @classmethod
    def load_from_file(cls):
        """ returns list of instances"""
        buf_list = []
        class_name = cls.__name__
        json_ext = ".json"
        filename = class_name + json_ext
        with open(filename, 'r', encoding="utf-8") as f:
            buf_list = cls.from_json_string(f.read())
            for i in range(len(buf_list)):
                buf_list[i] = cls.create(**buf_list[i])
        return buf_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        buf_list = []
        class_name = cls.__name__
        csv_ext = ".csv"
        filename = class_name + csv_ext
        if list_objs is not None:
            for obj in list_objs:
                buf_list.append(obj.to_dictionary())
        with open(filename, "w+", encoding="utf-8") as f:
            f.write(buf_list)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        buf_list = []
        class_name = cls.__name__
        csv_ext = ".csv"
        filename = class_name + csv_ext
