import os
import urllib.request
from collections import defaultdict

LOG = os.path.join("/tmp", "safari.logs")
PY_BOOK, OTHER_BOOK = "🐍", "."
if not os.path.exists(LOG):
    urllib.request.urlretrieve("http://bit.ly/2BLsCYc", LOG)

# Use a default dictionary for the daily book count
book_count = defaultdict(list)


def create_chart():
    # Read the lines of the log
    with open(LOG, "r") as f:
        lines = f.readlines()

    # Iterate over the lines using enumerate
    for num, line in enumerate(lines):
        if line.strip().endswith("- sending to slack channel"):
            prev_line = lines[num - 1].strip()
            book_date = prev_line.split(" ")[0]
            book_title = prev_line.split(" - ")[1]
            if "Python" in book_title:
                book_count[book_date].append(PY_BOOK)
            else:
                book_count[book_date].append(OTHER_BOOK)

    for key, item in dict(book_count).items():
        print(key, "".join(item))
