import unittest

from chapter_01.src.answer_01 import unique_chars


class TestUnique(unittest.TestCase):
    def test_empty_string(self):
        self.assertIs(unique_chars(""), True)

    def test_unique_string(self):
        self.assertIs(unique_chars("abcxyz"), True)

    def test_repeated_string(self):
        self.assertIs(unique_chars("ooooohh"), False)

if __name__ == "__main__":
    unittest.main()
