BALANCE_START = 20000


class Player:
    def __init__(self) -> None:
        """
        Initialize a player.
        """
        self.balance = BALANCE_START
        self.cards = []
        self.active = True

    def pay_move(self, money) -> None:
        """
        pay money for the current move
        :param money:
        :return:None
        """
        self.balance = max(0, self.balance - money)

    def is_active(self) -> bool:
        """
        Getter for active
        :return: bool val.
        """
        return self.active

    def turn_off_active(self) -> None:
        """
        turn active propery - when fold.
        :return: None.
        """
        self.active = False

    def get_balance(self) -> int:
        """
        A getter for the balance.
        :return: int
        """
        return self.balance

    def get_cards(self) -> list:
        """
        A getter for the cards.
        :return: list of 2 cards.
        """
        return self.cards

    def add_money(self, money) -> None:
        """
        Add money (in case you win).
        :param money: How much to add.
        :return: None.
        """
        self.balance += money

    def take_card(self, card) -> None:
        """
        Take cards from deck.
        :param card: a given card.
        :return: None.
        """
        self.cards.append(card)
