from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        attempts = 1
        while attempts <= MAX_RETRIES:
            try:
                func(*args, **kwargs)
            except Exception as exp:
                print(exp)
                attempts += 1
                if attempts > 3:
                    raise MaxRetriesException
                else:
                    continue
            return

    return wrapper
