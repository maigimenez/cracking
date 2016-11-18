class QueueStack:
    def __init__(self):
        self._stack = []
        self._stack_tmp = None
        self._tmp_is_queue = False

    def push(self, data):
        if self._tmp_is_queue:
            self._stack = []
            while self._stack_tmp:
                self._stack.append(self._stack_tmp.pop())
            self._tmp_is_queue = False
        self._stack.append(data)

    def pop(self):
        if not self._tmp_is_queue:
            self._stack_tmp = []
            while len(self._stack) > 1:
                data_pop = self._stack.pop()
                self._stack_tmp.append(data_pop)
            self._tmp_is_queue = True
            return self._stack.pop()
        else:
            return self._stack_tmp.pop()

    def __repr__(self):
        if self._tmp_is_queue:
            return "[{}]".format('->'.join(self._stack_tmp))
        else:
            return "[{}]".format('->'.join(self._stack))

    def peek(self):
        if self._tmp_is_queue:
            return self._stack_tmp[-1]
        else:
            return self._stack[-1]