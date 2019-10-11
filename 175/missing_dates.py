import pandas as pd
from datetime import date, timedelta


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    start_date = min(dates)
    end_date = max(dates)
    number_of_days = int((end_date - start_date).days)

    for count in range(1, number_of_days):
        next_day = start_date + timedelta(days=count)
        if next_day in dates:
            next
        else:
            yield next_day
