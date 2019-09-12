import csv
import os
from urllib.request import urlretrieve
from collections import defaultdict

BATTLE_DATA = os.path.join("/tmp", "battle-table.csv")
if not os.path.isfile(BATTLE_DATA):
    urlretrieve("https://bit.ly/2U3oHft", BATTLE_DATA)


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    victor_mappings = defaultdict(set)
    with open(BATTLE_DATA, "r") as f:
        reader = csv.reader(f)
        battle_list = list(reader)
    player2_names = battle_list[0]
    for attackers in battle_list[1:]:
        for idx, item in enumerate(attackers):
            if idx == 0:
                player1_name = item
                next
            else:
                if item == "win":
                    victor_mappings[player1_name].add(player2_names[idx])
    return victor_mappings


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    if player1 == player2:
        return "Tie"

    if player1 not in defeat_mapping.keys() or player2 not in defeat_mapping.keys():
        raise ValueError

    can_beat = defeat_mapping[player1]

    if player2 in can_beat:
        return player1
    else:
        return player2


# print(get_winner("Rock", "Human"))
