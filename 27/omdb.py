import glob
import json
import os
import re
from urllib.request import urlretrieve

BASE_URL = "http://projects.bobbelderbos.com/pcc/omdb/"
MOVIES = ("bladerunner2049 fightclub glengary " "horrible-bosses terminator").split()
TMP = "/tmp"

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f"{movie}.json"
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    if not os.path.exists(local):
        urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, "*json"))


def get_movie_data(files=files):
    movies_list = []
    for file in files:
        with open(file, "r") as f:
            m = json.load(f)
        movies_list.append(m)
    return movies_list


movies = get_movie_data(files)


def get_single_comedy(movies):
    for movie in movies:
        genre_str = movie["Genre"]
        genre_list = [genre.strip() for genre in genre_str.split(",")]
        if "Comedy" in genre_list:
            return movie["Title"]


def get_movie_most_nominations(movies):
    most_noms = {}
    for movie in movies:
        title = movie["Title"]
        noms = int(
            re.search(r"(\d{1,2}) nominations", movie["Awards"]).group().split(" ")[0]
        )
        most_noms[title] = noms
    # print(most_noms)
    # return max(zip(most_noms.values(), most_noms.keys()))[1]
    return max(most_noms, key=most_noms.get)


def get_movie_longest_runtime(movies):
    runtimes = {}
    for movie in movies:
        title = movie["Title"]
        runti = int(movie["Runtime"].split(" ")[0])
        runtimes[title] = runti
    return max(runtimes, key=runtimes.get)


get_movie_data()
