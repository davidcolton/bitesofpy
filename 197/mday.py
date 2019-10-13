import datetime


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    # What day in May 01
    may_01 = datetime.datetime(year, 5, 1)
    may_01_day = may_01.weekday()

    # If May 01 is a Sunday add 7 days
    if may_01_day == 6:
        mothers_day = may_01 + datetime.timedelta(days=7)

    # Because weekdays are indexed from zero
    # First Sunday in is 6 (7 days) - the current May 01 day number
    # Add this and a week (7 days) to get the second Sunday.
    else:
        first_sunday = 6 - may_01_day
        mothers_day = may_01 + datetime.timedelta(days=first_sunday + 7)
    return mothers_day.date()

