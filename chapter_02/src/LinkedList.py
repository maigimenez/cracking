class Node:
    def __init__(self, int_data=None):
        self._next = None
        self._data = int_data

    def __str__(self):
        print("{}".format(self._data))


class LinkedList(object):

    def __init__(self):
        # TODO Make this protected (@property)
        self._head = None

    def append_to_tail(self, int_data):
        """ Add a new node at the end of the Linked List """
        last_node = Node(int_data)
        if not self._head:
            self._head = last_node
        else:
            current_node = self._head
            while current_node._next is not None:
                current_node = current_node._next
            current_node._next = last_node

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