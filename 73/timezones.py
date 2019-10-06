import pytz
from datetime import datetime

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    tz_meeting_okay = []
    utc_dt = pytz.utc.localize(utc)
    for tz in timezones:
        if tz not in TIMEZONES:
            raise ValueError
        tz_time = utc_dt.astimezone(pytz.timezone(tz))
        tz_meeting_okay.append(tz_time.hour in list(MEETING_HOURS))

    return all(tz_meeting_okay)

