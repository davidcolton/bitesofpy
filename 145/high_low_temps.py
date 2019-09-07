from collections import namedtuple
from datetime import date

import pandas as pd

DATA_FILE = "http://projects.bobbelderbos.com/pcc/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a datetime.date() object.
    The temperatures in the dataset are in tenths of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.
    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day between 2005-2015
       * Extract lowest temperatures for each day between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days
    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015
    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID, Date, Value
    5. From the record breakers in 2015, extract the high/low of all the temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    # Read the URL into a Pandas Dataframe
    df = pd.read_csv(DATA_FILE)

    # Data Preparation & Setup
    # Create a Date Time Object
    df["date_obj"] = pd.to_datetime(df.Date)
    # Make the year and month-day values easily available
    df["year"] = df["Date"].str[:4]
    df["month_day"] = df["Date"].str[5:]
    # Set the Value to Celsius from tenth of Celsius
    df["Data_Value"] = df["Data_Value"] / 10
    # Strip out February 29 Leap Year anomalies
    df = df[df["month_day"] != "02-29"]

    # Get a unique list of month-days and Station ID Values
    unique_dates = sorted(df["month_day"].unique())
    unique_ids = sorted(df["ID"].unique())

    # A List to hold the 2015 record dates
    record_dates = []

    # Iterate over the month-days and Station ID Values
    for my_date in unique_dates:
        for my_id in unique_ids:
            try:
                # Create a temporary table based on month-days and Station ID Values
                # df_temp = df[(df["month_day"] == my_date) & (df["ID"] == my_id)].copy()
                date_match = df["month_day"] == my_date
                id_match = df["ID"] == my_id
                mask = date_match & id_match
                df_temp = df[mask].copy()
                # Sort the temporary table [MAX at top MIN at bottom]
                df_temp = df_temp.sort_values(
                    by=["Data_Value", "Date"], ascending=[False, True]
                )
                # If the first value is 2015 we have a record
                if df_temp.iloc[0, :]["year"] == "2015":
                    my_date_obj = df_temp.iloc[0, :]["date_obj"]
                    my_data_value = df_temp.iloc[0, :]["Data_Value"]
                    record_dates.append(STATION(my_id, my_date_obj, my_data_value))
                # If the last value is 2015 we have a record
                if df_temp.iloc[-1, :]["year"] == "2015":
                    my_date_obj = df_temp.iloc[-1, :]["date_obj"]
                    my_data_value = df_temp.iloc[-1, :]["Data_Value"]
                    record_dates.append(STATION(my_id, my_date_obj, my_data_value))
            except IndexError:
                # 05-21 USC00205450 missing
                # 12-15 USC00205450 missing
                continue
    return (
        max(record_dates, key=lambda k: k.Value),
        min(record_dates, key=lambda k: k.Value),
    )


high_low_record_breakers_for_2015()
