def is_palindrome_permutation(palindrome_permutation):
    if not palindrome_permutation:
        return False

    palindrome_hash = {}
    for character in palindrome_permutation:
        if character not in palindrome_hash.keys():
            palindrome_hash[character] = 1
        else:
            palindrome_hash[character] += 1

    an_odd_char = False
    for counts in palindrome_hash.values():
        if counts % 2 != 0:
            if an_odd_char:
                return False
            else:
                an_odd_char = True
    return True
