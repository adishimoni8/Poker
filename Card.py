from enum import Enum


class Card:
    """
    A single card class.
    """

    class CardNum(Enum):
        """
        Enum for card numbers.
        """
        TWO = 0
        THREE = 1
        FOUR = 2
        FIVE = 3
        SIX = 4
        SEVEN = 5
        EIGHT = 6
        NINE = 7
        TEN = 8
        JACK = 9
        QUEEN = 10
        KING = 11
        ACE = 12

    class Kind(Enum):
        """
        Enum for card types.
        """
        HEART = 0
        DIAMOND = 1
        CLOVER = 2
        SPADE = 3

    def __init__(self, num: CardNum, kind: Kind):
        """
        A constructor for a single card.
        :param num: Card number (by Enums)
        :param kind: Card Kind (by Enums)
        """
        self.num = num
        self.kind = kind

    def get_num(self) -> CardNum:
        """
        A getter for the number enum.
        :return: The card's number.
        """
        return self.num

    def get_kind(self) -> Kind:
        """
        A getter for the kind enum.
        :return: The card's kind.
        """
        return self.kind

    def __str__(self):
        return self.num.name + " of " + self.kind.name


