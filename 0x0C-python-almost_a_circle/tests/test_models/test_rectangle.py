#!/usr/bin/python3
"""Unittest for base.py([..])"""

import unittest
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):


    def test_correct_value(self):
        """test for four correct inputs for each instance"""
        Rct = Rectangle(10, 10, 5, 5)
        self.assertEqual((Rct.width, Rct.height, Rct.x, Rct.y), (10, 10, 5, 5))

if __name__ == '__main__':
    unittest.main()

