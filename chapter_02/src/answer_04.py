from chapter_02.src.LinkedList import LinkedList

def get_partition(partition, x):
    if not partition:
        return None

    lower, upper = LinkedList(), LinkedList()
    current_node = partition._head
    while current_node is not None:
        if current_node._data < x:
            lower.append_to_tail(current_node._data)
        else:
            upper.append_to_tail(current_node._data)

        current_node = current_node._next

    point_to_last = lower._head
    while point_to_last._next is not None:
        point_to_last = point_to_last._next
    point_to_last._next = upper._head

    return lower
