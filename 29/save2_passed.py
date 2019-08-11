def get_index_different_char(chars):
    first_char = str(chars[0]).isalnum()
    for ind, char in enumerate(chars):
        if first_char != str(char).isalnum():
            return ind
