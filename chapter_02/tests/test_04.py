import unittest

from random import shuffle, randrange

from chapter_02.src.answer_04 import get_partition
from chapter_02.src.LinkedList import create_linked_list


class TestPartition(unittest.TestCase):
    def test_partition(self):
        l = list(range(10))
        shuffle(l)
        ll = create_linked_list(l)
        k = randrange(-2,12)
        pl = get_partition(ll, k)
        right = False
        print(pl.to_list(), k)
        for e in pl.to_list():
            if e >= k:
                right = True
            if right:
                self.assertGreaterEqual(e, k)
            else:
                self.assertLess(e, k)
