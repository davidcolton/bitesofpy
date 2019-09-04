from collections import Counter
import os
from urllib.request import urlretrieve

from dateutil.parser import parse
from datetime import datetime
import re

commits = os.path.join("/tmp", "commits")
if not os.path.exists(commits):
    urlretrieve("https://bit.ly/2H1EuZQ", commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = "{y}-{m:02d}"
pattern = re.compile(r"(\d+) [insert|delet]+")


def _extract_month(date_str: str) -> str:
    update_date = parse(date_str[12:-1])
    year_month = update_date.strftime("%Y-%m")
    return year_month


def _extract_changes(updates: str) -> int:
    changes_list = pattern.findall(updates)
    return sum([int(n) for n in changes_list])


def get_min_max_amount_of_commits(
    commit_log: str = commits, year: int = None
) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    monthly_changes = Counter()

    with open(commits, "r") as f:
        lines = f.read().strip()

    for line in lines.split("\n"):
        update, activity = line.split("|")
        date_str = _extract_month(update)
        change = _extract_changes(activity)
        if year and str(year) not in date_str:
            next
        else:
            monthly_changes[date_str] += change

    return (
        min(monthly_changes, key=monthly_changes.get),
        max(monthly_changes, key=monthly_changes.get),
    )
