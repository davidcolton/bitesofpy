import string
from typing import List
from itertools import tee, zip_longest

from textwrap import dedent


def split_once(text: str, separators: str = None) -> List[str]:

    # Set sepatators to whitespace if None, makes everything else generic
    separators = (
        [w for w in string.whitespace]
        if separators == None
        else [c for c in separators]
    )

    # Determine if there any of the separators are present in the text
    # If not then 'indices' is None
    try:
        indices = sorted([text.index(s) for s in separators if s in text])
    except ValueError:
        indices = None

    # Handle edge cases where no text ot no separator found
    if not text:
        return [""]
    elif not separators or not indices:
        return [text]

    # Manually handle indices to break and strip split character
    # Add 0 index to the list of start indices
    start_indices = [0] + indices

    # The length of the text and the last index of the closing indices
    end_indices = indices + [len(text)]

    # Zip the indices together to make a start - end index tuple
    indices_tuples = list(zip(start_indices, end_indices))

    # Correct the indices so that the split character is stripped out
    correct_indices = [
        (t[0], t[1]) if t[0] == 0 and e == 0 else (t[0] + 1, t[1])
        for e, t in enumerate(indices_tuples)
    ]

    # Return the split text
    return [text[h[0] : h[1]] for h in correct_indices]
