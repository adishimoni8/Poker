from Card import Card


class CardStack:
    """
    A stack of cards.
    """

    def __init__(self):
        """
        A Constructor of a card stack.
        """
        self.cards = set()

    def add_card(self, card: Card) -> None:
        """
        Add a card to the stack.
        :param card: A given card.
        :return: None.
        """
        self.cards.add(card)

    def get_cards(self) -> set:
        """
        A getter for the stack's cards.
        :return: A set of cards.
        """
        return self.cards

    def __str__(self):
        cards = ''
        if len(self.cards) == 0:
            cards += "There are none"
        else:
            for card in self.cards:
                cards += "|" + card.get_num().name + " of " + card.get_kind().name + "| "
        return cards



