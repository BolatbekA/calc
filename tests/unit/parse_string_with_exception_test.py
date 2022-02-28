import unittest

from calculator.parse_string_with_exception import parse_string_with_exception
from calculator.parsing_exception import ParsingException


class ParseStringWithExceptionTest(unittest.TestCase):

    def test_positive_case_1(self):
        result = parse_string_with_exception('5+5')
        self.assertEqual(result, [5.0, 5.0, '+'])

    def test_positive_case_2(self):
        result = parse_string_with_exception('-5+5')
        self.assertEqual(result, [-5.0, 5.0, '+'])

    def test_negative_case_1_exception(self):
        with self.assertRaises(ParsingException):
            parse_string_with_exception('5+5)')


if __name__ == '__main__':
    unittest.main()
