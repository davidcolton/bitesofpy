import csv
import re
from pathlib import Path
from urllib.request import urlretrieve
from collections import Counter

tmp = Path("/tmp")
stats = tmp / "bites.csv"

if not stats.exists():
    urlretrieve("https://bit.ly/2MQyqXQ", stats)

pattern_str = r"^Bite (\d+)"
pattern = re.compile(pattern_str)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    bites_counter = Counter()
    with open(stats, "r") as f:
        lines = [line.strip() for line in f.readlines() if line is not None]

    pattern_str = r"^Bite (?P<bite>\d+).*;(?P<score>.*)$"
    pattern = re.compile(pattern_str)

    for line in lines:
        details = pattern.findall(line)
        if len(details) > 0 and details[0][1] != "None":
            bites_counter[details[0][0]] = details[0][1]

    return [bite for bite, score in bites_counter.most_common(N)]


if __name__ == "__main__":
    res = get_most_complex_bites()
    print(res)
