def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    front, _, remainder = text.strip().partition('"')
    quoted, _, end = remainder.strip().partition('"')
    return_str = front.strip().split(" ") + [quoted.strip()] + end.strip().split(" ")
    return list(filter(None, return_str))
