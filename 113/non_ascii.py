def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    non_ascii_words = dict()
    for word in text.split():
        for char in word:
            if ord(char) > 127:
                # Would prefer to use set but tests expect
                #   list in certain order
                non_ascii_words[word] = None

    return list(non_ascii_words.keys())
