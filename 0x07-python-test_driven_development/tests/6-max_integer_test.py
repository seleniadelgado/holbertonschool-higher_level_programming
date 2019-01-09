#!/usr/bin/python3
"""testing to find max int"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class Testmax(unittest.TestCase):
    """Testing the max_integer function"""

    def test_max_integer(self):
    """ test for an empty list"""
        self.assertEqual(max_integer(len(list[]), None)


if __name__ == '__main__':
    unittest.main()
