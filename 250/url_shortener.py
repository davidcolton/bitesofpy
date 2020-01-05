from math import floor
from string import ascii_lowercase, ascii_uppercase, digits
from typing import Dict

CODEX: str = digits + ascii_lowercase + ascii_uppercase
BASE: int = len(CODEX)
# makeshift database record
LINKS: Dict[int, str] = {
    1: "https://pybit.es",
    45: "https://pybit.es/pages/articles.html",
    255: "http://pbreadinglist.herokuapp.com",
    600: "https://pybit.es/pages/challenges.html",
    874: "https://stackoverflow.com",
}
SITE: str = "https://pybit.es"

# error messages
INVALID = "Not a valid PyBites shortened url"
NO_RECORD = "Not a valid shortened url"


def encode(record: int) -> str:
    """Encodes an integer into Base62"""

    if record == 0:
        return [record]
    encoded_str = []
    dividend = record
    while dividend > 0:
        dividend, remainder = divmod(dividend, BASE)
        encoded_str.insert(0, CODEX[remainder])
    return "".join(c for c in encoded_str)


def decode(short_url: str) -> int:
    """Decodes the Base62 string into a Base10 integer"""
    val_hash = []
    for char in short_url:
        val_hash.append(CODEX.index(char))
    val_hash = list(reversed(val_hash))

    int_id = 0
    for idx, val in enumerate(val_hash):
        int_id += val * (BASE ** idx)
    return int_id


def redirect(url: str) -> str:
    """Retrieves URL from shortened DB (LINKS)

    1. Check for valid domain
    2. Check if record exists
    3. Return URL stored in LINKS or proper message
    """
    if not url.startswith(SITE):
        return INVALID
    index = decode(url.split("/")[-1])
    if not index in LINKS:
        return NO_RECORD
    else:
        return LINKS[index]


def shorten_url(url: str, next_record: int) -> str:
    """Shortens URL and updates the LINKS DB

    1. Encode next_record
    2. Adds url to LINKS
    3. Return shortened URL
    """
    shortened_url = encode(next_record)
    LINKS[next_record] = url
    return f"{SITE}/{shortened_url}"
