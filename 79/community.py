import csv
import requests
from urllib.request import urlretrieve
from collections import Counter


CSV_URL = "https://bit.ly/2HiD2i8"


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode("utf-8")
        csv_content = csv.reader(decoded_content.splitlines(), delimiter=",")
    # Don't return the header
    return list(csv_content)[1:]


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    bar = "+"
    tz_counter = Counter()
    for line in content:
        _, _, tz = line
        tz_counter[tz] += 1

    for entry in sorted(tz_counter.items()):
        timezone, count = entry
        print(f"{timezone:<22} | {bar * count}")


create_user_bar_chart(get_csv())
