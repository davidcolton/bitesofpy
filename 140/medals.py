import pandas as pd
import requests

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data=data):
    # Read the data
    df = pd.read_csv(data)

    # Create group by objects
    df_men = df[df.Gender == "Men"].groupby("Athlete").agg({"Medal": "count"})
    df_women = df[df.Gender == "Women"].groupby("Athlete").agg({"Medal": "count"})

    # Add max of Men and Women to a dict
    results_dict = dict()
    results_dict.update(df_men[df_men.Medal == df_men.Medal.max()].to_dict()["Medal"])
    results_dict.update(
        df_women[df_women.Medal == df_women.Medal.max()].to_dict()["Medal"]
    )

    return results_dict
