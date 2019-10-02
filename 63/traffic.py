from collections import namedtuple
from itertools import cycle, islice
from time import sleep

State = namedtuple("State", "color command timeout")


def traffic_light():
    """Returns an itertools.cycle iterator that
       when iterated over returns State namedtuples
       as shown in the Bite's description"""
    color = ["red", "green", "amber"]
    command = ["Stop", "Go", "Caution"]
    timeout = [2, 2, 0.5]
    return cycle([State(*seq) for seq in zip(color, command, timeout)])


if __name__ == "__main__":
    # print a sample of 10 states if run as standalone program
    for state in islice(traffic_light(), 10):
        print(f"{state.command}! The light is {state.color}")
        sleep(state.timeout)
