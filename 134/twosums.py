from collections import namedtuple
from collections import defaultdict
from itertools import product

NumIdx = namedtuple("NumIdx", "number index")
NumIdxPair = namedtuple("NumIdxPair", "num_01 num_02")


def two_sums(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    # Create a DefaultDict to hold a list of all pairs that match the target
    sum_of_two = defaultdict(list)
    sorted_and_index = sorted([NumIdx(num, idx) for idx, num in enumerate(numbers)])
    for num_pair in product(sorted_and_index, sorted_and_index):
        if num_pair[0].index != num_pair[1].index:
            total = num_pair[0].number + num_pair[1].number
            sum_of_two[total].append(NumIdxPair(num_pair[0], num_pair[1]))
    try:
        target_pair = sorted(sum_of_two[target])[0]
        return (target_pair.num_01.index, target_pair.num_02.index)
    except IndexError:
        return None
