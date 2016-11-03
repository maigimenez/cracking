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


def create_linked_list(self, pylist):
    l = LinkedList()
    for elem in pylist:
        l.append(elem)
    return l
