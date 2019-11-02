from collections import defaultdict

names = "bob julian tim martin rod sara joyce nick beverly kevin".split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (5, 9),
    (6, 8),
    (7, 8),
    (8, 9),
]


def get_friend_with_most_friends(friendships=friendships, users=users):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    friends = defaultdict(set)
    for first, second in friendships:
        friends[(users[first], first)].add((users[second], second))
        friends[(users[second], second)].add((users[first], first))

    max_friends = max(friends, key=lambda x: len(friends[x]))
    return (max_friends[0], [x[0] for x in friends[max_friends]])


print(get_friend_with_most_friends())
