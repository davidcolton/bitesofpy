from functools import wraps


def make_html(element):
    def decorator(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            return f"<{element}>{fn(*args, **kwargs)}</{element}>"

        return wrapped

    return decorator


def get_text(text="I code with PyBites"):
    return text
