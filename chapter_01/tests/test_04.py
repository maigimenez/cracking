import unittest
import string
from random import randint, choice
from itertools import permutations

from chapter_01.src.answer_04 import is_palindrome_permutation


def create_permutations(chars):
    """ Generator that returns all possible permutations.
    Args:
        chars: yield the permutations for this string.
    """
    for permutation in permutations(chars):
        yield (''.join(permutation))


class TestPalindromePermutation(unittest.TestCase):
    def test_is_palindrome_permutation(self):
        characters = string.ascii_lowercase
        n_chars = randint(3, 10)
        seed_strings = ''.join([choice(characters) for _ in range(n_chars)])
        palindrome = seed_strings + ' ' + seed_strings[::-1]
        permutation_func = create_permutations(palindrome)
        self.assertIs(is_palindrome_permutation(next(permutation_func)), True)

    def test_is_not_palindrome_permutation(self):
        not_palindrome = 'abcdefg'
        self.assertIs(is_palindrome_permutation(not_palindrome), False)

    def test_is_empty(self):
        self.assertIs(is_palindrome_permutation(""), False)

    def test_is_none(self):
        self.assertIs(is_palindrome_permutation(None), False)


if __name__ == '__main__':
    unittest.main()