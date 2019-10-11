from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6, hour=22, minute=0, second=0)


def add_todo(q: str, task: str, start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    return_string = "{} @ {}"
    if q.isdigit():
        end_time = start_time + timedelta(seconds=int(q))
    else:
        pattern_dict = {
            "days": r"(\d*)d",
            "hours": r"(\d*)h",
            "minutes": r"(\d*)m",
            "seconds": r"(\d*)s",
        }

        td = dict()

        for key, regex in pattern_dict.items():
            res = re.findall(regex, q)
            td[key] = 0 if not res else int(res[0])

        end_time = start_time + timedelta(
            days=td["days"],
            hours=td["hours"],
            minutes=td["minutes"],
            seconds=td["seconds"],
        )

    return return_string.format(task, end_time)
