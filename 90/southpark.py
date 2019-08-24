from collections import Counter, defaultdict
import csv
import re

import requests

CSV_URL = "https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv"  # noqa E501

spoken_words = defaultdict(Counter)


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode("utf-8")


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    # Read the given csv string and del the header line
    script_lines = csv.reader(content.splitlines(keepends=True))

    # Iterate over each speaking line details
    for detail in script_lines:
        season = detail[0]
        episode = detail[1]
        char = detail[2]
        line = detail[3].strip()
        words = line.split()
        spoken_words[char][episode] += len(words)

    return spoken_words


# content = get_season_csv_file(season=1)
# print(content.splitlines(keepends=True))
# get_num_words_spoken_by_character_per_episode(content)
