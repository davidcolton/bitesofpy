from itertools import chain, cycle
import string


def sequence_generator():
    return cycle(list(chain(*zip(list(range(1, 27)), list(string.ascii_uppercase)))))
