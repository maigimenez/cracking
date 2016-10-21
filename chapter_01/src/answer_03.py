import re

def urlify(s, length):
    if not s:
        return []

    # Kind of the pythonic wat
    s = ''.join(s)
    return list(re.sub(r'\s', '%20', s.strip()))

    # String manipulation
    # solution = []
    # num_chars = 0
    # for character in s:
    #     if character == ' ':
    #         solution.extend(['%', '2', '0'])
    #     elif character != ' ':
    #         solution.append(character)
    #     num_chars += 1
    #
    #     if num_chars == length:
    #         return solution
