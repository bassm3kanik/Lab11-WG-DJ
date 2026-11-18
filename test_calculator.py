# https://github.com/bassm3kanik/Lab11-WG-DJ/tree/main
# Partner 1: Daniel Jinks
# Partner 2: Wolfgang Gutierrez

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-4, -6), -10)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(-2, -3), 1)

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(7, 0), 0)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,10), 5)
        self.assertEqual(div(-4, 20), -5)
        self.assertAlmostEqual(div(3, 1), 1/3)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(4, 16), 2.0)

    def test_log_invalid_base(self): # 1 assertion
        self.assertEqual(logarithm(2, 8), 3)
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.4142, places = 4)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(25), 5)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()