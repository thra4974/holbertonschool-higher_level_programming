#!/usr/bin/python3
"""defines Class: Mylist that inherits from list"""


class MyList(list):
    """defines Class Mylist, inherits list"""

    def __init__(self):
        """ inits myList object"""
        pass

    def print_sorted(self):
        """
        prints sorted list in ascending order
        """
        print(sorted(self))
