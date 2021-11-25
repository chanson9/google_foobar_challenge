"""Unit Tests for foo.bar GEARS Challenge"""
from unittest import TestCase

from solution import solution


class TryTesting(TestCase):
    def test_one(self):
        answer = solution([4, 17, 50])
        self.assertEqual(answer, [-1,-1])

    def test_two(self):
        answer = solution([4, 30, 50])
        self.assertEqual(answer, [12,1])
