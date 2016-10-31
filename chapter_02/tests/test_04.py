import unittest

from chapter_02.src.answer_04 import get_partition
from chapter_02.src.LinkedList import LinkedList


class TestPartition(unittest.TestCase):
    def test_empty_list(self):
        self.assertIs(get_partition(None, 4), None)

    def test_not_x(self):
        self.assertEqual(get_partition(LinkedList([1,2,3,4]), 5), LinkedList([1,2,3,4]))

    def test_delete_node(self):
        self.assertEqual(get_partition(LinkedList([3, 5, 8, 5, 10, 2, 1]), 5),
                         LinkedList([3, 2, 1, 5, 8, 5, 10]))

if __name__ == '__main__':
    unittest.main()
