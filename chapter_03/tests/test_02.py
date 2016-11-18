import unittest

from chapter_03.src.answer_02 import StackMin


class TestStackMin(unittest.TestCase):
    def test_add_item(self):
        stack = StackMin()

        stack.push(5)
        item_added = stack.peek()
        self.assertEqual(item_added, 5)
        self.assertEqual(stack.get_min(), 5)

        stack.push(6)
        item_added = stack.peek()
        self.assertEqual(item_added, 6)
        self.assertEqual(stack.get_min(), 5)

        stack.push(3)
        item_added = stack.peek()
        self.assertEqual(item_added, 3)
        self.assertEqual(stack.get_min(), 3)

        stack.push(7)
        item_added = stack.peek()
        self.assertEqual(item_added, 7)
        self.assertEqual(stack.get_min(), 3)

    def test_remove_items(self):
        stack = StackMin()
        stack.push(5)
        stack.push(6)
        stack.push(3)
        stack.push(7)

        value_deleted = stack.pop()
        self.assertEqual(value_deleted, 7)
        self.assertEqual(stack.get_min(), 3)

        value_deleted = stack.pop()
        self.assertEqual(value_deleted, 3)
        self.assertEqual(stack.get_min(), 5)

        value_deleted = stack.pop()
        self.assertEqual(value_deleted, 6)
        self.assertEqual(stack.get_min(), 5)

    def test_empty(self):
        stack = StackMin()
        stack.push(5)

        value_deleted = stack.pop()
        self.assertEqual(value_deleted, 5)
        self.assertIs(stack.get_min(), None)


if __name__ == '__main__':
    unittest.main()
