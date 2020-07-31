from collections import Counter


def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """

    num_counter = Counter(numbers)
    return (
        max(num_counter, key=num_counter.get),
        min(num_counter, key=num_counter.get),
    )

