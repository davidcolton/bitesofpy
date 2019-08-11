import re

VOWELS = 'aeiou'
PYTHON = 'python'
DIGITS = 'D1git5'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return all([x in VOWELS for x in input_str.lower()])


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    py_pat = '|'.join([x for x in PYTHON])
    return bool(re.search(py_pat, input_str, re.IGNORECASE))


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return bool(re.search(r'\d', input_str))