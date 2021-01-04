import os
from datetime import date
from datetime import datetime
from pathlib import Path
from typing import Dict, List
from urllib.request import urlretrieve
import json
import pandas as pd
import numpy as np

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

if not RATES_FILE.exists():
    urlretrieve(URL, RATES_FILE)


def prepare_data(rates_file=RATES_FILE):
    # Open the rates file and read in the json
    with open("exchangerates.json") as json_file:
        data = json.load(json_file)

    # Read the rates data into a pandas dataframe and transpose
    df = pd.DataFrame.from_records(data["rates"])
    df = df.T

    # Add a Base Date column to signify the dates imported
    # Will be the copied value used to fill missing dates
    df["Base Date"] = df.index
    df["Base Date"] = pd.to_datetime(df["Base Date"])

    # Create a date range from the start to end dates
    # This is used to reindex the dataframe and fill missing dates
    dr = pd.date_range(start=data["start_at"], end=data["end_at"])
    df.index = pd.DatetimeIndex(df.index)
    df = df.reindex(dr, fill_value=np.nan)

    # First forward fill then back fill all missing data
    df = df.ffill().bfill()

    return df


def get_all_days(start_date: date, end_date: date) -> List[date]:
    df = prepare_data()
    mask = (df.index.date >= start_date) & (df.index.date <= end_date)
    return list(df.loc[mask].index.date)


def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:
    df = prepare_data()
    df.drop("USD", axis=1, inplace=True)
    df.drop("GBP", axis=1, inplace=True)
    df_dict = df.to_dict("index")
    return {k.date(): v["Base Date"].date() for k, v in df_dict.items()}


def exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    df = prepare_data()

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if start not in df.index or end not in df.index:
        raise ValueError

    mask = (df.index >= start) & (df.index <= end)

    df_dict = df[mask].to_dict("index")
    new_dict = {}
    for k, v in df_dict.items():
        new_dict[k.date()] = {
            "Base Date": v["Base Date"].date(),
            "USD": v["USD"],
            "GBP": v["GBP"],
        }

    return new_dict