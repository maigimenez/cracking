def remove_dups(dlist):
    # # Using a temporary buffer
    # duplicates = set()
    # n = dlist.first
    # if n is not None:
    #     duplicates.add(n.data)
    #     while n.next is not None:
    #         if n.next.data not in duplicates:
    #             duplicates.add(n.next.data)
    #         else:
    #             n.next = n.next.next
    # return dlist

    n = dlist.first
    pos_n = 0
    while n is not None:
        prev = dlist.first
        pos_prev = 0
        dup = False
        while pos_prev < pos_n:
            if n.data == prev.data:
                dup = True
            prev = prev.next
            pos_prev += 1
        if dup:
            prev.next = prev.next.next
        else:
            pos_n += 1
        n = n.next
    return dlist
