from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = "white yellow orange green blue brown black paneled red".split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def _get_belt_recursion(score, scores_to_check):
    # Global stop condition if score is less then 10
    if score < 10:
        belt = None

    # Found the belt, return it
    elif score >= scores_to_check[0]:
        belt = HONORS[scores_to_check[0]]

    # Keep looking for the belt, remove head of list
    else:
        belt = _get_belt_recursion(score, scores_to_check[1:])

    return belt


def get_belt(user_score):
    return _get_belt_recursion(user_score, scores[::-1])
