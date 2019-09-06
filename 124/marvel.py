from collections import namedtuple
from collections import Counter
import csv
import re

import requests

MARVEL_CSV = "https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv"  # noqa E501

Character = namedtuple("Character", "pid name sid align sex appearances year")


# csv parsing code provided so this Bite can focus on the parsing


def _get_csv_data():
    """Download the marvel csv data and return its decoded content"""
    with requests.Session() as session:
        return session.get(MARVEL_CSV).content.decode("utf-8")


def load_data():
    """Converts marvel.csv into a sequence of Character namedtuples
       as defined above"""
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=",")
    for row in reader:
        name = re.sub(r"(.*?)\(.*", r"\1", row["name"]).strip()
        yield Character(
            pid=row["page_id"],
            name=name,
            sid=row["ID"],
            align=row["ALIGN"],
            sex=row["SEX"],
            appearances=row["APPEARANCES"],
            year=row["Year"],
        )


data = list(load_data())
print(data[0])


# start coding


def most_popular_characters(top=5):
    """Get the most popular character by number of appearances,
       return top n characters (default 5)"""
    appearance_counter = Counter()
    for character in data:
        if not character.appearances == "":
            name = character.name
            app = max(
                int(character.appearances), int(appearance_counter[character.name])
            )
            appearance_counter[character.name] = app

    return [name for name, app in appearance_counter.most_common(top)]


def max_and_min_years_new_characters():
    """Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv data, or
       the 'year' attribute of the namedtuple, return a tuple of
       (max_year, min_year)"""
    appearance_counter = Counter()
    for character in data:
        if not character.year == "":
            appearance_counter[character.year] += 1

    return (
        appearance_counter.most_common()[0][0],
        appearance_counter.most_common()[-1][0],
    )


def percentage_female():
    """Get the percentage of female characters as percentage of all characters, rounded to 2 digits"""
    appearance_counter = Counter()
    char_name = set()
    for character in data:
        if character.sex == "":
            gender = "None"
        else:
            gender = character.sex.split(" ")[0]
        name = character.name
        # if name not in char_name:
        #    char_name.add(name)
        appearance_counter[gender] += 1
        appearance_counter["Total"] += 1
    print(appearance_counter.most_common())
    return round((appearance_counter["Female"] / appearance_counter["Total"]) * 100, 2)

