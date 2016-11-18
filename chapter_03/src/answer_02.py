class Node:
    def __init__(self, data, minimum):
        self._data = data
        self._min = minimum

    def __str__(self):
        return str(self._data)


class StackMin:
    def __init__(self):
        self._stack = []
        self._current_min = None

    def push(self, data):
        if not self._current_min:
            self._current_min = data
        elif data <= self._current_min:
            self._current_min = data
        new_node = Node(data, self._current_min)
        self._stack.append(new_node)

    def pop(self):
        value_deleted = self._stack[-1]._data
        self._stack.pop()
        if value_deleted == self._current_min:
            if self._stack:
                self._current_min = self._stack[-1]._min
            else:
                self._current_min = None
        return value_deleted

    def __str__(self):
        if self._stack:
            stack_str = "-> Stack: {} \n".format(','.join([str(node._data) for node in self._stack]))
            stack_str += "-> Minimum is: {}\n".format(self._current_min)
        else:
            stack_str = "Empty Stack"
        return stack_str

    def get_min(self):
        return self._current_min

    def is_empty(self):
        return not self._stack

    def peek(self):
        if not self.is_empty():
            return self._stack[-1]._data
        return None