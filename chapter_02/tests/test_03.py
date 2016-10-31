import unittest

from chapter_02.src.answer_03 import delete_node
from chapter_02.src.LinkedList import LinkedList


class TestDeleteNode(unittest.TestCase):
    def test_empty_list(self):
        self.assertIs(delete_node(None), False)

    def test_not_middle(self):
        linked_list = LinkedList([1,2,3,4])
        middle_node = linked_list.append_to_tail(5)
        self.assertEqual(delete_node(middle_node), False)

    def test_delete_node(self):
        linked_list = LinkedList([1,2,3,4])
        middle_node = linked_list.append_to_tail(5)
        linked_list.append_to_tail(6)
        linked_list.append_to_tail(7)
        delete_node(middle_node)
        self.assertEqual(linked_list, LinkedList([1,2,3,4,6,7]))

if __name__ == '__main__':
    unittest.main()
