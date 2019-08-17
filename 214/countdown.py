def countdown():
    """Write a generator that counts from 100 to 1"""
    countdown_range = range(100, 0, -1)
    for i in countdown_range:
        yield i
