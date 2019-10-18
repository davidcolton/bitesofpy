from functools import wraps


DEFAULT_TEXT = (
    "Subscribe to our blog (sidebar) to periodically get "
    "new PyBites Code Challenges (PCCs) in your inbox"
)
DOT = "."


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text"""

    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            strip_text = ""
            if start > len(kwargs["text"]):
                return func(*args, **kwargs)
            strip_range = list(range(start, end))
            for idx, char in enumerate(kwargs["text"]):
                if idx in strip_range:
                    strip_text += DOT
                else:
                    strip_text += char
            return func(strip_text)

        return wrapper

    return real_decorator


@strip_range(2, 3)
def gen_output(text):
    print(text)


gen_output("hello")

