from pathlib import Path
from urllib.request import urlretrieve

tmp = Path("/tmp")
timings_log = tmp / "pytest_timings.out"
if not timings_log.exists():
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out", timings_log
    )


def timings():
    with open(timings_log) as f:
        return f.readlines()


def get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    # Hold the average test times in a dictionary
    average_times = dict()

    # Strip out lines with warnings
    timings = [
        timing
        for timing in timings
        if "warning" not in timing and "no tests ran" not in timing
    ]

    # Iterate over each timing and add to dictionary
    for timing in timings:
        bite, _, tests, _, _, time, _, _ = timing.split()
        average_times[bite] = float(time) / float(tests)

    # Return the key of the minimun dictionary value
    return min(average_times, key=lambda k: average_times[k])


get_bite_with_fastest_avg_test(timings())
