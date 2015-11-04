# Author: Yihong Du

import unittest
from unittest import TestCase
from create_array import *
from divide_array import *
from generate_randArray import *
from mandelbrot import *

class test_result(TestCase):

    def setUp(self):
        pass

    # Test question 1
    def test_create_array(self):
        ans = create_array()

        # correct array picked manually
        correct_array = np.array([[1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14], [5, 10, 15]])
        correct_a = np.array([[2, 7, 12], [4, 9, 14]])
        correct_b = np.array([[6], [7], [8], [9], [10]])
        correct_c = np.array([[2, 7, 12], [3, 8, 13], [4, 9, 14]])
        correct_d = np.array([6, 11, 7, 3, 8, 4, 9, 5, 10])

        self.assertTrue(np.array_equal(correct_array, ans.array))
        self.assertTrue(np.array_equal(correct_a, ans.picking_row()))
        self.assertTrue(np.array_equal(correct_b, ans.picking_column()))
        self.assertTrue(np.array_equal(correct_c, ans.picking_section()))
        self.assertTrue(np.array_equal(correct_d, ans.picking_range()))


    # Test question 2
    def test_divide_array(self):
        ans = divide_array()

        # correct answer for some elements in the array calculated manually
        correct_cordinate_1_2 = 1.4
        correct_cordinate_4_3 = 1.15

        self.assertEqual(correct_cordinate_1_2,ans[1,2])
        self.assertEqual(correct_cordinate_4_3,ans[4,3])


    # Test question 4
    def test_mandelbrot_init(self):
        ans = mandelbrot(500)
        correct_x, correct_y = np.meshgrid(np.linspace(-2, 1, 500), np.linspace(-1.5, 1.5, 500))
        correct_c = correct_x + 1j * correct_y

        self.assertTrue(np.array_equal(ans.c, correct_c))

if __name__ == "__main__":
    unittest.main() 
