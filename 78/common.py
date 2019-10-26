def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    languages = programmers.values()
    return set.intersection(*[set(lang) for lang in languages])
