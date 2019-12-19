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
     
    def test_pi(self):
        """
        Test pi corner cases
        """
        self.assertEqual(4.1415926535, Calc().eval('(pi)+1'))
        self.assertEqual(1.1415926535, Calc().eval('(pi)-2'))
        self.assertEqual(3.1415926535, Calc().eval('(pi+-5)+5'))
        self.assertEqual(1.8584073465, Calc().eval('(-pi+3)+2'))
        self.assertEqual(-29.478417602100684, Calc().eval('10-(pi*2)^2'))
        self.assertEqual(1.57079632675, Calc().eval('pi/2'))

    def test_e(self):
        """
        Test e corner cases
        """
        self.assertEqual(3.7182818284, Calc().eval('(e)+1'))
        self.assertEqual(0.7182818283999999, Calc().eval('(e)-2'))
        self.assertEqual(2.7182818284, Calc().eval('(e+-5)+5'))
        self.assertEqual(2.2817181716, Calc().eval('(-e+3)+2'))
        self.assertEqual(-19.556224394438587, Calc().eval('10-(e*2)^2'))
        self.assertEqual(1.3591409142, Calc().eval('e/2'))

    def test_phi(self):
        """
        Test phi corner cases
        """
        self.assertEqual(2.6180339886999997, Calc().eval('(phi)+1'))
        self.assertEqual(-0.3819660113000001, Calc().eval('(phi)-2'))
        self.assertEqual(1.6180339886999997, Calc().eval('(phi+-5)+5'))
        self.assertEqual(3.3819660113000003, Calc().eval('(-phi+3)+2'))
        self.assertEqual(-0.47213595435372646, Calc().eval('10-(phi*2)^2'))
        self.assertEqual(0.80901699435, Calc().eval('phi/2'))
