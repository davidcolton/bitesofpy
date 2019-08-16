import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
from statistics import mean

BASE_URL = "http://projects.bobbelderbos.com/pcc/movies/"
TMP = "/tmp"

fname = "movie_metadata.csv"
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
if not os.path.exists(local):
    urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movie_list = defaultdict(list)
    with open(local, "r") as f:
        movies = csv.DictReader(f)
        for m in movies:
            director = m["director_name"].strip()
            title = m["movie_title"].strip()
            year = m["title_year"].strip()
            imdb = m["imdb_score"].strip()
            try:
                if int(year) >= MIN_YEAR:
                    movie_list[director].append(Movie(title, int(year), float(imdb)))
            except ValueError:
                continue
    return movie_list


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    list_of_scores = []
    for m in movies:
        list_of_scores.append(m.score)
    return round(mean(list_of_scores), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    return sorted(
        [
            (director, calc_mean_score(movies))
            for director, movies in directors.items()
            if len(movies) >= MIN_MOVIES
        ],
        key=lambda x: x[1],
        reverse=True,
    )

