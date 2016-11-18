class SetOfStacks:
    def __init__(self, capacity=5):
        self._stacks = [[]]
        self._max_capacity = capacity
        self._current_stack = 0
        self._not_full_stacks = {}

    def is_empty(self):
        return self._stacks == []

    def is_full(self):
        if not self._stacks:
            self._stacks = [[]]
            return False
        return len(self._stacks[self._current_stack]) == self._max_capacity

    def push(self, data):
        if self._not_full_stacks:
            stack_not_full = sorted(self._not_full_stacks.keys())[0]
            self._stacks[stack_not_full].append(data)
            print(stack_not_full)
            if self._not_full_stacks[stack_not_full] == 1:
                del self._not_full_stacks[stack_not_full]
            else:
                self._not_full_stacks[stack_not_full] -= 1
        elif self.is_full():
            self._current_stack += 1
            self._stacks.append([data])
        else:
            self._stacks[self._current_stack].append(data)

    def pop(self):
        if self._stacks:
            deleted_node = self._stacks[self._current_stack][-1]
            self._stacks[self._current_stack].pop()
            if not self._stacks[self._current_stack]:
                del self._stacks[self._current_stack]
                self._current_stack -= 1
            return deleted_node
        return None

    def popAt(self, index):
        if index == self._current_stack:
            return self.pop()
        elif index < self._current_stack:
            deleted_node = self._stacks[index][-1]
            self._stacks[index].pop()
            if index in self._not_full_stacks:
                self._not_full_stacks[index] += 1
            else:
                self._not_full_stacks[index] = 1
            return deleted_node
        else:
            raise ValueError('This stack does not exist')

    def peek(self):
        return self._stacks[self._current_stack][-1]

    def __str__(self):
        stack_str = ""
        for i, stack_set in enumerate(self._stacks):
            stack_str += "({}): {}\n".format(i, ','.join([str(item) for item in stack_set]))
        return stack_str