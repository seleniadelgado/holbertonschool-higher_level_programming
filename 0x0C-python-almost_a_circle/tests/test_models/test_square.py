#!/usr/bin/python3
"""Unittest for base.py([..])"""

import unittest
from models.square import Square


class TestBase(unittest.TestCase):

    def test_correct_values_input(self):
        """test for four correct inputs for each instance"""
        Sq = Square(10, 10, 5, 5)
        self.assertEqual((Sq.size, Sq.x, Sq.y, Sq.id), (10, 10, 5, 5))

    def test_two_values_input(self):
        """test for if an input has only two values"""
        Sq = Square(10, 10, 0, 0)
        self.assertEqual((Sq.size, Sq.x, Sq.y, Sq.id), (10, 10, 0, 0))

    def test_type_one_input(self):
        """test for if input has no value"""
        with self.assertRaises(TypeError):
            Sq = Square()

    def test_type_float(self):
        """test for floats being passed in"""
        with self.assertRaises(TypeError):
            Sq = Square(10.5, 10, 5, 5)

    def test_type_str(self):
        """test for str being passed in"""
        with self.assertRaises(TypeError):
            Sq = Square(10, 10, "brasil", 5)

    def test_type_tuple(self):
        """test for tuples being passed in"""
        with self.assertRaises(TypeError):
            Sq = Square(10, (10, ), 5, 5)

    def test_type_list(self):
        """tests for lists being passed in"""
        with self.assertRaises(TypeError):
            Sq = Square(10, 10, [5], 5)

    def test_type_dict(self):
        """tests for dictionaries being passed in"""
        with self.assertRaises(TypeError):
            Sq = Square(10, 10, {"greeting": "hello"}, 5)

    def test_value_negative(self):
        """testing for correct value for width"""
        with self.assertRaises(ValueError):
            Sq = Square(-10, 10, 5, 5)

    def test_value_zero(self):
        """testing for correct value when 0"""
        with self.assertRaises(ValueError):
            Sq = Square(0, 0, 0, 0)

    def test_area(self):
        """testing for area number"""
        Sq = Square(10, 10)
        self.assertEqual(Sq.area(), 100)

    def test_area_type(self):
        """testing for area with string"""
        with self.assertRaises(TypeError):
            Sq = Square(10, "ten")

    def test_area_str(self):
        """testing for two strings"""
        with self.assertRaises(TypeError):
            Sq = Square("hello", "carrot")

    def test_display(self):
        """testing for display when nothing is passed"""
        with self.assertRaises(TypeError):
            Sq = Square()

    def test_display_allvalues(self):
        """testing for all values to display"""
        Sq = Square(2, 5, 3, 1)
        self.assertEqual(Sq.display(), None)

    def test_display_width_type(self):
        """testing for value error when 0 is passed"""
        with self.assertRaises(ValueError):
            Sq = Square(0, 5, 2, 1)

    def test_display_height_type(self):
        """testing for value error"""
        with self.assertRaises(ValueError):
            Sq = Square(5, -4, 2, 1)

    def test_update(self):
        """testing for true to update id to 4"""
        Sq = Square(10, 10, 10, 10)
        Sq.update(4)
        self.assertTrue(Sq.id == 4)

    def test_update_width(self):
        """testing for true to update width to 3"""
        Sq = Square(1, 1, 1, 1)
        Sq.update(width=3)
        self.assertFalse(Sq.width == 3)

    def test_update_height(self):
        """testing for true for height == 3"""
        Sq = Square(1, 1, 1, 1)
        Sq.update(height=3)
        self.assertFalse(Sq.height == 3)

    def test_update_x(self):
        """testing for true for x to == 3"""
        Sq = Square(1, 1, 1, 1)
        Sq.update(x=3)
        self.assertTrue(Sq.x == 3)

    def test_update_y(self):
        """testing for true that y = 3"""
        Sq = Square(1, 1, 1, 1)
        Sq.update(y=3)
        self.assertTrue(Sq.y == 3)

    def test_update_str(self):
        """testing for true that  y = string"""
        Sq = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            Sq.update(y="orange")

if __name__ == '__main__':
    unittest.main()
