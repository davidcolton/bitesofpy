from typing import List


def minimum_number(digits: List[int]) -> int:
    return int("".join(str(c) for c in sorted(set(digits)))) if digits else 0

