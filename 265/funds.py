IMPOSSIBLE = "Mission impossible. No one can contribute."


def max_fund(village):
    """Find a contiguous subarray with the largest sum."""

    if all([house < 0 for house in village]):
        print(IMPOSSIBLE)
        return 0, 0, 0

    return max(
        [
            (sum(village[f:l]), f + 1, l)
            for f in range(len(village))
            for l in range(len(village) + 1)
        ]
    )
