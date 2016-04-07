import unittest

from chapter01.src.question09 import string_rotation


class TestStringRotation(unittest.TestCase):
    def test_empty_string(self):
        self.assertIs(string_rotation("", ""), True)

    def test_equal_string(self):
        self.assertIs(string_rotation("abcdef", "abcdef"), True)

    def test_spaces_symbols(self):
        self.assertIs(string_rotation("d0=\*", "0=\*d"), True)

    def test_order(self):
        self.assertIs(string_rotation("waterbottle", "erbottlewat"), True)
        self.assertIs(string_rotation("waterbottle", "bottlewater"), True)
        self.assertIs(string_rotation("waterbottle", "elttobretaw"), False)
        self.assertIs(string_rotation("waterbottle", "watrebotlte"), False)

    def test_diff_size(self):
        self.assertIs(string_rotation("asdfg", "sdfg"), False)

if __name__ == "__main__":
    unittest.main()
