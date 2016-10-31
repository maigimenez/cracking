from math import floor

def is_palindrome(pal_list):
    if pal_list is None:
        return None
    if pal_list._head is None or pal_list._head._next is None:
        return True

    num_elements = 0
    head_pointer = pal_list._head
    letter_stack = []
    while head_pointer is not None:
        num_elements += 1
        letter_stack.append(head_pointer._data)
        head_pointer = head_pointer._next

    head_pointer = pal_list._head
    num_different = 0
    half = floor(num_elements / 2)
    if num_different % 2:
        half -= 1

    for current_comparation in range(half):
        last_letter = letter_stack.pop()
        if last_letter != head_pointer._data:
            num_different += 1
        if num_different > 1:
            return False
        head_pointer = head_pointer._next

    if num_different == 0:
        return True
    return False