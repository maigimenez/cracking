from chapter_02.src.LinkedList import LinkedList


def get_kth_last(linked_list, k):
    if linked_list.first is None:
        return None
    res = LinkedList()
    n = linked_list.first
    pos = 0
    while n is not None:
        if pos >= k:
            res.append(n.data)
        n = n.next
        pos += 1
    if pos < k:
        return None
    else:
        return res
