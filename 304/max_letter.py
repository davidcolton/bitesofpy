from typing import Tuple
from collections import Counter
import re


def max_letter_word(text) -> Tuple[str, str, int]:
    """
    Find the word in text with the most repeated letters. If more than one word
    has the highest number of repeated letters choose the first one. Return a
    tuple of the word, the (first) repeated letter and the count of that letter
    in the word.
    >>> max_letter_word('I have just returned from a visit...')
    ('returned', 'r', 2)
    >>> max_letter_word('$5000 !!')
    ('', '', 0)
    """
    max_word = ""
    max_letter = ""
    max_count = 0
    if isinstance(text, str):
        for idx, word in enumerate(text.split()):
            most_frequent = Counter(
                "".join(filter(str.isalpha, word.casefold()))
            ).most_common(1)
            try:
                letter, cnt = most_frequent[0]
                if cnt > max_count:
                    max_word = word
                    max_letter = letter
                    max_count = cnt
            except IndexError:
                pass
    else:
        raise ValueError
    max_word = "".join([c for c in max_word if c.isalpha() or c in ["'", "-"]])
    return (max_word, max_letter, max_count)

