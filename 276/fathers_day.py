from pathlib import Path
from urllib.request import urlretrieve
from datetime import datetime
from dateutil.parser import parse

from collections import defaultdict

# get the data
tmp = Path("/tmp")
base_url = "https://bites-data.s3.us-east-2.amazonaws.com/"

fathers_days_countries = tmp / "fathers-day-countries.txt"
fathers_days_recurring = tmp / "fathers-day-recurring.txt"

for file_ in (fathers_days_countries, fathers_days_recurring):
    if not file_.exists():
        urlretrieve(base_url + file_.name, file_)


def merge_defaultdicts_lists(d, d1):
    for k, v in d1.items():
        if k in d:
            d[k].extend(d1[k])
        else:
            d[k] = d1[k]
    return d


def _parse_father_days_per_country(year, filename=fathers_days_countries):
    """Helper to parse fathers_days_countries"""
    d = defaultdict(list)
    with open(filename, "r") as f:
        lines = "".join(f.readlines()[1:])
    country_groups = lines.split("\n\n")
    for group in country_groups:
        elements = group.strip().split("\n")
        countries = [
            country.strip()
            for country in elements[0][2:].replace("and ", "").split(",")
        ]
        dates = {int(k): v.strip() for k, v in (e.split(":") for e in elements[1:])}
        d[dates[year]] = countries
    return d


def _parse_recurring_father_days(filename=fathers_days_recurring):
    """Helper to parse fathers_days_recurring"""
    d = defaultdict(list)
    with open(filename, "r") as f:
        lines = "".join(f.readlines()[1:])
    date_groups = lines.split("\n\n")
    [
        d[elements[0][2:]].extend(elements[1:])
        for elements in (group.strip().split("\n") for group in date_groups)
    ]
    return d


def get_father_days(year=2020):
    """Returns a dictionary of keys = dates and values = lists
       of countries that celebrate Father's day that date

       Consider using the the 2 _parse* helpers.
    """
    country_days = _parse_father_days_per_country(year, fathers_days_countries)
    recurring_days = _parse_recurring_father_days(fathers_days_recurring)
    return merge_defaultdicts_lists(country_days, recurring_days)


def generate_father_day_planning(father_days=None):
    """Prints all father days in order, example in tests and
       Bite description
    """
    if father_days is None:
        father_days = get_father_days()

    for day in sorted(
        father_days.items(), key=lambda x: datetime.strptime(x[0], "%B %d")
    ):
        print(day[0])
        for country in day[1]:
            print(f"- {country}")
        print()
