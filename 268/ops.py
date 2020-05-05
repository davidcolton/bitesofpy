def num_ops(n):
    """
    Input: an integer number, the target number
    Output: the minimum number of operations required to reach to n from 1.

    Two operations rules:
    1.  multiply by 2
    2.  int. divide by 3

    The base number is 1. Meaning the operation will always start with 1
    These rules can be run in any order, and can be run independently.

    [Hint] the data structure is the key to solve it efficiently.
    """
    target = n
    level = 1
    found = {1: level}
    added = [1]
    while True:
        new_added = []
        for num in added:
            if 2 * num not in found:
                found[2 * num] = level
                new_added.append(2 * num)
            if num // 3 not in found:
                found[num // 3] = level
                new_added.append(num // 3)
        if target in found:
            break
        # Copies new_added over the added array.
        added[:] = new_added
        level += 1

    return level
