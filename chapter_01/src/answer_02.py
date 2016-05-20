def is_permutation(fst_str, snd_str):
    if not fst_str or not snd_str:
        return False
    a = list(fst_str)
    b = list(snd_str)
    a.sort()
    b.sort()
    return a == b
