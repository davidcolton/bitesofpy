import math


def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    return [math.ceil(x) if up else math.floor(x) for x in transactions]