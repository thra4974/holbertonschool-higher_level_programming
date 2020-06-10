#!/usr/bin/python3
import unittest
import json
import sys
import pep8
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseDocumentation(unittest.TestCase):
    """Checks Documentation"""
    def test_module_documentation(self):
        """check that module has docstrings"""
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_documentation(self):
        """check that class Base has docstrings"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_documentation(self):
        """checks that methods of Base have docstrings"""
        for methods in dir(Base):
            self.assertTrue(len(methods.__doc__) > 0)


class TestBasePep8(unittest.TestCase):
    """Checks for Pep8 formatting"""
    def test_pep8_format(self):
        """test base module for pep8 formatting"""
        pep8style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base.py'
        file2 = 'tests/test_models/test_base.py'
        result = pep8style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Test_Base(unittest.TestCase):
    """Tests for class Base model"""
    @classmethod
    def setUp_Class(cls):
        """set up class instance"""
        Base._Base_nb_objects = 0
        cls.b1 = Base()
        cls.b2 = Base(98)
        cls.b3 = Base("one")
        cls.b4 = Base(1.1)
        cls.rec = Rectangle(1, 1, 0, 0, 1)

    def test_id(self):
        """tests for id attribute"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 98)
        self.assertEqual(self.b3.id, "one")
        self.assertEqual(self.b4.id, 1.1)
