from typing import List


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    if N == 0:
        return []
    lines = []
    for line in range(1, N + 1):
        l = []
        value = 1
        for position in range(1, line + 1):
            l.append(value)
            value = int(value * (line - position) / position)
        lines.append(l)
    return lines[-1]

