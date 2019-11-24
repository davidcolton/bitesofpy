import json
import pandas as pd
from pathlib import Path

SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
BELTS = ("white yellow orange green blue brown black " "paneled red").split()

# Create a dictionary of the scores, belts
belt_dict = dict(zip(SCORES, BELTS))

TMP = Path("/tmp")


def get_belts(data: str) -> dict:
    """Parsed the passed in json data:
       {"date":"5/1/2019","score":1},
       {"date":"9/13/2018","score":3},
       {"date":"10/25/2019","score":1},

       Loop through the scores in chronological order,
       determining when belts were achieved (use SCORES
       and BELTS).

       Return a dict with keys = belts, and values =
       readable dates, example entry:
       'yellow': 'January 25, 2018'
    """

    # Read JSON into a Pandas Dataframe
    df = pd.read_json(data)

    # Convert the date string to a real date then sort
    df["date"] = pd.to_datetime(df.date)
    df = df.sort_values(by="date").reset_index(drop=True)

    # Add a cumulative sum column based on the scores
    df["cumulative_sum"] = df.score.cumsum()

    # An empty dictionary to hold the return values
    return_dict = dict()

    # For each belt / bitecoins to achieve
    for bitecoins, belt in belt_dict.items():
        # If a date exists that meet the minimum requirements
        # Get it and add to the dictionary
        # As the table is sorted it will always be position [0]
        try:
            if df[df.cumulative_sum >= bitecoins].iloc[0].date:
                date_achieved = df[df.cumulative_sum >= bitecoins].iloc[0].date
                return_dict[belt] = date_achieved.strftime("%B %d, %Y")
        except IndexError:
            # To handle the scenario where the data does not include all belts
            pass
    return return_dict

