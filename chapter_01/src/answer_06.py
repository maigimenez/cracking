from collections import OrderedDict

def compress(string_to_compress):
    # There is not repeated characters and there is nothing to compress
    if len(string_to_compress) == len(set(string_to_compress)):
        return string_to_compress

    compressed_hash = OrderedDict()
    for character in string_to_compress:
        if character not in compressed_hash.keys():
            compressed_hash[character] = 1
        else:
            compressed_hash[character] += 1
    compressed_string = ''
    for key, value in compressed_hash.items():
        compressed_string += '{}{}'.format(key, str(value))

    return compressed_string
