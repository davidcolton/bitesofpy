import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
if not os.path.exists(DICTIONARY):
    urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY, 'r') as f:
        words = f.read()
    return [w for w in words.split('\n') if w != '']


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    try:
        return sum([LETTER_SCORES[c.upper()] for c in word])
    except KeyError:
        return 0


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    scores = {calc_word_value(word): word for word in words}
    return scores[max(scores)]