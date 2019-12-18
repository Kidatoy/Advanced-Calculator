import unittest
from tests.test_calculator import TestCalculator
from modules.calculator import Calculator
import numpy as np

"""
This main file will execute a custom expression
calculator as a safe non-modifiable python interpreter
to calculate pemdas mathmatical expressions

Example: Calculator().eval('(18/6*5)-14/7'))

Note: pemdas is the order of operations
  1 -> p: perenthesis
  2 -> e: exponents
  3 -> m: multiplication
  4 -> d: division
  5 -> a: addition
  6 -> s: subtraction


Note: will execute all unittests

Author: Kida Toy
"""

if __name__ == '__main__':
    
    # perform all unittests
    unittest.main(TestCalculator(), exit=False)

    # print the options to the user
   

    # prompt for and calculate expressions
    while True:
        try:
          print(f'> {Calculator().prompt()}')
        except Exception as e:
          pass
    
