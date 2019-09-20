from collections import Counter

from bs4 import BeautifulSoup
import requests
import re

AMAZON = "amazon.com"
TIM_BLOG = "https://bit.ly/2NBnZ6P"


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode("utf-8")


def a_amazon(href):
    return href and re.compile(AMAZON).search(href)


def get_top_books(content=None, limit=5):
    """Make a BeautifulSoup object loading in content,
       find all links and filter on AMAZON, extract the book title
       and count them, return the top "limit" books (default 5)"""
    popular_count = Counter()
    if content is None:
        content = load_page()
    soup = BeautifulSoup(content, "html.parser")
    amazon_links = soup.find_all(href=a_amazon)
    for link in amazon_links:
        try:
            popular_count[link.i.span.text] += 1
        except AttributeError:
            # No details in the Amazon link.
            pass

    return [book_name for book_name, count in popular_count.most_common(5)]
