import unittest

from chapter_02.src.answer_01 import remove_dups
from chapter_02.src.LinkedList import LinkedList


class TestRemoveDup(unittest.TestCase):
    def test_empty_list(self):
        self.assertIs(remove_dups(None), None)
        self.assertEqual(remove_dups(LinkedList()), LinkedList())

    def test_remove_dups(self):
        orig_list = LinkedList([1, 2, 4, 3, 3, 4])
        dup_list = LinkedList([1, 2, 4, 3])
        self.assertEqual(remove_dups(orig_list), dup_list)

        orig_list = LinkedList([1, 1, 1, 3, 3, 4])
        dup_list = LinkedList([1, 3, 4])
        self.assertEqual(remove_dups(orig_list), dup_list)

        orig_list = LinkedList([1, 1, 1, 1, 1, 1, 1])
        dup_list = LinkedList([1])
        self.assertEqual(remove_dups(orig_list), dup_list)

        orig_list = LinkedList([1, 2, 3, 4, 5])
        dup_list = LinkedList([1, 2, 3, 4, 5])
        self.assertEqual(remove_dups(orig_list), dup_list)


if __name__ == '__main__':
    unittest.main()
