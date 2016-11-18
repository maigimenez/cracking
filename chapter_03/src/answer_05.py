class SortedStack:
    def __init__(self, unordered_list):
        self._stack = unordered_list

    def sort(self):
        sorted_stack = []
        while self._stack:
            tmp = self._stack.pop()
            if not sorted_stack:
                sorted_stack.append(tmp)
            else:
                while sorted_stack[-1] > tmp and sorted_stack:
                    self._stack.append(sorted_stack.pop())
                sorted_stack.append(tmp)

        self._stack = []
        while sorted_stack:
            self._stack.append(sorted_stack.pop())
        return self._stack

    def __repr__(self):
        return "->".join([str(data) for data in self._stack[::]])
