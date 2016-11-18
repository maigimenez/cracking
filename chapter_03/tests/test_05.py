from chapter_03.src.answer_05 import SortedStack
#In [1]: a = SortedStack(); a._stack = [7,10,5]
#In [1]: a.sort()

import unittest

class TestSortedStack(unittest.TestCase):
    def test_sort(self):
        a = SortedStack([7, 10, 5])
        self.assertEqual(a.sort(), [10, 7, 5])

if __name__=="__main__":
    unittest.main()
