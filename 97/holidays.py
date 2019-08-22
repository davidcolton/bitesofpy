from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
holidays_page = os.path.join("/tmp", "us_holidays.php")
urlretrieve("https://bit.ly/2LG098I", holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, "html.parser")
    table_rows = soup.find(class_="list-table").find_all("tr")

    for row in table_rows:
        try:
            holiday_date = row.find("time").get("datetime")
            holiday_month = holiday_date.split("-")[1]
            holiday_name = row.find("a").text
            holidays[holiday_month].append(holiday_name)
        except AttributeError:
            pass
    return holidays
