import emoji
import re
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = re.compile(r"[^\w\s,]")


def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    ## Create the function to extract the emojis
    # Find all the emoji's
    emojis_list = map(lambda x: "".join(x.split()), emoji.UNICODE_EMOJI.keys())
    r = re.compile("|".join(re.escape(p) for p in emojis_list))
    return [idx for idx, e in enumerate(text) if e in r.findall(text)]

