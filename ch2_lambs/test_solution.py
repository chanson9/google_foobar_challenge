"""Unit Tests for foo.bar LAMB Challenge"""
from unittest import TestCase

from solution import solution


class TryTesting(TestCase):
    def test_ten(self):
        answer = solution(10)
        self.assertEqual(answer, 1)

    def test_six(self):
        answer = solution(6)
        self.assertEqual(answer, 1)

    def test_143(self):
        answer = solution(143)
        self.assertEqual(answer, 3)

    def test_negative(self):
        answer = solution(-10)
        self.assertEqual(answer, 0)

    def test_one(self):
        answer = solution(1)
        self.assertEqual(answer, 0)

    def test_40(self):
        answer = solution(40)
        self.assertEqual(answer, 2)

    def test_onebillion(self):
        answer = solution(1000000000)
        self.assertEqual(answer, 13)
