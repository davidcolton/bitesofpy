def get_index_different_char_orig(chars):
    first_char = str(chars[0]).isalnum()
    for ind, char in enumerate(chars):
        if first_char != str(char).isalnum():
            return ind


def get_index_different_char(chars):
    # A list of 0,1's representing whether each char is alphanum or not
    #   1 if it is alphanum
    #   0 if not alphanum
    #   e.g. ['A', 'f', '.', 'Q', 2] = [1, 1, 0, 1, 1]
    num_alnum = [1 if str(char).isalnum() else 0 for char in chars]

    # If the sum of the array of ints == 1 this implies a single alphanum
    #   Return the index of the only 1 in the array
    # If the  sum of the array of ints > 1 this implies a single non alphanum
    #   Return the index of the only 0 in the array
    return num_alnum.index(1) if sum(num_alnum) == 1 else num_alnum.index(0)
