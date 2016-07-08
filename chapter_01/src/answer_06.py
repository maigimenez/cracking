def compress(string_to_compress):
    if string_to_compress is None:
        return None
    if len(string_to_compress) == 0:
        return ""
    comp = [[string_to_compress[0], 1]]
    for char in string_to_compress[1:]:
        if comp[-1][0] == char:
            comp[-1][1] += 1
        else:
            comp.append([char, 1])
    if len(string_to_compress) <= len(comp)*2:
        return string_to_compress
    else:
        return "".join([str(letter[0])+str(letter[1]) for letter in comp])
