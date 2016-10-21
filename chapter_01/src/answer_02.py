def is_permutation(fst_str, snd_str):
    """
    Questions to ask:
    - Is it case sensitive?
    - Do whitespaces matter?
    Hints:
    - Strings with two different sizes cannot be permutations.
    """
    if not fst_str or not snd_str:
        return False
    if len(fst_str) != len(snd_str):
        return False
    if fst_str and snd_str:
        return sorted(fst_str) == sorted(snd_str)
    return None
