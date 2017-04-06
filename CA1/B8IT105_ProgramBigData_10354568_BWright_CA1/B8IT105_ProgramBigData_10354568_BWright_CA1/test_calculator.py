#This code contains the test code

import unittest

from calculator import Calculator

# test the car functionality
#class TestCar(unittest.TestCase):
# test the calculator functionality

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

# Arithmetic Functions
	# this tests the add functionality
	# 2 + 2 = 4
	# 2 + 4 = 6
	# 2 + (-2) = 0
    # All tests follow this format
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
        result = self.calc.add(2,4)
        self.assertEqual(6, result)
        result = self.calc.add(2, -2)
        self.assertEqual(0, result)

    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2, -4)
        self.assertEqual(6, result)
        
    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply(2, 2)
        self.assertEqual(4, result)
        result = self.calc.multiply(2,0)
        self.assertEqual(0, result)
        result = self.calc.multiply(-2, -2)
        self.assertEqual(4, result)
		
    def test_calculator_divide_method_returns_correct_result(self):
        result = self.calc.divide(2, 2)
        self.assertEqual(1, result)
        result = self.calc.divide(4,2)
        self.assertEqual(2, result)
        result = self.calc.divide(2, -2)
        self.assertEqual(-1, result)
        result = self.calc.divide(2, 4)
        self.assertEqual(0.5, result)
        result = self.calc.divide(2, 0)
        self.assertEqual('NaN', result)
        self.assertRaises(ValueError, self.calc.divide, 'two', 'three')
        self.assertRaises(ValueError, self.calc.divide, 'two', 0)
        self.assertRaises(ValueError, self.calc.divide, 2, 'three')
        
    # Power Functions	
    def test_calculator_exponent_method_returns_correct_result(self):
        result = self.calc.exponent(2, 2)
        self.assertEqual(4, result)
        result = self.calc.exponent(0,2)
        self.assertEqual(0, result)
        result = self.calc.exponent(2, 0)
        self.assertEqual(1, result)
        result = self.calc.exponent(2, -2)
        self.assertEqual(0.25, result)
		
    def test_calculator_squareroot_method_returns_correct_result(self):
        result = self.calc.squareroot(4)
        self.assertEqual(2, result)
        result = self.calc.squareroot(100)
        self.assertEqual(10, result)
        result = self.calc.squareroot(25)
        self.assertEqual(5, result)  
        
    def test_calculator_square_method_returns_correct_result(self):
        result = self.calc.square(2)
        self.assertEqual(4, result)
        result = self.calc.square(-4)
        self.assertEqual(16, result)
        result = self.calc.square(5.5)
        self.assertEqual(30.25, result)
        result = self.calc.square(0)
        self.assertEqual(0, result)  
               
    def test_calculator_factorial_method_returns_correct_result(self):
        result = self.calc.factorial(5)
        self.assertEqual(120, result)
        result = self.calc.factorial(6)
        self.assertEqual(720, result)
        result = self.calc.factorial(1)
        self.assertEqual(1, result)
        
# Trigonometric Functions  
    def test_calculator_sinRad_method_returns_correct_result(self):
        result = self.calc.sinRad(3)
        self.assertEqual(0.1411200080598672, result)
        result = self.calc.sinRad(180)
        self.assertEqual(-0.8011526357338304, result)
        result = self.calc.sinRad(100)
        self.assertAlmostEqual(-0.5063656, result)
        
    def test_calculator_cosRad_method_returns_correct_result(self):
        result = self.calc.cosRad(90)
        self.assertAlmostEqual(-0.4480736, result)
        result = self.calc.cosRad(200)
        self.assertAlmostEqual(0.4871877, result)
        result = self.calc.cosRad(0)
        self.assertEqual(1, result)
       
    def test_calculator_tanRad_method_returns_correct_result(self):
        result = self.calc.tanRad(90)
        self.assertEqual(-1.995200412208242, result)
        result = self.calc.tanRad(180)
        self.assertAlmostEqual(1.3386902, result)
        result = self.calc.tanRad(1)
        self.assertAlmostEqual(1.5574077, result)

        
if __name__ == '__main__':
    unittest.main()