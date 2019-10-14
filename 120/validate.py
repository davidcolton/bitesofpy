from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not all([isinstance(x, int) for x in args]):
            raise TypeError
        if any([x < 0 for x in args]):
            raise ValueError
        return func(*args, **kwargs)

    return wrapper
