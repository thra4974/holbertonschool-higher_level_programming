#!/usr/bin/python3
"""containts load_from_json_file func"""
import json


def load_from_json_file(filename):
    """ creates an Object from JSON file"""
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
