import operator
from itertools import accumulate


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    for idx, sum in enumerate(accumulate(sequence, operator.add), start=1):
        yield (f"{sum/idx :0.2f}")