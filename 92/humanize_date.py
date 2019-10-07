from collections import namedtuple
from datetime import datetime
from datetime import timedelta


TimeOffset = namedtuple("TimeOffset", "offset date_str divider")

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60 * 60, 24 * 60 * 60
TIME_OFFSETS = (
    TimeOffset(10, "just now", None),
    TimeOffset(MINUTE, "{} seconds ago", None),
    TimeOffset(2 * MINUTE, "a minute ago", None),
    TimeOffset(HOUR, "{} minutes ago", MINUTE),
    TimeOffset(2 * HOUR, "an hour ago", None),
    TimeOffset(DAY, "{} hours ago", HOUR),
    TimeOffset(2 * DAY, "yesterday", None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    # Handle invalid input, not datetime type
    if type(date) is not datetime:
        raise ValueError

    diff = (NOW - date).total_seconds()

    # Handle scenario where date is in the future
    if diff < 0:
        raise ValueError

    # Handle scenario where date 2 or more days in past
    if diff >= DAY * 2:
        return date.strftime(r"%m/%d/%y")

    # Handle all other scenarios
    for os in TIME_OFFSETS:
        if diff < os.offset:
            denominator = os.divider if os.divider else 1
            return os.date_str.format(int(diff / denominator))
    return date.strftime(r"%m/%d/%y")

