from collections import namedtuple, Counter
import re
from typing import NamedTuple

import feedparser
import datetime


def total_seconds(episode_time):
    return (episode_time.hour * 3600) + (episode_time.minute * 60) + episode_time.second


SPECIAL_GUEST = "Special guest"

# using _ as min/max are builtins
Duration = namedtuple("Duration", "avg max_ min_")

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = "https://bites-data.s3.us-east-2.amazonaws.com/python_bytes"
IGNORE_DOMAINS = {
    "https://pythonbytes.fm",
    "http://pythonbytes.fm",
    "https://twitter.com",
    "https://training.talkpython.fm",
    "https://talkpython.fm",
    "http://testandcode.com",
}


class PythonBytes:
    def __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = feedparser.parse(url).entries

    def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        episodes = []
        for entry in self.entries:
            if domain in entry.description:
                episodes.append(entry.itunes_episode)
        return episodes

    def get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """

        mentioned_domains = []
        http_filter = re.compile(r"https?://[^/]+")
        for entry in self.entries:
            domain_set = set(http_filter.findall(entry.summary))
            domain_set = domain_set - IGNORE_DOMAINS
            mentioned_domains += list(domain_set)
        return Counter(mentioned_domains).most_common(n)

    def number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        episodes = []
        for entry in self.entries:
            if SPECIAL_GUEST in entry.description:
                episodes.append(entry.itunes_episode)
        return len(episodes)

    def get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """
        episodes = []
        for entry in self.entries:
            h, m, s = [int(n) for n in entry.itunes_duration.split(":")]
            episodes.append(datetime.time(h, m, s))
        shortest = min(episodes)
        longest = max(episodes)
        average = int(sum([total_seconds(t) for t in episodes]) / len(episodes))
        return Duration(
            average, longest.strftime("%H:%M:%S"), shortest.strftime("%H:%M:%S")
        )

