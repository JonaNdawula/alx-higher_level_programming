#!/usr/bin/python3

"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class testMaxInteger(unittest.TestCase):

#All tests must be passed
#unittest module constructs and runs test
    
    def test_empty_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_value(self):
        self.assertEqual(max_integer([10, 15, 20, 25]), 25)

    def test_negative_value(self):
        self.assertEqual(max_integer([-10]), -10)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_large_number(self):
        self.assertEqual(max_integer([1000, 5000, 3000, 8000]), 8000)

    def test_mixed_values(self):
        self.assertEqual(max_integer([7, -2, -5, 10]), 10)

if __name__ == '__main__':
    unittest.main()
