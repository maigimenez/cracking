def delete_node(node_to_delete):
    if node_to_delete is None or node_to_delete._next is None:
        return False
    else:
        node_to_delete._data = node_to_delete._next._data
        node_to_delete._next = node_to_delete._next._next
        return True
