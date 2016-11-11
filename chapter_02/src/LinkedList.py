class ElementList():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.first = None
        self.last = None

    def append(self, elem):
        e = ElementList(elem)
        if self.first is None:
            self.first = e
            self.last = e
        else:
            self.last.next = e
            self.last = self.last.next

    def to_list(self):
        l = []
        node = self.first
        while node is not None:
            l.append(node.data)
            node = node.next
        return l


def create_linked_list(mylist):
    l = LinkedList()
    for elem in mylist:
        l.append(elem)
    return l
