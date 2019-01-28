#!/usr/bin/python3
"""Unittest for base.py([..])"""

import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):

    def test_correct_values_input(self):
        """test for four correct inputs for each instance"""
        Rct = Rectangle(10, 10, 5, 5)
        self.assertEqual((Rct.width, Rct.height, Rct.x, Rct.y), (10, 10, 5, 5))

    def test_two_values_input(self):
        """test for if an input has only two values"""
        Rct = Rectangle(10, 10)
        self.assertEqual((Rct.width, Rct.height, Rct.x, Rct.y), (10, 10, 0, 0))

    def test_type_one_input(self):
        """test for if input has no value"""
        with self.assertRaises(TypeError):
            Rct = Rectangle()

    def test_type_float(self):
        """test for floats being passed in"""
        with self.assertRaises(TypeError):
            Rct = Rectangle(10.5, 10, 5, 5)

    def test_type_str(self):
        """test for str being passed in"""
        with self.assertRaises(TypeError):
            Rct = Rectangle(10, 10, 5, "brasil")

    def test_type_tuple(self):
        """test for tuples being passed in"""
        with self.assertRaises(TypeError):
            Rct = Rectangle(10, (10, ), 5, 5)

    def test_type_list(self):
        """tests for lists being passed in"""
        with self.assertRaises(TypeError):
            Rct = Rectangle(10, 10, [5], 5)

    def test_type_dict(self):
        """tests for dictionaries being passed in"""
        with self.assertRaises(TypeError):
            Rct = Rectangle(10, 10, {"greeting": "hello"}, 5)

    def test_value_negative(self):
        """testing for correct value for width"""
        with self.assertRaises(ValueError):
            Rct = Rectangle(-10, 10, 5, 5)

    def test_value_zero(self):
        """testing for correct value when 0 is passed"""
        with self.assertRaises(ValueError):
            Rct = Rectangle(0, 0, 0, 0)

    def test_area(self):
        """testing for correct area"""
        Rct = Rectangle(10, 10)
        self.assertEqual(Rct.area(), 100)

    def test_area_type(self):
        """testing for when str is passed"""
        with self.assertRaises(TypeError):
            Rct = Rectangle(10, "ten")

    def test_area_empty(self):
        """testing for when str Type is passed"""
        with self.assertRaises(TypeError):
            Rct = Rectangle()

    def test_area_str(self):
        """testing for when there's two strings"""
        with self.assertRaises(TypeError):
            Rct = Rectangle("hello", "carrot")

    def test_display(self):
        """testing for when there's an empty type"""
        with self.assertRaises(TypeError):
            Rct = Rectangle()

    def test_display_allvalues(self):
        """testing for when correct values are passed"""
        Rct = Rectangle(2, 5, 3, 1)
        self.assertEqual(Rct.display(), None)

    def test_display_width_type(self):
        """testing for when 0 is passed"""
        with self.assertRaises(ValueError):
            Rct = Rectangle(0, 5, 2, 1)

    def test_display_height_type(self):
        """testing for when 0 is passed for height"""
        with self.assertRaises(ValueError):
            Rct = Rectangle(5, 0, 2, 1)

    def test_update(self):
        """testing for when update is passed 4"""
        Rct = Rectangle(10, 10, 10, 10)
        Rct.update(4)
        self.assertTrue(Rct.id == 4)

    def test_update_width(self):
        """testing for when 3 is passed for with"""
        Rct = Rectangle(1, 1, 1, 1)
        Rct.update(width=3)
        self.assertTrue(Rct.width == 3)

    def test_update_height(self):
        """testing for when 3 is passed for height"""
        Rct = Rectangle(1, 1, 1, 1)
        Rct.update(height=3)
        self.assertTrue(Rct.height == 3)

    def test_update_x(self):
        """testing for when 3 is passed for x"""
        Rct = Rectangle(1, 1, 1, 1)
        Rct.update(x=3)
        self.assertTrue(Rct.x == 3)

    def test_update_y(self):
        """testing for when 3 is passed for y"""
        Rct = Rectangle(1, 1, 1, 1)
        Rct.update(y=3)
        self.assertTrue(Rct.y == 3)

    def test_update_str(self):
        """testing for when str is passed for y"""
        Rct = Rectangle(1, 2, 3, 4)
        Rct.update(y="orange")
        self.assertTrue(Rct.y == "orange")

    def test_update_Kwargs(self):
        """testing for when 2 is passed for id"""
        Rct = Rectangle(1, 2, 3, 4)
        Rct.update(hello=2)
        self.assertTrue(Rct.id == 2)


if __name__ == '__main__':
    unittest.main()
