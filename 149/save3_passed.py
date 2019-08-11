import string

def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case,
       one twist: numbers have to appear after letters!"""
    # Split and sort the words by lower case
    words_sorted = sorted(words, key=str.lower)
    
    #Get the index of the first non digit
    i = [not x[0] in string.digits for x in words_sorted].index(True)
    
    # Use slicing to return required order
    # This is done by swaping the two parts of the list
    #     around the index of the first non digit entry
    return words_sorted[i:] + words_sorted[:i]