from typing import List
from itertools import accumulate
from collections import defaultdict


def sum_indices(items: List[str]) -> int:
    # Handle all other scenarios
    indices = defaultdict(list)
    for idx, char in enumerate(items):
        indices[char].append(idx)
    return sum(sum(accumulate(values)) for values in indices.values())

