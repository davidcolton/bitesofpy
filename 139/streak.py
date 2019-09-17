from datetime import datetime, timedelta, date

TODAY = date(2018, 11, 12)

data = """
+------------+------------+---------+
| date       | activity   | count   |
|------------+------------+---------|
| 2018-11-10 | pcc        | 1       |
| 2018-11-09 | 100d       | 1       |
| 2018-11-07 | 100d       | 2       |
| 2018-10-23 | pcc        | 1       |
| 2018-10-15 | pcc        | 1       |
| 2018-10-05 | bite       | 1       |
| 2018-09-21 | bite       | 4       |
| 2018-09-18 | bite       | 2       |
| 2018-09-18 | bite       | 4       |
+------------+------------+---------+
"""


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    # The format is consistent
    #  - line[4:-2]
    #  - characters[2:12]
    extracted_dates = set()
    for line in data.splitlines()[4:-2]:
        extracted_dates.add(datetime.strptime(line.strip()[2:12], "%Y-%m-%d").date())
    return list(extracted_dates)


def _recursive_calculate_streak(streak, start_date, list_of_dates):
    # Streak is broken, return the streak
    if (start_date - list_of_dates[0]).days > 1:
        return streak
    # Edge Case
    # Streak still on but last date return streak + 1
    elif ((start_date - list_of_dates[0]).days == 1) and (len(list_of_dates) == 1):
        return streak + 1
    # On a streak, streak + 1 and recursive call
    else:
        return _recursive_calculate_streak(
            streak + 1, list_of_dates[0], list_of_dates[1:]
        )


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    # Sort the dates to be analysed
    dates = sorted(dates, reverse=True)
    streak = 0
    return _recursive_calculate_streak(streak, TODAY, dates)

