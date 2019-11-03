from operator import itemgetter

VOWELS = list("aeiou")


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    word_tuples = []
    for word in text.split():
        word_tuples.append(
            (word, sum([1 if letter in VOWELS else 0 for letter in word]))
        )

    return max(word_tuples, key=itemgetter(1))
