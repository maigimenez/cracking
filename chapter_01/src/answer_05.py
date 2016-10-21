def one_away(s1, s2):
    # Chech the number of differences between both strings
    difference = abs(len(s1) - len(s2))
    num_away, i, j = 0, 0, 0
    # Check if there is a modification
    if difference == 0:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_away += 1
                if num_away > 1:
                    return False
        return True
    # Check if there is an insertion or an elimination
    elif difference == 1:
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                num_away += 1
                if num_away > 1:
                    return False
                if s1[i+1] == s2[j]:
                    i += 1
                elif s1[i] == s2[j+1]:
                    j += 1
            else:
                i += 1
                j += 1

        return True
    return False
