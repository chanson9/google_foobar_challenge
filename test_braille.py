"""Unit Tests for foo.bar Braille Challenge"""
from unittest import TestCase

from braille import solution

class TryTesting(TestCase):
    def test_code(self):
        answer = solution('code')
        self.assertEqual(answer, '100100101010100110100010')

    def test_capitalization(self):
        answer_cap = solution('Code')
        self.assertEqual(answer_cap, '000001100100101010100110100010')

    def test_space(self):
        answer_space = solution('Code ')
        self.assertEqual(answer_space, '000001100100101010100110100010000000')

    def test_nonalphaspace(self):
        answer_non_alphanumeric = solution('Code12')
        self.assertEqual(answer_non_alphanumeric, '')

    def test_length(self):
        answer_long = solution('abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeakdlslkfjflslkdjf')
        self.assertEqual(answer_long, '')
