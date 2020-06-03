#!/usr/bin/python3
"""constains class_to_json function"""


def class_to_json(obj):
    """return dict desc w/simple data struct for JSON serialization"""
    return obj.__dict__
