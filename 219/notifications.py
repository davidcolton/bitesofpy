from datetime import date, timedelta
from itertools import repeat

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    for i in repeat(0):
        start_date = start_date + timedelta(days=num_days)
        for b in range(num_bites):
            yield start_date

