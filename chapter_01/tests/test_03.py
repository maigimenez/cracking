import unittest

from chapter_01.src.question_03 import urlify


class TestURLify(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(urlify(list(""), 0), list(""))

    def test_string_no_spaces(self):
        self.assertEqual(urlify(list("CivilWar"), 8),
                         list("CivilWar"))

    def test_string_double_spaces(self):
        self.assertEqual(urlify(list("Double  space    "), 13),
                         list("Double%20%20space"))

    def test_string_normal(self):
        self.assertEqual(urlify(list("Mr John Smith    "), 13),
                         list("Mr%20John%20Smith"))

if __name__ == "__main__":
    unittest.main()
