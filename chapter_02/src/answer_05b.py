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

    carry_out = []
    while fst_pointer is not None:
        sum_elements = fst_pointer._data + snd_pointer._data
        if sum_elements >= 10:
            fst_pointer._data = sum_elements % 10
            carry_out.append(sum_elements // 10)
        else:
            fst_pointer._data = sum_elements
            carry_out.append(0)
        fst_pointer = fst_pointer._next
        snd_pointer = snd_pointer._next
    carry_out.append(0)

    fst_pointer = fst_list._head
    pos = 1
    while fst_pointer is not None:
        if carry_out[pos]:
            fst_pointer._data += carry_out[pos]
        fst_pointer = fst_pointer._next
        pos += 1

    return fst_list
