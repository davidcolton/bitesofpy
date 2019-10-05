from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ["-", "\\", "|", "/"]  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    spinner = cycle(SPINNER_STATES)
    end = time() + seconds
    while time() < end:
        print(f"\r{next(spinner)}", end="", flush=True)
        sleep(STATE_TRANSITION_TIME)
    print()


if __name__ == "__main__":
    spinner(2)
