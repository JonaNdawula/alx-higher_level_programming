#!/usr/bin/python3
"""
Class testSquareMethods
"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import json
import unittest
from unittest.mock import patch
 

class TestSquareMethods(unittest.TestCase):
    """
    Test for Square Class
    """

    def initialize(self):
        """
        Invoked for each test
        """
        Base._Base__nb_objects = 0

    def cleanUp():
        """
        cleans up after test
        """
        pass

    def test_constructor_args(self):
        """
        constuctor with args
        """
        with self.assertRaises(TypeError) as err:
            sq =Square(1, 2, 3, 4, 5)
            resp = "__init__() takes from 2 to 5 positional arguments but 6 \ were given"
            self.assertEqual(str(err.exception), resp)

    def test_constructor_noargs(self):
        """
        Constructor with no args
        """
        with self.assertRaises(TypeError) as err:
            sq = Square()
            resp ="__init__() missing 1 required positional argument: 'size'"
            self.assertEqual(str(err.exception), resp)


    def test_area(self):
        """
        Test area
        """
        sq = Square(2)
        self.assertEqual(sq.area(), 4)

    def test_area_noargs(self):
        """
        area no args
        """
        x = Square(5)
        with self.assertRaises(TypeError) as err:
            Square.area()
        info = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), info)


    def test_area_modified(self):
        """
        Test area method
        """
        sq1 = Square(10)
        self.assertEqual(sq1.area(), 100)
        sq1.size = 11
        self.assertEqual(sq1.area(), 121)

    def test_load_from_file(self):
        """
        Test load JSON File
        """
        file_load = Square.load_from_file()
        self.assertEqual(file_load, file_load)

    def test_basic_display(self):
        """
        Test display No x or y
        """
        sq1 = Square(4)
        res = "####\n####\n####\n####\n"

        with patch('sys.stdout', new=StringIO()) as s_out:
            sq1.display()
            self.assertEqual(s_out.getvalue(), res)
