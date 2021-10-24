import CardStack
from Deck import Deck
from Player import Player


class Dealer:
    """
    A dealer of cards.
    """

    def __init__(self):
        """
        A constructor of a dealer.
        """
        self.deck = Deck()

    def deal_cards_to(self, stack: CardStack, num_of_cards: int) -> None:
        """
        Deal cards to a stack.
        :param stack: A given stack.
        :param num_of_cards: number of cards to deal.
        :return: None.
        """
        for i in range(num_of_cards):
            stack.add_card(self.deck.open_top())
