from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get("http://bit.ly/2EN2Ntv").text

Book = namedtuple("Book", "title description image link")


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, "html.parser")
    title = soup.find(class_="dotd-title").find("h2").text.strip()
    desc = soup.find(class_="dotd-main-book-summary").find_all("div")[2].text.strip()
    img = soup.find(class_="dotd-main-book-image").find("img").get("src")
    link = soup.find(class_="dotd-main-book-image").find("a").get("href")

    return Book(title, desc, img, link)
