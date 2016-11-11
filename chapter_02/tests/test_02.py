import unittest

from random import randrange

from chapter_02.src.answer_02 import get_kth_last
from chapter_02.src.LinkedList import create_linked_list


class TestKLast(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_kth_last(create_linked_list([]), 2), None)

    def test_range(self):
        ll = create_linked_list(list(range(10)))
        self.assertEqual(get_kth_last(ll, 12), None)

    def test_integer_list(self):
        l = list(range(10))
        ll = create_linked_list(l)
        k = randrange(10)
        self.assertEqual(get_kth_last(ll, k).to_list(), l[k:])
