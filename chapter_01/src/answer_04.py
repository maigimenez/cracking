def is_palindrome_permutation(palindrome_permutation):
    if palindrome_permutation:
        freq = {}
        for char in palindrome_permutation:
            if char != ' ':
                if char not in freq:
                    freq[char] = 1
                else:
                    freq[char] += 1
        odd_f = [f for f in freq.values() if f%2 == 1]
        if len(odd_f) < 2:
            return True
    return False
