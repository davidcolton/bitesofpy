import struct

april_1981 = """     April 1981
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
"""

jan_1986 = """    January 1986
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
"""

jan_1956 = """    January 1956
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
"""


def _slice(s, size, num):
    position = 0
    for length in range(0, (size * num), size):
        yield s[position : position + size]
        position += size


def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    # A dictionary to hold the date: day key value pairs
    date_day = dict()

    # Just set up a fixed list of days
    days_of_week = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]

    # Iterate over all calender lines that contain dates
    # From line index 2 to line index -1
    for week in calendar_output.split("\n")[2:-1]:
        days = _slice(week, 3, 7)
        # Process each day in the days list
        # Basically test if an integer
        for idx, day in enumerate(days):
            if day.strip() == "":
                # No date here
                next
            else:
                date_day[int(day.strip())] = days_of_week[idx]

    return date_day
