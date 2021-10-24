from random import sample
from Card import Card


class Deck:
    """
    A deck of cards.
    """

    def __init__(self):
        """
        A constructor for a deck of cards.
        """
        self.cards = set()
        for kind in Card.Kind:
            for card_num in Card.CardNum:
                self.cards.add(Card(card_num, kind))

    def open_top(self):
        """
        Open and return the top card (randomized) in a deck.
        :return: the card opened.
        """
        card = sample(self.cards, 1)[0]
        self.cards.remove(card)
        return card
