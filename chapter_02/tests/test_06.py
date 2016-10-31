import unittest

from chapter_02.src.answer_06 import is_palindrome
from chapter_02.src.LinkedList import LinkedList


class TestPalindrome(unittest.TestCase):
    def test_empty_list(self):
        self.assertIs(is_palindrome(None), None)
        self.assertEqual(is_palindrome(LinkedList()), True)

    def test_sum_lists(self):
        self.assertEqual(is_palindrome(LinkedList(['a'])), True)
        self.assertEqual(is_palindrome(LinkedList(['a', 'b', 'a'])), True)
        self.assertEqual(is_palindrome(LinkedList(['a', 'b', 'b', 'a'])), True)
        self.assertEqual(is_palindrome(LinkedList(['a', 'b', 'a', 'a'])), False)
        self.assertEqual(is_palindrome(LinkedList(['a', 'b', 'c', 'b', 'a'])), True)
        self.assertEqual(is_palindrome(LinkedList(['a', 'b', 'c', 'c', 'a'])), False)

if __name__ == '__main__':
    unittest.main()