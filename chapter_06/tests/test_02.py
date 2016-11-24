import unittest

from random import uniform

from chapter_06.src.answer_02 import basketball


class TestBasketball(unittest.TestCase):
    def test_equal(self):
        for p in [0.0, 0.5, 1.0]:
            self.assertEqual(basketball(p), 0)

    def test_game1(self):
        self.assertEqual(basketball(uniform(0.01, 0.49)), 1)

    def test_game2(self):
        self.assertEqual(basketball(uniform(0.51, 0.99)), 2)
