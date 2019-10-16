PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    text = text.capitalize()
    for char in PYBITES:
        text = text.replace(char, char.upper())
    if text[0].lower() in PYBITES:
        text = text[0].lower() + text[1:]
    return text
