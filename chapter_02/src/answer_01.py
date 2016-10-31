# With buffer:
# Time complexity: O(n)
# Space
# def remove_dups(dup_list):
#     if dup_list is None:
#         return None
#
#     if dup_list._head is None:
#         return dup_list
#
#     current_node = dup_list._head
#     seen_data = []
#
#     while current_node is not None:
#         if current_node._data in seen_data:
#             prev_node._next = current_node._next
#         else:
#             seen_data.append(current_node._data)
#             prev_node = current_node
#         current_node = current_node._next
#
#     return dup_list


def remove_dups(dup_list):
    if dup_list is None:
        return None

    if dup_list._head is None:
        return dup_list

    current_node = dup_list._head
    while current_node is not None:
        runner = current_node
        while runner._next is not None:
            if runner._next._data == current_node._data:
                runner._next = runner._next._next
            else:
                runner = runner._next
        current_node = current_node._next
    return dup_list