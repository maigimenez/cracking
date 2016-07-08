import unittest
import string
from random import randint, choice
from chapter_01.src.answer_06 import compress


class TestComprenssion(unittest.TestCase):

    def test_is_compressed(self):
        characters = string.ascii_lowercase
        long_string = randint(3, 10)
        seed_string = []
        for _ in range(long_string):
            char_to_add = choice(characters)
            if seed_string:
                while char_to_add == seed_string[-1][0]:
                    char_to_add = choice(characters)

            seed_string.append((char_to_add, randint(3, 10)))

        compressed_string = ''.join([letter+str(rep) for letter, rep in seed_string])
        expanded_string = ''.join([letter*rep for letter, rep in seed_string])
        self.assertEqual(compress(expanded_string), compressed_string)
    #
    # def test_is_same_len(self):
    #     self.assertEqual(compress("abcde"), "abcde")
    #
    # def test_is_empty(self):
    #     self.assertIs(compress(""), "")
    #
    # def test_is_none(self):
    #     self.assertIs(compress(None), None)


if __name__ == '__main__':
    unittest.main()
