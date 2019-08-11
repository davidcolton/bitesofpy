from string import punctuation

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return ''.join([c for c in input_string if c not it punctuation])