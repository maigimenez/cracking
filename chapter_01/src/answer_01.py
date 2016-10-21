def unique_chars(s):
    # The pythonic approach
    # return len(s) == len(set(s))

    solution = []
    for character in s:
        if character not in solution:
            solution.append(character)
        else:
            return False
    return True
