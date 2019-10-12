from dataclasses import dataclass
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

import dateutil


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    actor_dob = parse(actor.born)
    movie_released = parse(movie.release_date)
    age_in_years = relativedelta(movie_released, actor_dob).years
    return f"{actor.name} was {age_in_years} years old when {movie.title} came out."

