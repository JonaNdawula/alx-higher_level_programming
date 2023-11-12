#!/usr/bin/python3

import json
import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """
    Tests for Rectangle
    Class
    """

    @classmethod
    def init(cls):
        """
        Runs test
        """
        Base._Base__nb_objects = 0

    def cleanup(self):
        """
        cleans up after test
        """
        pass


    def test_class(self):
        """
        Tests if Rectangle
        is a class
        """
        self.assertEqual(str(Rectangle),
                          "<class 'models.rectangle.Rectangle'>")

    def test_arg_passed(self):
        """
        Test for args passed
        """
        with self.assertRaises(TypeError):
            Rectangle(10)
            Rectangle()

    def test_class_inheritance(self):
        """
        Test for whether
        Rectangle is a child
        of Base
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_constructor_without_args(self):
        """
        Tests a constructor
        with no args
        """
        with self.assertRaises(TypeError) as err:
            rect = Rectangle()
            ch = "__init__() missing 2 required positional arguments: 'width' \ and 'height'"
            self.assertEqual(str(err.exception), ch)

    def test_constructor_single_arg(self):
        """
        Tests a constructor with
        one Argument
        """
        with self.assertRaises(TypeError) as err:
            rect = Rectangle(1)

        ch = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(err.exception), ch)

    def test_area(self):
        """
        Check return value of area
        """
        rect = Rectangle(4, 4)
        self.assertEqual(rect.area(), 16)
        rect.width = 3
        self.assertEqual(rect.area(), 12)
        rect.height = 3
        self.assertEqual(rect.area(), 9)

    def test_area_with_no_args(self):
        """
        Check return value of area
        """
        rect = Rectangle(10, 12)
        with self.assertRaises(TypeError) as err:
            Rectangle.area()
        ch = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), ch)

    def test_str_with_no_args(self):
        """
        Test __str__ no args
        """

        rect = Rectangle(10, 2)
        with self.assertRaises(TypeError) as err:
            Rectangle.__str__()
        ch = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(err.exception), ch)

    def _to_dictionary(self):
        """
        Test for dictionary method
        """
        rect1 = Rectangle(10, 2, 1, 9)
        dict1 = rect1.to_dictionary()

        exp_list = {'id': 1, 'width' : 10, 'height': 2, 'x': 1, 'y': 9}
        rect2 = Rectangle(1, 1)

        dict2 = rect2.to_dictionary()

        exp_list2 = {'x': 0, 'y': 0, 'id': 2, 'height': 1, 'width': 1}
        self.assertEqual(dict1, exp_list)
        self.assertEqual(dict2, exp_list2)
        self.assertEqual(type(dict1), dict)
        self,assertEqual(type(dict2), dict)


    def test_save_to_file_(self):
        """
        save to empty file
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as fi:
            self.assertEqual([], json.load(fi))

    def test_save_to_file_Noneargs(self):
        """
        Test save_to_file None as arg
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode="r") as fi:
            self.assertEqual([], json.load(fi))

    def test_save_to_file(self):
        """
        Test save_to_file
        """
        rect0 = Rectangle(1, 2, 3, 4)
        rect1 = Rectangle(2, 4)
        my_list = [rect0, rect1]
        Rectangle.save_to_file(my_list)
        reference = Rectangle.load_from_file()
        self.assertNotEqual(my_list, reference)
