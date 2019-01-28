#!/usr/bin/python3
"""Unittest for base.py([..])
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_empty_id(self):
        """test for an id = none"""
        Base1 = Base()
        self.assertEqual(Base1.id, 1)

    def test_number_id(self):
        """test for an id = 20"""
        Base1 = Base(20)
        self.assertEqual(Base1.id, 20)

    def test_str_id(self):
        """test for an id of a str"""
        Base1 = Base("carrot")
        self.assertEqual(Base1.id, "carrot")

    def test_float_id(self):
        """test for an id of a float"""
        Base1 = Base(1.5)
        self.assertEqual(Base1.id, 1.5)

if __name__ == '__main__':
    unittest.main()
