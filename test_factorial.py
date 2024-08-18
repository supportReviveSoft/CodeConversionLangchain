
import unittest
from factorial import calc_factorial

class TestFactorial(unittest.TestCase):
    def test_calc_factorial(self):
        result = calc_factorial(5)
        self.assertEqual(result, 120)
        print("Factorial of 5 is", result)
        print("Test Passed")

if __name__ == '__main__':
    unittest.main()