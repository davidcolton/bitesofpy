import re


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in text string
    """
    # Decided to go for finding non-ascii / non printable
    # Could not figure out the unicode - I have need at the moment either
    accents = set(re.sub("[\x00-\x7f]", "", text))
    return [acc.lower() for acc in accents]
