import re
import requests
from bs4 import BeautifulSoup
from operator import itemgetter

cached_so_url = "https://bit.ly/2IMrXdp"


def load_page(url):
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(url).content.decode("utf-8")


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    # An empty list for the questions
    questions_list = []

    # Load the html page
    content = load_page(url)
    soup = BeautifulSoup(content, "html.parser")

    # Extract the questions data and add to list
    most_up_voted = soup.find_all("div", {"class": "question-summary"})
    for snippet in most_up_voted:
        question = snippet.find("a", {"class": "question-hyperlink"}).get_text()
        votes = int(
            snippet.find("span", {"class": "vote-count-post"}).strong.get_text()
        )
        raw_views = snippet.find("div", {"class": re.compile(r"^views")})["title"]
        views = int(raw_views.replace(",", "").split(" ")[0])
        questions_list.append([views, (question, votes)])

    # Return the questions with > 1m views sorted by votes
    return sorted(
        [q for v, q in questions_list if v > 1000000], key=itemgetter(1), reverse=True
    )


print(top_python_questions())
