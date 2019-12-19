import unittest # https://docs.python.org/3/library/unittest.html
from modules.calculator import Calculator as Calc


class TestCalculator(unittest.TestCase):
    """
    Test Driven Development Unittest File
    Module: Calculator
    Updated: 12/16/2019
    Author: Kida Toy
    """
    def test_addition(self):
        """
        Evaluate addition corner cases
        """
        self.assertEqual(2, Calc().eval('1+1'))
        self.assertEqual(2, Calc().eval('1.0+1.0'))
        self.assertEqual(0, Calc().eval('-1+1'))
        self.assertEqual(-2, Calc().eval('-1+-1'))

    def test_subtraction(self):
        """
        Evaluate subtraction corner cases
        """
        self.assertEqual(0, Calc().eval('1-1'))
        self.assertEqual(-2, Calc().eval('-1-1'))
        self.assertEqual(0, Calc().eval('-1--1'))
    
    def test_multiplication(self):
        """
        Evaluate multiplication corner cases
        """
        self.assertEqual(0, Calc().eval('1*0'))
        self.assertEqual(0, Calc().eval('0*-1'))
        self.assertEqual(1, Calc().eval('1*1'))
        self.assertEqual(-1, Calc().eval('-1*1'))
        self.assertEqual(1, Calc().eval('-1*-1'))
        self.assertEqual(1, Calc().eval('.25*4'))
    
    def test_division(self):
        """
        Test division corner cases
        Note: division by zero is handled in test_exceptions
        """
        self.assertEqual(1, Calc().eval('1/1'))
        self.assertEqual(.25, Calc().eval('1/4'))
        self.assertEqual(-1, Calc().eval('-1/1'))
        self.assertEqual(1, Calc().eval('-1/-1'))
        self.assertEqual(0, Calc().eval('0/-1'))
    
    def test_exponents(self):
        """
        Test exponent corner cases
        """
        self.assertEqual(1, Calc().eval('2^0'))
        self.assertEqual(2, Calc().eval('2^1'))
        self.assertEqual(4, Calc().eval('2^2'))
        self.assertEqual(.5, Calc().eval('2^-1'))
        self.assertEqual(4, Calc().eval('-2^2'))

    def test_parentheses(self):
        """
        Test parentheses corner cases
        """
        self.assertEqual(5.0, Calc().eval('(4.0)+1'))
        self.assertEqual(3.0, Calc().eval('(4+1)-2'))
        self.assertEqual(5.0, Calc().eval('(5+-5)+5'))
        self.assertEqual(-5.0, Calc().eval('(-10+3)+2'))
        self.assertEqual(-26.0, Calc().eval('10-(3*2)^2'))
