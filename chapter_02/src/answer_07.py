def is_intersection(fst_list, snd_list):
    if fst_list is None or snd_list is None:
        return None

    if fst_list._head is None or snd_list._head is None:
        return None

    current_node = fst_list._head

    while current_node is not None:
        compare_node = snd_list._head
        while compare_node is not None:
            if compare_node == current_node:
                return current_node
            compare_node = compare_node._next
        current_node = current_node._next
    return None
