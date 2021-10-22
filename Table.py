from Deck import Deck
from Player import Player
from Rules import Rules

NUM_OF_ROUNDS = 4
CARDS_TO_BEGIN_WITH = 2
SHOW_OPEN_CARDS = """===================
THE OPEN CARDS ARE:
{0}
==================="""

PLAYER_TURN = """----------------
Player {0} it's your turn!
Your balance: {1}$
Your cards are: {2} | {3}
What do you want to do? C for Call, R for Raise, F for Fold: """

WINNER = """===================
Player {0} won! He earned {1}$ from the stack!
==================="""


class Table:
    """A table class"""

    def __init__(self, num_of_players) -> None:
        """
        Initialize, all fields are self-explanatory.
        :param num_of_players: Num of players.
        """
        self.players = [Player() for i in range(num_of_players)]
        self.num_of_player = num_of_players
        self.active_players = num_of_players
        self.deck = Deck()
        self.stack_money = 0
        self.money_each_player_round = 0
        self.keep_play = True
        self.cards_per_round = [0,3,1,1]
        self.round_num = 0
        self.open_cards = []
        self.dict_of_types = {0: "Heart", 1: "Diamond", 2: "Clover", 3: "Spade"}

    def play_game(self) -> None:
        """
        Play a full game of poker
        :return: None
        """
        self.deal_cards()
        while self.active_players > 1 and self.round_num < NUM_OF_ROUNDS:
            self.open_cards_to_deck(self.cards_per_round[self.round_num])
            self.show_open_cards()
            self.play_round()
            self.round_num += 1
        self.prize_winner()

    def play_round(self) -> None:
        """
        Play 1 round after opening another bunch of cards
        :return: None
        """
        first_round = True
        last_raised = 0  # Need to stop when we reach the last one that raised.
        i = 0
        while i != last_raised or first_round:
            first_round = False
            if self.players[i].is_active():  # only active player play
                player_balance = str(self.players[i].get_balance())
                player_first_card = self.convert_card_to_string(self.players[i].get_cards()[0])
                player_second_card = self.convert_card_to_string(self.players[i].get_cards()[1])
                move = input(PLAYER_TURN.format(str(i), player_balance, player_first_card, player_second_card))
                while move != "C" and move != "R" and move != "F":
                    move = input("Wrong input: C for Call, R for Raise, F for Fold")

                if move == "C":  # if one chose "Call"
                    self.players[i].pay_move(self.money_each_player_round)
                    self.stack_money += self.money_each_player_round

                elif move == "R":  # If one chose "Raise"
                    raise_by = min(self.players[i].get_balance(), int(input("How much money? ")))
                    last_raised = i
                    self.players[i].pay_move(raise_by)
                    self.money_each_player_round += raise_by
                    self.stack_money += self.money_each_player_round

                elif move == "F":  # If one chose "Fold"
                    self.active_players -= 1
                    if self.active_players == 1:
                        break
                    self.players[i].turn_off_active()

            i = (i+1) % self.num_of_player  # go to next player.
        self.money_each_player_round = 0

    def open_cards_to_deck(self, num_of_cards) -> None:
        """
        Open a given number of cards to deck.
        :param num_of_cards: The given number of cards.
        :return: None.
        """
        for i in range(num_of_cards):
            self.open_cards.append(self.deck.open_card())

    def deal_cards(self) -> None:
        """
        Deal 2 cards to each player.
        :return: None.
        """
        for player in self.players:
            for i in range(CARDS_TO_BEGIN_WITH):
                player.take_card(self.deck.open_card())

    def show_open_cards(self) -> None:
        """
        Show open cards in deck to CLI
        :return: None
        """
        open_cards = ''
        if len(self.open_cards) > 0:
            for i in range(len(self.open_cards)):
                open_cards += str(self.open_cards[i][0]) + " of " + self.dict_of_types[self.open_cards[i][1]]
                if i != len(self.open_cards):
                    open_cards += " | "
        else:
            open_cards = "There Are None"
        print(SHOW_OPEN_CARDS.format(open_cards))

    def convert_card_to_string(self, card) -> str:
        """
        Convert card from [1:3] -> 1 of clove for example - for printing.
        :param card: a given card.
        :return: string.
        """
        card_num = str(card[0])
        card_type = self.dict_of_types[card[1]]
        return card_num + " of " + card_type

    def prize_winner(self) -> None:
        """
        Check for the winner among all active players, write winning message and add money to hs balance.
        :return: None
        """
        if self.active_players == 1:
            for i in range(len(self.players)):
                if self.players[i].is_active():
                    print(WINNER.format(str(i), str(self.stack_money)))
                    # self.players[i].add_money(self.stack_money)
        else:
            last_cards = dict()
            for i in range(len(self.players)):
                if self.players[i].is_active():
                    last_cards[i] = self.players[i].get_cards()
            rules = Rules(last_cards, self.open_cards)
            winner = rules.find_winner()
            print(WINNER.format(str(winner), str(self.stack_money)))
            # self.players[winner].add_money(self.stack_money)


