import os
import re
import urllib.request
from collections import Counter

# data provided
stopwords_file = os.path.join("/tmp", "stopwords")
harry_text = os.path.join("/tmp", "harry")
if not os.path.exists(stopwords_file):
    urllib.request.urlretrieve("http://bit.ly/2EuvyHB", stopwords_file)
if not os.path.exists(harry_text):
    urllib.request.urlretrieve("http://bit.ly/2C6RzuR", harry_text)

stopwords, harrywords = [], []

count_words = Counter()


def _keep_word(word):
    return bool(re.match("^[a-zA-Z0-9]+$", word)) and word not in stopwords


def get_harry_most_common_word():
    # Read in the stop words
    with open(stopwords_file, "r") as stop:
        stopwords = [word.strip().lower() for word in stop.read().split("\n")]
    # Read in the words from harry text
    with open(harry_text, "r") as harry:
        harrywords = [
            word.strip().lower()
            for line in harry.read().split("\n")
            for word in line.split(" ")
        ]

    # Remove any non alpha-numeric characts
    pattern = re.compile(r"[\W_]+")
    harrywords = [pattern.sub("", word) for word in harrywords]
    # Remove any stop words
    harrywords = [word for word in harrywords if word not in stopwords]

    for w in harrywords:
        count_words[w] += 1

    return count_words.most_common(1)[0]

