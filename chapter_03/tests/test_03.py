import unittest

from chapter_03.src.answer_03 import SetOfStacks

class TestStackMin(unittest.TestCase):
    def test_push(self):
        set_stacks = SetOfStacks(2)
        set_stacks.push(1)
        self.assertEqual(1, set_stacks.peek())
        set_stacks.push(2)
        self.assertEqual(2, set_stacks.peek())
        set_stacks.push(3)
        self.assertEqual(3, set_stacks.peek())
        # TODO: This is not generic enough
        self.assertEqual(1, set_stacks._current_stack)

    def test_pop(self):
        set_stacks = SetOfStacks(2)
        set_stacks.push(1)
        set_stacks.push(2)
        set_stacks.push(3)
        set_stacks.push(4)
        set_stacks.push(5)

        set_stacks.pop()
        self.assertEqual(4, set_stacks.peek())
        set_stacks.pop()
        self.assertEqual(3, set_stacks.peek())
        set_stacks.pop()
        self.assertEqual(2, set_stacks.peek())
        set_stacks.pop()
        self.assertEqual(1, set_stacks.peek())
        set_stacks.pop()
        self.assertIs(True, set_stacks.is_empty())
        set_stacks.push(1)
        self.assertEqual(1, set_stacks.peek())

if __name__ == '__main__':
    unittest.main()
