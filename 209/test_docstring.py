from docstring import sum_numbers


def test_sum_numbers():
    docstring = sum_numbers.__doc__.strip().split("\n")
    for line in ('Sums numbers',
                 '    :param numbers: a list of numbers',
                 '    :type numbers: list',
                 '    :raises TypeError: if not all numeric values passed in',
                 '    :return: sum of numbers',
                 '    :rtype: int'):
        assert line in docstring