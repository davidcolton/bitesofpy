from collections import namedtuple
from itertools import repeat
import shlex

SUITS = "Red Green Yellow Blue".split()
SUITED_CARDS = shlex.split("0 1 2 3 4 5 6 7 8 9 'Draw Two' Skip Reverse")
NON_SUITED_CARDS = shlex.split("Wild 'Wild Draw Four'")

UnoCard = namedtuple("UnoCard", "suit name")


def _card_maker(suit, card):
    if suit == None:
        return repeat(UnoCard(suit, card), 4)
    if card == "0":
        return repeat(UnoCard(suit, card), 1)
    else:
        return repeat(UnoCard(suit, card), 2)


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    uno_deck = []
    for suit in SUITS:
        for card in SUITED_CARDS:
            cards_to_add = _card_maker(suit, card)
            uno_deck.extend(x for x in cards_to_add)

    for wild_card in NON_SUITED_CARDS:
        cards_to_add = _card_maker(None, wild_card)
        uno_deck.extend(x for x in cards_to_add)

    return uno_deck
