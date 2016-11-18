import unittest

from chapter_03.src.answer_04 import QueueStack

class TestQueueStack(unittest.TestCase):
    def test_push(self):
        queue_stacks = QueueStack()
        queue_stacks.push('a')
        self.assertEqual('a', queue_stacks.peek())
        queue_stacks.push('b')
        self.assertEqual('b', queue_stacks.peek())
        queue_stacks.push('c')
        self.assertEqual('c', queue_stacks.peek())
        queue_stacks.push(42)
        self.assertEqual(42, queue_stacks.peek())

    def test_pop(self):
        queue_stacks = QueueStack()
        queue_stacks.push('a')
        queue_stacks.push('b')
        queue_stacks.push('c')

        popped = queue_stacks.pop()
        self.assertEqual('a', popped)
        popped = queue_stacks.pop()
        self.assertEqual('b', popped)
        popped = queue_stacks.pop()
        self.assertEqual('c', popped)


if __name__== "__main__":
    unittest.main()