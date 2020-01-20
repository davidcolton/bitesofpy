XYZ = "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
THRESHOLDS = (5000, 0.05)

import pandas as pd


def calculate_flux(XYZ: str) -> list:
    """Read the data in from xyz.csv
    add two new columns, one to calculate dollar flux,
    and the other to calculate percentage flux
    return as a list of tuples
    """
    df = pd.read_csv(XYZ)
    df["DollarFlux"] = df["12/31/20"] - df["12/31/19"]
    df["PercentageFlux"] = df["DollarFlux"] / df["12/31/19"]
    return list(df.itertuples(index=False, name=None))


def identify_flux(xyz: list) -> list:
    """Load the list of tuples, iterate through
    each item and determine if it is above both
    thresholds. if so, add to the list
    """
    flagged_lines = []

    for flux_tup in xyz:
        compare_tuple = (abs(flux_tup[3]), abs(flux_tup[4]))
        if all(i > j for i, j in zip(compare_tuple, THRESHOLDS)):
            flagged_lines.append(flux_tup)
    return flagged_lines
