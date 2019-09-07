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

    idx_min = df.groupby(["month_day"])["Data_Value"].transform(min) == df["Data_Value"]
    idx_max = df.groupby(["month_day"])["Data_Value"].transform(max) == df["Data_Value"]
    year_mask = df["year"] == "2015"

    mask = (idx_min | idx_max) & year_mask

    df_2015 = df[mask].sort_values(by=["Data_Value"], ascending=[False]).copy()

    my_max_id = df_2015.iloc[0, :]["ID"]
    my_max_date_obj = df_2015.iloc[0, :]["date_obj"]
    my_max_data_value = df_2015.iloc[0, :]["Data_Value"]
    max_value = STATION(my_max_id, my_max_date_obj.date(), my_max_data_value)

    my_min_id = df_2015.iloc[-1, :]["ID"]
    my_min_date_obj = df_2015.iloc[-1, :]["date_obj"]
    my_min_data_value = df_2015.iloc[-1, :]["Data_Value"]
    min_value = STATION(my_min_id, my_min_date_obj.date(), my_min_data_value)

    return (max_value, min_value)


print(high_low_record_breakers_for_2015())
