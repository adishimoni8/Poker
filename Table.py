from Dealer import Dealer
from MoneyStack import MoneyStack
from PokerRules import PokerRules
from CardStack import CardStack


class Table:
    """
    A table for poker.
    """

    def __init__(self, players, num_of_players):
        """
        A constructor for the table.
        :param players: a list of players.
        :param num_of_players: the number of players.
        """
        self.players = players
        self.num_of_players = num_of_players
        self.active_players = num_of_players
        self.dealer = Dealer()
        self.card_stack = CardStack()
        self.money_stack = MoneyStack()
        self.cur_player = 0
        self.round_num = 0
        self.round_player_money = 0

    def next_active_player(self):
        """
        Move to the next active player and update the index field.
        :return: None
        """
        self.cur_player = (self.cur_player + 1) % self.num_of_players
        while not self.players[self.cur_player].is_active():
            self.cur_player = (self.cur_player + 1) % self.num_of_players

    def play_poker(self) -> None:
        """
        Play an entire poker game on the table.
        :return: None.
        """
        self.deal_opening_cards()
        for i in range(PokerRules.NUM_OF_ROUNDS):
            if self.active_players == 1:
                break
            self.play_round()
        PokerRules.winner(self.card_stack, self.money_stack, self.players)

    def play_round(self) -> None:
        """
        Play a single round of poker.
        :return: None.
        """
        self.open_cards()
        self.card_stack.print_cards()
        self.money_stack.print_money()
        start_player = self.cur_player   # Helper for the round to end correctly.

        # The actual round
        while self.continue_round(start_player):
            if self.active_players == 1:
                break
            self.round_player_money += self.players[self.cur_player].play_round(self.round_player_money)
            if not self.players[self.cur_player].is_active():
                self.active_players -= 1
            self.next_active_player()
            self.players[start_player].set_already_raised(True)  # Helper for the round to end correctly.
        self.end_round()

    def end_round(self) -> None:
        """
        End the round, collect the money of all players, and set their raise field to to False.
        :return: None.
        """
        self.collect_money()
        self.round_num += 1
        self.round_player_money = 0
        for player in self.players:
            player.set_already_raised(False)

    def continue_round(self, start_player):
        """
        Check if the round needs to continue to the next player. To determine when to stop the round we need to find
        the last one who already raised to the highest amount of money.
        :param start_player: the player that started the round.
        :return: if the round shell proceed.
        """
        if self.players[self.cur_player].get_already_raised() and \
                self.players[self.cur_player].round_money == self.round_player_money:
            return False
        return True

    def collect_money(self) -> None:
        """
        Collect the money that the players bet at the end of a round.
        :return: None.
        """
        for player in self.players:
            self.money_stack.add_money(player.pay_round_money())

    def open_cards(self) -> None:
        """
        Open cards to the stack of cards on the table.
        :return: None.
        """
        self.dealer.deal_cards_to(self.card_stack, PokerRules.CARDS_PER_ROUND[self.round_num])

    def deal_opening_cards(self) -> None:
        """
        Deal the players the opening cards.
        :return: None.
        """
        for i in range(self.num_of_players):
            self.dealer.deal_cards_to(self.players[i].cards_stack, PokerRules.CARDS_PER_PLAYER)