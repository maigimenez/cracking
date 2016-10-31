def delete_node(node_to_delete):
<<<<<<< 33a8a45b0d4a407a901bd2d99a710ce6fdb4ecfd
    pass 
=======
    if node_to_delete is None or node_to_delete._next is None:
        return False
    else:
        node_to_delete._data = node_to_delete._next._data
        node_to_delete._next = node_to_delete._next._next
        return True
>>>>>>> Solutions to the second chapter.
