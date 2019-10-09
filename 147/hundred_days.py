from datetime import date
from datetime import timedelta

import dateutil

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    hundred_weekdays = []
    date_to_check = start_date
    while len(hundred_weekdays) < 100:
        weekday_number = int(date_to_check.weekday())
        if weekday_number not in [5, 6]:
            hundred_weekdays.append(date_to_check)
        date_to_check = date_to_check + timedelta(days=1)
    return hundred_weekdays
