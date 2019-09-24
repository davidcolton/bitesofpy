def get_index_different_char(chars):
    first_char = chars[0].isalnum()
    for ind, char in enumerate(chars):
        if first_char != char.isalnum():
            return ind
        
print(get_index_different_char(['A', 'f', '.', 'Q', 2]))
print(get_index_different_char(['.', '{', ' ^', '%', 'a']))