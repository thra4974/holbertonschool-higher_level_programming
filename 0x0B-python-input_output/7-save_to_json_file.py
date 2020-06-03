#!/usr/bin/python3
"""contains save_to_json_file func"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to text file using JSON rep"""
    with open(filename, "w+", encoding="utf-8") as f:
        return json.dump(my_obj, f)
