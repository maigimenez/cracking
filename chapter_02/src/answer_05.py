def sum_lists(fst_list, snd_list):

    if fst_list is None or snd_list is None:
        return None

    if fst_list._head is None and snd_list._head is None:
        return fst_list
    elif fst_list._head is None and snd_list._head is not None:
        return snd_list
    elif fst_list._head is not None and snd_list._head is None:
        return fst_list

    fst_pointer = fst_list._head
    snd_pointer = snd_list._head

    carry_out = 0
    while fst_pointer is not None:
        sum_elements = fst_pointer._data + snd_pointer._data + carry_out
        if sum_elements >= 10:
            fst_pointer._data = sum_elements % 10
            carry_out = sum_elements // 10
        else:
            fst_pointer._data = sum_elements
        fst_pointer = fst_pointer._next
        snd_pointer = snd_pointer._next

    return fst_list
