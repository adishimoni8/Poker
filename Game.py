from Messages import Messages
from Player import Player
from Table import Table

# For testing purposes
from PokerRules import PokerRules
from CardStack import CardStack
from Deck import Deck
from MoneyStack import MoneyStack


class Game:
    """
    A Poker Game class.
    """

    def __init__(self):
        """
        Constructor for a poker game.
        """
        self.table = None
        self.num_of_players = None
        self.players = []
        self.play_again = True

    def start_game(self) -> None:
        """
        Start the game
        :return: None
        """
        while self.play_again:
            print(Messages.START_MESS)
            self.create_players()
            self.table = Table(self.players, self.num_of_players)
            self.table.play_poker()
            self.another_game()
        print(Messages.BYE)

    def create_players(self) -> None:
        """
        Player Creator, adds it to the players list.
        :return: None.
        """
        self.get_num_of_players()
        for i in range(self.num_of_players):
            self.add_player(i)

    def get_num_of_players(self) -> None:
        """
        Get from the user the number of player that will play, set the current field to this number.
        :return: None.
        """
        num_of_player = input(Messages.PLAYERS_MESS)
        while not num_of_player.isdigit() or int(num_of_player) < 2 or int(num_of_player) > 10:
            num_of_player = input(Messages.WRONG_MESS)
        self.num_of_players = int(num_of_player)

    def add_player(self, num_of_player: int) -> None:
        """
        Add a single player.
        :return:
        """
        name = input(Messages.NAME_OF_PLAYER.format(num_of_player + 1))
        balance = input(Messages.BALANCE)
        while not balance.isdigit() or int(balance) < 1:
            balance = input(Messages.WRONG_MESS)
        self.players.append(Player(name, int(balance)))

    def another_game(self) -> None:
        """
        Checker if the user wants another game.
        :return: A boolean value.
        """
        play_again = input(Messages.PLAY_AGAIN)
        while not play_again == "Y" and not play_again == "N":
            play_again = input(Messages.PLAY_AGAIN)
        if play_again == "Y":
            self.play_again = True
            self.players = []
        else:
            self.play_again = False


if __name__ == '__main__':
    game = Game()
    game.start_game()

    # # test to check winning hands:
    # adi = Player("adi", 300)
    # guy = Player("guy", 300)
    # card_stack = CardStack()
    # money_stack = MoneyStack(1000)
    # deck = Deck()
    #
    # for i in range(2):
    #     adi.cards_stack.add_card(deck.open_top())
    #     guy.cards_stack.add_card(deck.open_top())
    # for i in range(5):
    #     card_stack.add_card(deck.open_top())
    #
    # PokerRules.winner(card_stack, money_stack, [adi, guy])
