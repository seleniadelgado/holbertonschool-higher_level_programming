#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """ test for an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_max_integer(self):
        """test if biggest number is at the end"""
        self.assertEqual(max_integer([0, float("inf")]), float("inf"))

    def test_max_integer(self):
        """test if biggest number is at the beginning"""
        self.assertEqual(max_integer([float("inf"), 0]), float("inf"))

    def text_max_integer(self):
        """test if biggest number is in the middle"""
        self.assertEqual(max_integer([0, float("inf"), 0]), float("inf"))

    def text_max_integer(self):
        """test for if "one negative number in the list" exists"""
        self.assertEqual(max_integer([-1, 0, 0]), -1)

    def test_max_integer(self):
        """test for only negative numbers in the list"""
        self.assertEqual(max_integer([-1, -4]), -1)

    def test_max_integer(self):
        """test for only one element in list"""
        self.assertEqual(max_integer([0]), 0)

if __name__ == '__main__':
    unittest.main()
