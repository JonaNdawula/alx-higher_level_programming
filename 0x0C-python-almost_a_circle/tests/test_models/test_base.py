#!/usr/bin/python3

"""
Test for Base class
"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseMethods(unittest.TestCase):
    """
    Tests for the Base class
    """
    def initialize(self):
        """ Runs for every test"""
        Base._Base__nb_objects = 0
        self.new_base = Base(id=1)

    def clean_up(self):
        """cleans up"""
        pass

    def test_docstring(self):
        """
        is doc string present ??
        """
        self.assertIsNotNone(Base.__doc__)

    def test_random_id(self):
        """ Test random args """
        test1 = Base(2)
        self.assertEqual(test1.id, 2)
        test2 = Base(4)
        self.assertEqual(test2.id, 4)
        test3 = Base(6)
        self.assertEqual(test3.id, 6)
        test4 = Base(-5)
        self.assertEqual(test4.id, -5)
        test5 = Base(-4)
        self.assertEqual(test5.id, -4)

    def test_incrementing_ids(self):
        """
        Tests ids
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_nondefault_start_id(self):
        """ Test if id duplicates"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base(20)
        b4 = Base()
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 20)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 4)


    def test_missing_args(self):
        """Test constructor"""
        with self.assertRaises(TypeError) as a:
            Base.__init__()
        info = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(a.exception), info)

    def test_to_json_string(self):
        """
        Test to_json_string
        method
        """
        rect1 = Rectangle(10, 7, 2, 8)
        rect2 = Rectangle(2, 4, 6, 8)

        square = [rect1, rect2]
        json_string = Base.to_json_string([rect1.to_dictionary(), rect2.to_dictionary()])
        self.assertEqual(type(json_string), str)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertTrue(type(Base.to_json_string(None)) is str)
        self.assertTrue(type(Base.to_json_string("[]")) is str)
        dic = json.loads(json_string)
        self.assertEqual(dic, [rect1.to_dictionary(), rect2.to_dictionary()])
        
    def test_from_json_string(self):
        """
        Test from_json_string
        """
        rect1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])
        exp_input = [rect1.to_dictionary()]
        json_ls_input = Rectangle.to_json_string(exp_input)
        ls_output = Rectangle.from_json_string(json_ls_input)
        self.assertEqual(ls_output, [rect1.to_dictionary()])
        self.assertTrue(type(ls_output), list)

    def test_create(self):
        """
        Test for create
        """
        exp_w = 1
        exp_h = 1

        result =  Rectangle.create(width=exp_w, height=exp_h)
        self.assertEqual(result.width, exp_w)
        self.assertEqual(result.height, exp_h)

        result2 = Square.create(size=exp_w)
        self.assertEqual(result2.size, exp_w)
