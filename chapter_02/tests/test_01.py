import unittest

from random import randrange, shuffle

from chapter_02.src.answer_01 import remove_dups
from chapter_02.src.LinkedList import create_linked_list


class TestRemoveDups(unittest.TestCase):
    def test_empty_list(self):
        empty_ll = create_linked_list([])
        self.assertEqual(remove_dups(empty_ll).to_list(), [])

    def test_unique_list(self):
        l_aux = list(range(randrange(6,10)))
        shuffle(l_aux)
        l = create_linked_list(l_aux)
        l2 = remove_dups(l).to_list()
        self.assertEqual(l_aux.sort(), l2.sort())

    def test_duplicate_element(self):
        l = []
        for i in range(randrange(15,20)):
            l.append(randrange(10))
        l2 = remove_dups(create_linked_list(l)).to_list()
        self.assertEqual(l.sort(), l2.sort())
