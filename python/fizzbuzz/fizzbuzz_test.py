# -*- coding: utf-8 -*-
import unittest

from fizzbuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.fb = FizzBuzz()

    def test_all_numbers_are_returned(self):
        expected = 100
        actual = len(self.fb.get())

        self.assertEqual(actual, expected)

    def test_fizz_for_multiple_of_three(self):
        expected = True
        actual = self.fb.is_fizz(3)

        self.assertEqual(actual, expected)

    def test_fizz_for_non_multiple_of_three(self):
        expected = False
        actual = self.fb.is_fizz(10)

        self.assertEqual(actual, expected)

    def test_buzz_for_multiple_of_five(self):
        expected = True
        actual = self.fb.is_buzz(5)

        self.assertEqual(actual, expected)

    def test_buzz_for_non_multiple_of_five(self):
        expected = False
        actual = self.fb.is_buzz(11)

        self.assertEqual(actual, expected)

    def test_fizz_buzz_for_non_multiple_of_three_and_five(self):
        expected = False
        actual = self.fb.is_fizz_buzz(2)

        self.assertEqual(actual, expected)

    def test_fizz_buzz_for_multiple_of_three_and_five(self):
        expected = True
        actual = self.fb.is_fizz_buzz(15)

        self.assertEqual(actual, expected)

    def test_get_return_the_right_list(self):
        actual = self.fb.get()

        self.assertEqual(actual[2], 'Fizz')
        self.assertEqual(actual[4], 'Buzz')
        self.assertEqual(actual[14], 'Fizz Buzz')


if __name__ == '__main__':
    unittest.main()
