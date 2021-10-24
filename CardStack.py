from Card import Card


class CardStack:
    """
    A stack of cards.
    """

    OPEN_CARDS = """================
THE OPEN CARDS ARE: """

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

    def print_cards(self) -> None:
        """
        Print the cards in the stack.
        :return: None.
        """
        print(CardStack.OPEN_CARDS)
        if len(self.cards) == 0:
            print("There are none")
        for card in self.cards:
            print(card.get_num().name + " of " + card.get_kind().name)

    def get_cards(self) -> set:
        """
        A getter for the stack's cards.
        :return: A set of cards.
        """
        return self.cards
