def is_substring(s1, s2):
    return s2.find(s1) >= 0


def string_rotation(s1, s2):
    if len(s1) == len(s2):
        twos1 = s1 + s1
        return is_substring(s2, twos1)
    return False
