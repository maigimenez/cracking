import unittest
import string
from random import randint, choice
from itertools import permutations

from chapter_01.src.answer_02 import is_permutation


def create_permutations(chars):
    """ Generator that returns all possible permutations.
    Args:
        chars: yield the permutations for this string.
    """
    for permutation in permutations(chars):
        yield (''.join(permutation))


class TestPermutation(unittest.TestCase):
    def test_is_permutation(self):
        characters = string.ascii_lowercase + string.digits
        n_chars = randint(3, 10)
        seed_strings = ''.join([choice(characters) for _ in range(n_chars)])
        permutation_func = create_permutations(seed_strings)
        fst_string, snd_string = next(permutation_func), next(permutation_func)
        self.assertIs(is_permutation(fst_string, snd_string), True)

    def test_is_not_permutation(self):
        fst_string, snd_string = 'abcd', 'efg'
        self.assertIs(is_permutation(fst_string, snd_string), False)

    def test_is_empty(self):
        self.assertIs(is_permutation("non empty string", ""), False)
        self.assertIs(is_permutation("", "non empty string"), False)
        self.assertIs(is_permutation("", ""), False)

    def test_is_none(self):
        self.assertIs(is_permutation("non empty string", None), False)
        self.assertIs(is_permutation(None, "non empty string"), False)

if __name__ == '__main__':
    unittest.main()