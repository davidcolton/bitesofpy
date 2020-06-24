from typing import List


def make_changes(n: int, coins: List[int]) -> int:
    """
    Input: n - the changes amount
          coins - the coin denominations
    Output: how many ways to make this changes
    """

    num_coins = len(coins)

    # We need n+1 rows as the table is constructed
    # in bottom up manner using the base case 0 value
    # case (n = 0)
    table = [[0 for x in range(num_coins)] for x in range(n + 1)]

    # Fill the entries for 0 value case (n = 0)
    for i in range(num_coins):
        table[0][i] = 1

    # Fill rest of the table entries in bottom up manner
    for i in range(1, n + 1):
        for j in range(num_coins):

            # Count of solutions including coins[j]
            x = table[i - coins[j]][j] if i - coins[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j - 1] if j >= 1 else 0

            # total count
            table[i][j] = x + y

    return table[n][num_coins - 1]
