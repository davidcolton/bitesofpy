import pandas as pd

movie_excel_file = "https://bit.ly/2BVUyrO"


def _extract_values(row):
    genres = row["genres"].split("|")
    movie = row["movie"]
    return [[genre, movie] for genre in genres]


def group_by_genre(data=movie_excel_file):
    """Takes movies data excel file (https://bit.ly/2BXra4w) and loads it
       into a DataFrame (df).

       Explode genre1|genre2|genre3 into separte rows using the provided
       "explode" function we found here: https://bit.ly/2Udfkdt

       Filters out '(no genres listed)' and groups the df by genre
       counting the movies in each genre.

       Return the new df of shape (rows, cols) = (19, 1) sorted by movie count
       descending (example output: https://bit.ly/2ILODva)
    """
    # Read in the Excel File
    df = pd.read_excel(
        "https://bit.ly/2BVUyrO", sheet_name="data", header=7, usecols=[2, 3]
    )

    # Remove the (no genres listed) movies first
    df = df[df.genres != "(no genres listed)"]

    # Apply the extract value function to each row
    # Data is now a list of lists of (genres, movie) tuples
    data = df.apply(_extract_values, axis=1)

    # Create a new Dataframe from the flattened list of lists
    df_new = pd.DataFrame.from_records(
        [y for x in data for y in x], columns=["genres", "movie"]
    )

    # Return the requested dataframe
    return df_new.groupby("genres").count().sort_values("movie", ascending=False)

