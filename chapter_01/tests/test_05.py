import unittest

from chapter_01.src.question_05 import one_away


class TestOneAway(unittest.TestCase):
    def test_one_char(self):
        self.assertIs(one_away("a", ""), True)
        self.assertIs(one_away("", "b"), True)
        self.assertIs(one_away("c", "d"), True)

    def test_zero_away(self):
        self.assertIs(one_away("", ""), True)
        self.assertIs(one_away("lol", "lol"), True)

    def test_spaces(self):
        self.assertIs(one_away("Del ete", "Delete"), True)
        self.assertIs(one_away("Mod fy", "Modify"), True)
        self.assertIs(one_away("Insert", "In sert"), True)
        self.assertIs(one_away("Two much", "Twomuch "), False)

    def test_more_away(self):
        self.assertIs(one_away("Good", "Evil"), False)
        self.assertIs(one_away("cue", "queue"), False)

    def test_book(self):
        self.assertIs(one_away("pale", "ple"), True)
        self.assertIs(one_away("pales", "pale"), True)
        self.assertIs(one_away("pale", "bale"), True)
        self.assertIs(one_away("pale", "bake"), False)

if __name__ == "__main__":
    unittest.main()
