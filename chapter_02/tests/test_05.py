import unittest

from chapter_02.src.answer_05 import sum_lists
from chapter_02.src.LinkedList import LinkedList


class TestSumLists(unittest.TestCase):
    def test_empty_list(self):
        self.assertIs(sum_lists(None, None), None)
        self.assertEqual(sum_lists(LinkedList(), LinkedList()), LinkedList())

    def test_sum_lists(self):
        self.assertEqual(sum_lists(LinkedList([7, 1, 6]), LinkedList([5, 9, 2])),
                         LinkedList([2, 1, 9]))

if __name__ == '__main__':
    unittest.main()
