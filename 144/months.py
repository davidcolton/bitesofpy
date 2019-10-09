from datetime import date
from calendar import monthrange

from dateutil.relativedelta import relativedelta

START_DATE = date(2018, 11, 1)
MIN_DAYS_TO_COUNT_AS_MONTH = 10
MONTHS_PER_YEAR = 12


def calc_months_passed(year, month, day):
    """Construct a date object from the passed in arguments.
       If this fails due to bad inputs reraise the exception.
       Also if the new date is < START_DATE raise a ValueError.

       Then calculate how many months have passed since the
       START_DATE constant. We suggest using dateutil.relativedelta!

       One rule: if a new month is >= 10 (MIN_DAYS_TO_COUNT_AS_MONTH)
       days in, it counts as an extra  month.

       For example:
       date(2018, 11, 10) = 9 days in => 0 months
       date(2018, 11, 11) = 10 days in => 1 month
       date(2018, 12, 11) = 1 month + 10 days in => 2 months
       date(2019, 12, 11) = 1 year + 1 month + 10 days in => 14 months
       etc.

       See the tests for more examples.

       Return the number of months passed int.
    """
    if not all(isinstance(x, int) for x in [year, month, day]):
        raise TypeError
    if (
        (year < START_DATE.year)
        or (month not in range(1, 13))
        or (day not in range(1, monthrange(year, month)[1]))
        or (date(year, month, day) < START_DATE)
    ):
        raise ValueError

    date_to_test = date(year, month, day)
    relative_delta = relativedelta(date_to_test, START_DATE)
    days_to_month = 1 if relative_delta.days >= MIN_DAYS_TO_COUNT_AS_MONTH else 0
    return (
        (relative_delta.years * MONTHS_PER_YEAR) + relative_delta.months + days_to_month
    )