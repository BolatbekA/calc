import unittest

from calculator.calculate import calculate


class CalculateTest(unittest.TestCase):

    def test_positive_case_1(self):
        result = calculate([5.0, 5.0, '+'])
        self.assertEqual(result, 10)

    def test_positive_case_2(self):
        result = calculate([100.1, '+'])
        self.assertEqual(result, 100.1)

    def test_positive_case_3(self):
        result = calculate([-0, '-'])
        self.assertEqual(result, 0)

    def test_positive_case_4(self):
        result = calculate([-7.0, 34.2, '/'])
        self.assertEqual(result, -0.205)
        



if __name__ == '__main__':
    unittest.main()
