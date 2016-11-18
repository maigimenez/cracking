class TripleStack:
    def __init__(self, size_stacks=20):
        self._stacks = {1:[], 2: [], 3: []}
        self._max = size_stacks

    def size_used(self):
        return sum([len(stack) for stack in self._stacks.values()])

    def size_exceeded(self):
        total_size = self.size_used()
        if total_size >= self._max:
            return True
        return False

    def push(self, data, stack_num=1):
        try:
            if not self.size_exceeded():
                self._stacks[stack_num].append(str(data))
            else:
                raise ValueError('The stacks are full.')
        except (ValueError, IndexError):
            # For testing purposes
            return False

    def pop(self, stack_num):
        try:
            if not self.is_empty(stack_num):
                self._stacks[stack_num].pop()
            else:
                raise ValueError('This stack is empty.')
        except (ValueError, IndexError):
            # For testing purposes
            return False

    def peek(self, stack_num=1):
        if not self.is_empty(stack_num):
            return self._stacks[stack_num][-1]
        return None

    def is_empty(self, stack_num=None):
        if stack_num:
            if len(self._stacks[stack_num]) == 0:
                return True
            else:
                return False
        if self.size_used() == 0:
            return True
        else:
            return False

    def __str__(self):
        stack_str = ""
        for stack_num, values in self._stacks.items():
            stack_str += "({}): {} \n".format(stack_num, ','.join(values))
        stack_str += "-> Max Size: {}\n".format(self._max)
        stack_str += "-> Used Size: {}\n".format(self.size_used())
        return stack_str