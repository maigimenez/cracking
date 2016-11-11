def delete_node(linked_list, node):
    n = linked_list.first
    while n.next is not None:
        if n.next.data == node:
            n.next = n.next.next
            return
        n = n.next
