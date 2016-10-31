import unittest

from chapter_02.src.answer_02 import get_kth_last
from chapter_02.src.LinkedList import LinkedList


class TestKthLast(unittest.TestCase):
    def test_empty_list(self):
        self.assertIs(get_kth_last(None, 7), None)
        self.assertIs(get_kth_last(LinkedList(), 33), None)

    def test_out_range(self):
        self.assertIs(get_kth_last(LinkedList([1,2,3,4,5]), 10), None)

    def test_out_range(self):
        self.assertEqual(get_kth_last(LinkedList([1, 2, 3, 4, 5]), 2), LinkedList([3, 4, 5]))
        self.assertEqual(get_kth_last(LinkedList([1, 2, 3, 4, 5]), 4), LinkedList([5]))

if __name__ == '__main__':
    unittest.main()
