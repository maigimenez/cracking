class Node:
    def __init__(self, int_data=None):
        self._next = None
        self._data = int_data

    def __str__(self):
        print("{}".format(self._data))


class LinkedList(object):

    def __init__(self, list_ints=None):
        # TODO Make this protected (@property)
        self._head = None
        self._tail = None
        if list_ints:
            for int_data in list_ints:
                self.append_to_tail(int_data)

    def append_to_tail(self, int_data):
        """ Add a new node with the data at the end of the Linked List """
        last_node = Node(int_data)
        if not self._head:
            self._head = last_node
            self._tail = last_node
        else:
            current_node = self._head
            while current_node._next is not None:
                current_node = current_node._next
            current_node._next = last_node
            self._tail = last_node
        return last_node

    def append_node(self, new_node):
        """ Add a the new node passed at the end of the Linked List """
        if not self._head:
            self._head = new_node
        else:
            current_node = self._head
            while current_node._next is not None:
                current_node = current_node._next
            current_node._next = new_node

    def append_list(self, tail_list):
        current_node = self._head
        while current_node._next is not None:
            current_node = current_node._next
        current_node._next = tail_list._head

    def delete_node(self, int_data):
        """ It deletes every node with the int_data as value"""
        current_node = self._head
        if current_node._data == int_data:
            self._head = self._head._next
        else:
            while current_node._next is not None:
                if current_node._next._data == int_data:
                    current_node._next = current_node._next._next
                current_node = current_node._next

    def __str__(self):
        if not self._head:
            return "{->}"
        current_node = self._head
        str_rep = "{"
        while current_node._next is not None:
            str_rep += "{}->".format(current_node._data)
            current_node = current_node._next
        str_rep += "{}".format(current_node._data)
        return str_rep+"}"

    def __eq__(self, other):
        fst_node = self._head
        snd_node = other._head

        # Comparing an empty list
        if self._head is None and other._head is None:
            return True

        # Comparing non empty lists
        while fst_node._next is not None:
            if fst_node._data != snd_node._data:
                return False
            fst_node = fst_node._next
            snd_node = snd_node._next
        if fst_node._data != snd_node._data:
            return False
        if snd_node._next is not None:
            return False
        return True
