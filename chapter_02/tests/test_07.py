import unittest

from chapter_02.src.answer_07 import is_intersection
from chapter_02.src.LinkedList import LinkedList, Node


class TestIntersection(unittest.TestCase):
    def test_empty_list(self):
        self.assertIs(is_intersection(None, None), None)
        self.assertEqual(is_intersection(LinkedList(), LinkedList()), None)

    def test_intersection(self):
        fst_list = LinkedList([1, 2, 3, 4])
        snd_list = LinkedList([4, 6])
        self.assertEqual(is_intersection(fst_list, snd_list), None)
        self.assertEqual(is_intersection(fst_list, LinkedList()), None)
        self.assertEqual(is_intersection(LinkedList(), snd_list), None)
        common_node = Node(7)
        fst_list.append_node(common_node)
        snd_list.append_node(common_node)
        self.assertEqual(is_intersection(fst_list, snd_list), common_node)

if __name__ == '__main__':
    unittest.main()