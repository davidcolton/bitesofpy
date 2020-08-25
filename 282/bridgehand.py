from collections import namedtuple, Sequence, defaultdict
from enum import Enum
from typing import Sequence

Suit = Enum("Suit", list("SHDC"))
Rank = Enum("Rank", list("AKQJT98765432"))
Card = namedtuple("Card", ["suit", "rank"])

HCP = {Rank.A: 4, Rank.K: 3, Rank.Q: 2, Rank.J: 1}
HCP_LTC = {Rank.A: 4, Rank.K: 3, Rank.Q: 2}
SSP = {2: 1, 1: 2, 0: 3}  # cards in a suit -> short suit points


class BridgeHand:
    def __init__(self, cards: Sequence[Card]):
        """
        Process and store the sequence of Card objects passed in input.
        Raise TypeError if not a sequence
        Raise ValueError if any element of the sequence is not an instance
        of Card, or if the number of elements is not 13
        """
        if not isinstance(cards, Sequence):
            raise TypeError
        elif not len(cards) == 13 or not all(isinstance(card, Card) for card in cards):
            raise ValueError

        self.hand = cards
        self.sorted_hand = defaultdict(list)

        # Store sorted hand in default dict
        for card in self.hand:
            self.sorted_hand[card.suit.name].append(card.rank)

        for suit in Suit:
            self.sorted_hand[suit.name] = sorted(
                self.sorted_hand[suit.name], key=lambda x: x.value
            )

        print(self.sorted_hand)

    def __str__(self) -> str:
        """
        Return a string representing this hand, in the following format:
        "S:AK3 H:T987 D:KJ98 C:QJ"
        List the suits in SHDC order, and the cards within each suit in
        AKQJT..2 order.
        Separate the suit symbol from its cards with a colon, and
        the suits with a single space.
        Note that a "10" should be represented with a capital 'T'
        """
        return_string = ""
        for suit in Suit:
            if len(self.sorted_hand[suit.name]):
                return_string += f"{suit.name}:"
                return_string += (
                    f"{''.join(card.name for card in self.sorted_hand[suit.name])}"
                )
                return_string += " "
        return return_string.strip()

    @property
    def hcp(self) -> int:
        """ Return the number of high card points contained in this hand """
        hcp = 0
        for card in self.hand:
            if card.rank.name in ["A", "K", "Q", "J"]:
                hcp += HCP[card.rank]
        return hcp

    @property
    def doubletons(self) -> int:
        """ Return the number of doubletons contained in this hand """
        dts = 0
        return dts + int(
            sum(1 for suit in Suit if len(self.sorted_hand[suit.name]) == 2)
        )

    @property
    def singletons(self) -> int:
        """ Return the number of singletons contained in this hand """
        sts = 0
        return sts + int(
            sum(
                1
                for suit in Suit
                if len(self.sorted_hand[suit.name]) == 1
                and self.sorted_hand[suit.name][0].name != "A"
            )
        )

    @property
    def voids(self) -> int:
        """ Return the number of voids (missing suits) contained in
            this hand
        """
        voids = 0
        return sum(1 for suit in Suit if len(self.sorted_hand[suit.name]) == 0)

    @property
    def ssp(self) -> int:
        """ Return the number of short suit points in this hand.
            Doubletons are worth one point, singletons two points,
            voids 3 points
        """
        return (self.singletons * 2) + (self.doubletons * 1) + (self.voids * 3)

    @property
    def total_points(self) -> int:
        """ Return the total points (hcp and ssp) contained in this hand """
        return self.hcp + self.ssp

    @property
    def ltc(self) -> int:
        """ Return the losing trick count for this hand - see bite description
            for the procedure
        """
        ltc = 0
        for suit in Suit:
            if len(self.sorted_hand[suit.name]) == 0:
                print(f"Suit: {self.sorted_hand[suit.name]}, Void, {ltc}")
                continue
            elif (
                len(self.sorted_hand[suit.name]) == 1
                and self.sorted_hand[suit.name][0].name != "A"
            ):
                ltc += 1
                print(f"Suit: {self.sorted_hand[suit.name]}, Singleton, {ltc}")
            elif len(self.sorted_hand[suit.name]) == 2:
                d_rank = sum(
                    HCP_LTC[card]
                    for card in self.sorted_hand[suit.name]
                    if card in HCP_LTC.keys()
                )
                if d_rank < 3:
                    ltc += 2
                elif 3 <= d_rank <= 4:
                    ltc += 1
                print(
                    f"Suit: {suit.name}, Cards:{self.sorted_hand[suit.name]}, Doubleton, {ltc}"
                )
            else:
                d_rank = sum(
                    HCP_LTC[card]
                    for card in self.sorted_hand[suit.name][:3]
                    if card in HCP_LTC.keys()
                )
                if d_rank < 2:
                    ltc += 3
                elif 2 <= d_rank <= 4:
                    ltc += 2
                elif 5 <= d_rank <= 7:
                    ltc += 1
                print(
                    f"Suit: {suit.name}, Cards:{self.sorted_hand[suit.name][:3]}, Triple, Rank {d_rank}, {ltc}"
                )
        return ltc
