from chapter_02.src.LinkedList import LinkedList, ElementList


def get_partition(linked_list, x):
    res = LinkedList()
    n = linked_list.first
    while n is not None:
        if n.data < x:
            new_first = ElementList(n.data)
            new_first.next = res.first
            res.first = new_first
            if res.last is None:
                res.last = new_first
        else:
            res.append(n.data)
        n = n.next
    return res
