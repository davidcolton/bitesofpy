from itertools import permutations
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join("/tmp", "dictionary.txt")
urllib.request.urlretrieve("http://bit.ly/2iQ3dlZ", DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    return [
        token.lower()
        for token in _get_permutations_draw(draw)
        if token.lower() in dictionary
    ]


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    return [
        "".join(word)
        for perm in range(1, len(draw) + 1)
        for word in list(permutations(draw, perm))
    ]

