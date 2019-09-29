from itertools import combinations, permutations
from typing import Iterable


def friends_teams(
    friends: list, team_size: int = 2, order_does_matter: bool = False
) -> Iterable:
    return (
        permutations(friends, team_size)
        if order_does_matter
        else combinations(friends, team_size)
    )
