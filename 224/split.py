import re
from itertools import combinations

TEXT_WITH_DOTS = """
We are looking forward attending the next Pycon in the U.S.A.
in 2020. Hope you do so too. There is no better Python networking
event than Pycon. Meet awesome people and get inspired. Btw this
dot (.) should not end this sentence, the next one should. Have fun!
"""


def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    # A pattern where to split the string
    pattern = re.compile(r"[.?!]{1}\s{1}[A-Z]{1}")

    # A list of breakpoints to split the text on
    # Add 0 to the front and the overall length of the text to the end
    bps = [0]
    bps += [m.start(0) + 1 for m in re.finditer(pattern, text)]
    bps += [len(text)]

    # Iterate over a the list of breakpoints.
    #   Minus 1 so that we don't get an index error
    #   Would like to make this nicer using std lib or something.
    return_list = []
    for n in range(0, len(bps) - 1):
        return_list.append((text[bps[n] : bps[n + 1]]).replace("\n", " ").strip())

    return return_list


# get_sentences(TEXT_WITH_DOTS)
