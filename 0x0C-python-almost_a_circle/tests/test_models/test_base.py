#!/usr/bin/python3
import unittest
import sys
import pep8
from models import base
from models.base import Base


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
        file1 = 'module/base.py'
        file2 = 'tests/test_models/test_base.py'
        result = pep8style.check_files(['file1.py', 'file2.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
