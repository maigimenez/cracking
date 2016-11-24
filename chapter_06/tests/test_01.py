import unittest

from chapter_06.src.answer_01 import heavy_pill


class TestHeavyPill(unittest.TestCase):
    def test_empty(self):
        n_pills = 5
        bottles = [[1.0] * n_pills] * 19
        bottles += [[None] * n_pills]
        self.assertIs(heavy_pill(bottles), None)

    def test_multiple_arguments(self):
        n_pills = 5
        bottle_1 = [[1.0] * n_pills]
        bottle_3 = [[1.1] * n_pills]
        bottle_2 , bottle_4 = bottle_1, bottle_1
        self.assertIs(heavy_pill(bottle_1, bottle_2, bottle_3, bottle_4), 3)

    def test_find_bottle(self):
        n_pills = 5
        bottles = [[1.0] * n_pills] * 5
        bottles += [[1.1] * n_pills]
        bottles = [[1.0] * n_pills] * 14
        self.assertIs(heavy_pill(bottles), 5)

        bottles = [[1.0] * n_pills] * 19
        bottles += [[1.1] * n_pills]
        self.assertIs(heavy_pill(bottles), 20)

        bottles = [[1.1] * n_pills]
        bottles += [[1.0] * n_pills] * 19
        self.assertIs(heavy_pill(bottles), 1)


if __name__ == "__main__":
    unittest.main()
