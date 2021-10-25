from CardStack import CardStack
from HandsChecker import HandsChecker
from Messages import Messages
from MoneyStack import MoneyStack


class PokerRules(object):
    """
    A set of utility of poker rules.
    """

    # Constant for the rules:
    NUM_OF_ROUNDS = 4
    CARDS_PER_ROUND = [0, 3, 1, 1]
    CARDS_PER_PLAYER = 2
    HANDS = {"Royal Flush": HandsChecker.check_royal_flush,
             "Straight Flush":  HandsChecker.check_straight_flush,
             "Four of a Kind": HandsChecker.check_four_of_a_kind,
             "Full House": HandsChecker.check_full_house,
             "Flush": HandsChecker.check_flush,
             "Straight": HandsChecker.check_straight,
             "Three of a Kind": HandsChecker.check_three_of_a_kind,
             "Two Pair": HandsChecker.check_two_pair,
             "Pair": HandsChecker.check_pair}

    @staticmethod
    def winner(card_stack: CardStack, money_stack: MoneyStack, players: list) -> None:
        """
        A static method gets the players at the end of the game and determine the winner.
        :param card_stack: The card stack on the table.
        :param money_stack: The money stack on the table.
        :param players: The list of players.
        :return: None.
        """
        active_players = [player for player in players if player.is_active()]  # Use only the active players.
        PokerRules.add_cards_to_players(active_players, card_stack)
        for hand, func in PokerRules.HANDS.items():
            players_with_hand = list(filter(func, active_players))
            if len(players_with_hand) > 0:
                PokerRules.print_winner(players_with_hand, money_stack, hand)
                break
        else:
            players_with_high_card = PokerRules.check_high_card(active_players)
            PokerRules.print_winner(players_with_high_card, money_stack)

    @staticmethod
    def print_winner(players: list, money_stack: MoneyStack, hand="High Card") -> None:
        """
        Print the winner or winners (in case there are some) and the amount of money (split if needed)
        :param players: The players who won.
        :param money_stack: The amount of money the players won from the stack.
        :param hand: The hand the players won with.
        :return: None.
        """
        if len(players) > 1:
            print(Messages.WINNER)
            for player in players:
                print(player.get_name())
            print(Messages.COUPLE_WINNERS.format(hand, int(money_stack.get_money() / len(players))))
        else:
            print(Messages.WINNER)
            print(players[0].get_name())
            print(Messages.ONE_WINNER.format(hand, int(money_stack.get_money())))
        # Here I can add a logic to give the money, using money_stack.give_money to the winners.

    @staticmethod
    def add_cards_to_players(players: list, card_stack: CardStack) -> None:
        """
        Combine the stack cards and the players cards for determining the winning hand.
        :param players: The list of players.
        :param card_stack: The stack of cards on the table.
        :return: None.
        """
        cards = card_stack.get_cards()
        for player in players:
            for card in cards:
                player.cards_stack.add_card(card)

    @staticmethod
    def check_high_card(players):
        """
        Check the highest card, in case none of the active player has no hand.
        :param players: A list of players.
        :return: The list of players with the high card.
        """
        players_by_card = [[] for i in range(13)]
        for player in players:
            player_cards = [0 for i in range(13)]
            for card in player.cards_stack.get_cards():
                player_cards[card.get_num().value] += 1
            for i in range(len(player_cards) - 1, -1, -1):
                if player_cards[i] > 0:
                    players_by_card[i].append(player)
                    break
        for lst in reversed(players_by_card):
            if len(lst) > 0:
                return lst
        return []  # we will not arrive to this point because there is at least one player playing
