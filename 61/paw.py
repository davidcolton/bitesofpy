from collections import namedtuple
from random import randint
import string

ACTIONS = ["draw_card", "play_again", "interchange_cards", "change_turn_direction"]
NUMBERS = range(1, 5)
AllCARDS = string.ascii_uppercase

PawCard = namedtuple("PawCard", "card action")


def create_paw_deck(n=8):
    deck = []
    if n > 26:
        raise ValueError(f"There can only be a maximum of 26 types of cards")
    card_letters = [AllCARDS[x] for x in range(n)]
    for letter in card_letters:
        action_card = randint(1, 4)
        for number in NUMBERS:
            action = ACTIONS[action_card - 1] if number == action_card else None
            deck.append(PawCard(letter + str(number), action))
    return deck


create_paw_deck()
