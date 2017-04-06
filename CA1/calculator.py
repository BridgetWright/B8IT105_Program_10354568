# Student no: 10354568
# Student name: Bridget Wright
# Module: Programming for Data Analytics
# Assignment: CA 1
# Submission Date: Sun 26th Mar 2017
# Assignment Title: A 10 function scientific calculator
# A functioning calculator with 3 seperate pieces of code 
# 1. the user interface, 2. the functions and 3. the test code 
# for the arithmetic, power, and trigonometric functions
# This calculator contains 11 functions

# This code contains the functions

import math

# Import the following if calculator functionality needs to be extended with more complex functions
# import cmath
# import numpy
# import scipy


class Calculator(object):
# implement the calculator object

# Arithmetic Functions 
    def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    def subtract(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError
            
    def multiply(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x * y
        else:
            raise ValueError
            
    def divide(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            if y == 0:
                return 'NaN'
            return x / float(y)
        else:
            raise ValueError
 
# Power Functions	 
    def exponent(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x ** y
        else:
            raise ValueError	

    def squareroot(self, x):
        number_types = (int, long, float, complex)
        if x < 0:
            return "This is a negative root"
        elif isinstance(x, number_types):
            return math.sqrt(x)
        elif not isinstance(x, (int, long, float)):
            return "Please enter a number"
        else:
            raise ValueError
            
    def square(self, x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            return x*x
        else:
            raise ValueError  	
                        
    def factorial (self,x):
        number_types = (int, long, float, complex) 
        if isinstance(x, number_types):
            return math.factorial(x)
        else:
            raise ValueError

# Trigonometric Functions             
    def sinRad(self, x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            return math.sin(x)
        else:
            raise ValueError
            
        
    def cosRad(self, x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            return math.cos(x)
        else:
            raise ValueError
            
    def tanRad(self, x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            return math.tan(x)
        else:
            raise ValueError
            
        
