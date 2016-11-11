import unittest

from random import randrange, shuffle

from chapter_02.src.answer_03 import delete_node
from chapter_02.src.LinkedList import create_linked_list


class TestDeleteNode(unittest.TestCase):
    def test_delete_node(self):
        l = list(range(randrange(6, 10)))
        shuffle(l)
        l2 = [elem for elem in l]
        node = l[randrange(1, len(l) - 1)]
        l2.remove(node)
        ll = create_linked_list(l)
        delete_node(ll, node)
        self.assertEqual(ll.to_list(), l2)
