from collections import namedtuple

from bs4 import BeautifulSoup
import requests
import re

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
page_01 = "https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html"
page_02 = "https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html"

Entry = namedtuple("Entry", "title points comments")


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url=page_02, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)

    # Get all the titles in a list
    titles = [
        title.get_text().strip() for title in soup.find_all("span", {"class": "title"})
    ]

    # Regular expression patterns to find points and comments
    find_points_pattern = re.compile(r"(\d{1,2}) point")
    find_comments_pattern = re.compile(r"(\d{1,2}) comment")

    # Create the soup objects that contains the points and comments
    others = soup.find_all("span", {"class": "controls"})

    # Get all the points in a list
    points = [
        int(
            find_points_pattern.findall(
                other.find("span", {"class": "smaller"}).get_text()
            )[0]
        )
        for other in others
    ]

    # Get all the comments in a list
    comments = [
        int(
            find_comments_pattern.findall(
                other.find("span", {"class": "smaller"}).get_text()
            )[0]
        )
        for other in others
    ]

    # Create the final list of entries and sort
    sorted_entries = sorted(
        [Entry(*e) for e in zip(titles, points, comments)],
        key=lambda k: (-k.points, -k.comments),
    )

    # Return the amount required
    return sorted_entries[:top]
