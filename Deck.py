import random


class Deck:
    """A deck class"""

    def __init__(self) -> None:
        """
        Initialize a deck.
        """
        self.cards = [[i, j] for i in range(13) for j in range(4)]

    def open_card(self) -> list:
        """
        Open randomized card from deck, and erase it.
        :return: the card chosen.
        """
        chosen = random.choice(self.cards)
        self.cards.remove(chosen)
        return chosen

