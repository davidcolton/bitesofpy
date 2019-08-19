"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import string
import urllib.request

DICTIONARY = os.path.join("/tmp", "dictionary_m_words.txt")
if not os.path.exists(DICTIONARY):
    urllib.request.urlretrieve("http://bit.ly/2Cbj6zn", DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    # convert to lowercase
    word = word.lower()

    # Remove chars that are not alphanumeric, including spaces
    word = "".join(c for c in word if c in string.ascii_letters or c in string.digits)

    return word == word[::-1]


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    if words is None:
        words = list(load_dictionary())
    words.sort(key=len, reverse=True)
    for test_word in words:
        if is_palindrome(test_word):
            return test_word
