import unittest
import string
from random import randint, choice
from chapter_01.src.answer_06 import compress


class TestComprenssion(unittest.TestCase):

    def test_is_compressed(self):
        characters = string.ascii_lowercase
        long_string = randint(3, 10)
        seed_string = [(choice(characters), randint(3, 10)) for _ in range(long_string)]
        compressed_string = ''.join([letter+str(rep) for letter, rep in seed_string])
        expanded_string = ''.join([letter*rep for letter, rep in seed_string])
        self.assertIs(compress(expanded_string), compressed_string)

    def test_is_same_len(self):
        self.assertIs(compress("abcde"), "abcde")

    def test_is_empty(self):
        self.assertIs(compress(""), "")

    def test_is_none(self):
        self.assertIs(compress(None), None)


if __name__ == '__main__':
    unittest.main()
