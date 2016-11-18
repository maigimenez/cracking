import unittest

from chapter_03.src.answer_01 import TripleStack


class TestTripleStack(unittest.TestCase):
    def test_add_item(self):
        stack = TripleStack(5)

        stack.push('a', 1)
        item_added = stack.peek(1)
        self.assertEqual(item_added, 'a')

        stack.push('b', 2)
        item_added = stack.peek(1)
        self.assertEqual(item_added, 'a')

        stack.push('c', 1)
        item_added = stack.peek(1)
        self.assertEqual(item_added, 'c')

    def test_remove_item_full(self):
        stack = TripleStack(5)
        stack.push('a', 1)
        stack.push('b', 1)
        stack.push('c', 1)
        stack.push('d', 2)
        stack.pop(1)
        last_item = stack.peek(1)
        self.assertEqual(last_item, 'b')

    def test_remove_item_emptied(self):
        stack = TripleStack(5)
        stack.push('a', 1)
        stack.push('b', 1)
        stack.push('c', 1)
        stack.push('d', 2)
        stack.pop(2)
        last_item = stack.peek(2)
        self.assertEqual(last_item, None)

    def test_remove_item_empty(self):
        stack = TripleStack(5)

        stack.pop(3)
        last_item = stack.peek(2)
        self.assertEqual(last_item, None)

    def test_full_stack(self):
        stack = TripleStack(3)
        stack.push('a', 1)
        stack.push('b', 1)
        stack.push('c', 2)
        error = stack.push('d', 3)

        self.assertEqual(error, False)

    def test_empty(self):
        stack = TripleStack(5)
        self.assertEqual(stack.is_empty(), True)


    def test_not_empty(self):
        stack = TripleStack(5)
        stack.push('a', 1)
        stack.push('b', 1)
        stack.push('c', 2)
        self.assertEqual(stack.is_empty(), False)


if __name__ == '__main__':
    unittest.main()
