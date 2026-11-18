import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(7, 0), 0)


    def test_divide(self): # 3 assertions
        self.assertEqual(divide(2,10), 5)
        self.assertEqual(divide(-4, 20), -5)
        self.assertAlmostEqual(divide(3, 1), 0.33333)
    ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.4142)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(25), 5)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()