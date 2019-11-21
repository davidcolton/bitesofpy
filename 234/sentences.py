import re


def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    # Split into sentences. Therefore, find all text that ends
    # with punctuation followed by white space or end of string.
    sentences = re.findall("[^.!?]+[.!?](?:\s|\Z)", text)

    # Capitalize the first letter of each sentence
    sentences = [x[0].upper() + x[1:] for x in sentences]

    # Combine sentences
    return "".join(sentences)

