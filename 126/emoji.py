import sys
import unicodedata


START_EMOJI_RANGE = 100000  # estimate


def what_means_emoji(emoji):
    """Receives emoji and returns its meaning,
       in case of a TypeError return 'Not found'"""
    try:
        return unicodedata.name(emoji)
    except TypeError:
        return "Not found"


def _make_emoji_mapping():
    """Helper to make a mapping of all possible emojis:
       - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
       - return dict with keys=emojis, values=names"""
    emoji_dict = dict()
    for emoji in range(START_EMOJI_RANGE, sys.maxunicode + 1):
        try:
            emoji_dict[chr(emoji)] = unicodedata.name(chr(emoji)).lower()
        except ValueError:
            pass
    return emoji_dict


def find_emoji(term):
    """Return emojis and their texts that match (case insensitive)
       term, print matches to console"""
    emoji_dict = _make_emoji_mapping()
    emoji_name_lengths = []
    emojis_found = {}
    for emoji, emoji_name in emoji_dict.items():
        if term.lower() in emoji_name.lower():
            emoji_name_lengths.append(len(emoji_name))
            emojis_found[emoji_name.strip()] = emoji.strip()
    if len(emojis_found) == 0:
        print("no matches")
    else:
        for name, emoji in emojis_found.items():
            print(f"{name.title(): <{max(emoji_name_lengths)}} | {emoji}")

