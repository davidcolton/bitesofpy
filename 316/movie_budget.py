from datetime import date
from typing import Dict, Sequence, NamedTuple
import pandas as pd


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = "stream", "rent"

renting_history = [
    MovieRented("Mad Max Fury Road", 4, date(2020, 12, 17)),
    MovieRented("Die Hard", 4, date(2020, 12, 3)),
    MovieRented("Wonder Woman", 4, date(2020, 12, 28)),
]


def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH,
) -> Dict[str, str]:
    """Function that calculates if renting movies one by one is
    cheaper than streaming movies by months.

    Determine this PER MONTH for the movies in renting_history.

    Return a dict of:
    keys = months (YYYY-MM)
    values = 'rent' or 'stream' based on what is cheaper

    Check out the tests for examples.
    """
    df = pd.DataFrame(columns=["year-mm", "cost"])
    for movie in renting_history:
        movie_month = f"{movie.date.year}-{movie.date.month}"
        df = df.append({"year-mm": movie_month, "cost": movie.price}, ignore_index=True)
    df_sum = df.groupby("year-mm").sum()
    return_dict = {}
    for row in df_sum.itertuples(index=True, name="Pandas"):
        return_dict[row.Index] = (
            RENT if row.cost <= STREAMING_COST_PER_MONTH else STREAM
        )
    return return_dict