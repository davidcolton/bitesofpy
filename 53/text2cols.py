import textwrap
from itertools import zip_longest

COL_WIDTH = 20

str_1 = """My house is small but cosy."""

str_2 = """My house is small but cosy.

    It has a white kitchen and an empty fridge."""

str_3 = """My house is small but cosy.

    It has a white kitchen and an empty fridge.

    I have a very comfortable couch, people love to sit on it."""

str_4 = """My house is small but cosy.

    It has a white kitchen and an empty fridge.

    I have a very comfortable couch, people love to sit on it.

    My mornings are filled with coffee and reading, if only I had a garden"""


def _pad(my_list, n, fillvalue=""):
    # Padding to include empty values like this means
    #   that I don't need to worry about index exceptions
    return my_list + [fillvalue] * (n - len(my_list))


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    # Split the text into lines
    lines = text.split("\n\n")

    # Split each line into fixed width snippets
    wrapped_lines = [textwrap.wrap(line.strip(), COL_WIDTH) for line in lines]

    # Get the max lines in any snippet and number of snippets
    # And pad each list
    num_snippets = len(wrapped_lines)
    max_length = max([len(i) for i in wrapped_lines])
    wrapped_lines = [_pad(line, max_length) for line in wrapped_lines]

    # Transpose in preparation for printing
    transposed_lines = list(map(list, zip_longest(*wrapped_lines)))

    # Now construct a string to return
    return_str = f""
    for line in transposed_lines:
        print_line = f""
        for snippet in line:
            print_line += f"{snippet:<22}"
        return_str = return_str + print_line + "\n"
    return return_str


# text_to_columns(str_1)
# text_to_columns(str_2)
# text_to_columns(str_3)
# text_to_columns(str_4)
