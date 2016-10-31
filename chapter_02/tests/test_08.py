import unittest

from chapter_02.src.answer_08 import circular_node
from chapter_02.src.LinkedList import LinkedList, Node


class TestIntersection(unittest.TestCase):
    def test_empty_list(self):
        self.assertIs(circular_node(None), None)
        self.assertEqual(circular_node(LinkedList()), None)

    def test_intersection(self):
        fst_list = LinkedList(['A', 'B'])
        self.assertEqual(circular_node(fst_list), None)
        fst_list.append_to_tail('C')
        fst_list.append_to_tail('D')
        fst_list.append_to_tail('E')
        fst_list.append_to_tail('F')
        loop_node = fst_list._head._next._next
        fst_list._tail._next = loop_node
        self.assertEqual(circular_node(fst_list), loop_node)

if __name__ == '__main__':
    unittest.main()