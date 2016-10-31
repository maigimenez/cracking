def circular_node(circular_list):
    # There is no list
    if circular_list is None or circular_list._head is None:
        return None
    # There is only one node
    if circular_list._head._next is None:
        return None

    current_node = circular_list._head
    runner_node = circular_list._head._next
    there_is_loop = False
    while current_node and runner_node._next and not there_is_loop:
        if runner_node == current_node:
            there_is_loop = True
        # Check if there is a next runner node
        if runner_node._next is not None and runner_node._next._next is not None:
            runner_node = runner_node._next._next
        else:
            return None
        current_node = current_node._next
    fst_node = circular_list._head

    while fst_node != runner_node._next:
        fst_node = fst_node._next

    return fst_node