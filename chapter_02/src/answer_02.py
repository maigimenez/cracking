from chapter_02.src.LinkedList import LinkedList

# Time and space complexitty: O(n)
def get_kth(head, current_element, kth_element):
    if current_element == kth_element-1:
        k_linked = LinkedList()
        k_linked._head = head._next
        return k_linked
    else:
        return get_kth(head._next, current_element+1, kth_element)

def get_kth_last(linked_list, k_element):
    if linked_list is None or linked_list._head is None:
        return None

    return get_kth(linked_list._head, 0, k_element)

